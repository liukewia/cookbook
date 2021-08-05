import type { Settings as LayoutSettings } from '@ant-design/pro-layout';
import { PageLoading } from '@ant-design/pro-layout';
import { request as umiRequest, RequestConfig, RunTimeLayoutConfig } from 'umi';
import { history, Link } from 'umi';
import RightContent from '@/components/RightContent';
import Footer from '@/components/Footer';
import { currentUser as queryCurrentUser } from './services/ant-design-pro/api';
import { BookOutlined, LinkOutlined } from '@ant-design/icons';
import Exception403Page from './pages/403';
import { message } from 'antd';
import { isDev } from './global';

// const isDev = process.env.NODE_ENV === 'development';
const loginPath = '/user/login';

/** 获取用户信息比较慢的时候会展示一个 loading */
export const initialStateConfig = {
  loading: <PageLoading />,
};

/**
 * @see  https://umijs.org/zh-CN/plugins/plugin-initial-state
 * */
export async function getInitialState(): Promise<{
  settings?: Partial<LayoutSettings>;
  currentUser?: API.CurrentUser;
  fetchUserInfo?: () => Promise<API.CurrentUser | undefined>;
}> {
  const fetchUserInfo = async () => {
    try {
      const msg = await queryCurrentUser();
      return msg.data;
    } catch (error) {
      console.log('getInitialState error: ', error);
      history.push(loginPath);
    }
    return undefined;
  };
  // 如果是登录页面，不执行
  if (history.location.pathname !== loginPath) {
    const currentUser = await fetchUserInfo();
    console.log('InitialState, not loginPath: ', {
      fetchUserInfo,
      currentUser,
      settings: {},
    });
    return {
      fetchUserInfo,
      currentUser,
      settings: {},
    };
  }

  console.log('InitialState, is loginPath: ', {
    fetchUserInfo,
    settings: {},
  });
  return {
    fetchUserInfo,
    settings: {},
  };
}

// ProLayout 支持的api https://procomponents.ant.design/components/layout
export const layout: RunTimeLayoutConfig = ({ initialState }) => {
  return {
    rightContentRender: () => <RightContent />,
    disableContentMargin: false,
    // waterMarkProps: {
    //   content: initialState?.currentUser?.name,
    // },
    footerRender: () => <Footer />,
    onPageChange: () => {
      // const { location } = history;
      // // 如果没有登录，重定向到 login
      // // dont redirect for guest
      // if (!initialState?.currentUser && location.pathname !== loginPath) {
      //   history.push(loginPath);
      // }
    },
    links: isDev
      ? [
          <Link to="/umi/plugin/openapi" target="_blank">
            <LinkOutlined />
            <span>OpenAPI 文档</span>
          </Link>,
          <Link to="/~docs">
            <BookOutlined />
            <span>业务组件文档</span>
          </Link>,
        ]
      : [],
    menuHeaderRender: undefined,
    // customized 403 page
    unAccessible: <Exception403Page />,
    ...initialState?.settings,
    // locale: 'en-US',
  };
};

// https://umijs.org/plugins/plugin-request#%E8%BF%90%E8%A1%8C%E6%97%B6%E9%85%8D%E7%BD%AE
export const request: RequestConfig = {
  errorHandler: (err) => {
    // console.log('err', JSON.stringify(err));
    message.error(err.data?.data?.message || `${err.request?.options?.method} ${err.request?.url} Failed`);
  },
};

let extraRoutes: any;

export function render(oldRender: any) {
  umiRequest('/api/get_all_categories/')
    .then((res) => {
      // console.log('res?.data: ', res?.data?.categories);
      extraRoutes = res?.data?.categories?.map((cat: any) => ({
        name: cat.categoryName,
        path: `/${cat.categorySlug}`,
      }));
      // console.log('extraRoutes: ', extraRoutes);
      oldRender();
    })
    .catch((err) => {
      message.error('Cannot fetch categories!');
      oldRender();
    });
}

// https://github.com/umijs/umi/issues/2511
// https://www.codenong.com/cs109219288/
// https://umijs.org/zh-CN/docs/runtime-config
export function patchRoutes({ routes }) {
  // console.log('extraRoutes: ', extraRoutes);
  if (extraRoutes) {
    const _routes = routes.find((ele) => ele.path === '/').routes;
    const tmpRouteIdx = _routes.indexOf(_routes.find((ele) => ele.routeKey === 'tmp'));
    const comp = _routes[tmpRouteIdx].component;
    _routes.splice(
      tmpRouteIdx,
      1,
      ...extraRoutes.map((r) => {
        r.component = comp;
        r.exact = true;
        return r;
      }),
    );
  }

  // console.log('routes: ', routes);
}
