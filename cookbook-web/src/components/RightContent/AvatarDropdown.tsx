import React, { useCallback } from 'react';
import {
  EditOutlined,
  LoginOutlined,
  LogoutOutlined,
  PlusOutlined,
  SettingOutlined,
  UserOutlined,
} from '@ant-design/icons';
import { Avatar, Menu, message, Spin } from 'antd';
import { history, useModel } from 'umi';
import { stringify } from 'querystring';
import HeaderDropdown from '../HeaderDropdown';
import styles from './index.less';
import { logout } from '@/services/ant-design-pro/api';
import type { MenuInfo } from 'rc-menu/lib/interface';
import { useAccess } from 'umi';

export type GlobalHeaderRightProps = {
  menu?: boolean;
};

/**
 * 退出登录，并且将当前的 url 保存
 */
export const loginOut = async () => {
  await logout();
  message.success('Successfully logged out.');
  const { query = {}, pathname } = history.location;
  const { redirect } = query;
  if (window.location.pathname !== '/user/login' && !redirect) {
    history.replace({
      pathname: '/user/login',
      search: stringify({
        redirect: pathname,
      }),
    });
  }
};

const login = async () => {
  const { query = {}, pathname } = history.location;
  const { redirect } = query;
  // Note: There may be security issues, please note
  if (window.location.pathname !== '/user/login' && !redirect) {
    history.replace({
      pathname: '/user/login',
      search: stringify({
        redirect: pathname,
      }),
    });
  }
};

const AvatarDropdown: React.FC<GlobalHeaderRightProps> = () => {
  const { initialState, setInitialState } = useModel('@@initialState');
  const access = useAccess();

  const onMenuClick = useCallback(
    (event: MenuInfo) => {
      const { key } = event;
      if (key === 'login') {
        if (initialState?.currentUser?.access === 'guest') {
          login();
        } else {
          window.location.reload();
        }
        return;
      }
      if (key === 'logout') {
        setInitialState((s) => ({
          ...s,
          currentUser: {
            access: 'guest',
            state: 'error',
          },
        }));
        loginOut();
        return;
      }
      // excludes login and logout circumstances
      history.push(`${key}`);
    },
    [setInitialState],
  );

  // const loading = (
  //   <span className={`${styles.action} ${styles.account}`}>
  //     <Spin
  //       size="small"
  //       style={{
  //         marginLeft: 8,
  //         marginRight: 8,
  //       }}
  //     />
  //   </span>
  // );

  // if (!initialState) {
  //   return loading;
  // }
  const { currentUser } = initialState;
  // if (!currentUser?.access) {
  //   return loading;
  // }

  const menuHeaderDropdown = (
    <Menu className={styles.menu} selectedKeys={[]} onClick={onMenuClick}>
      {access.isLoggedin && (
        <Menu.Item key="/post-recipe">
          <EditOutlined />
          Post Recipe
        </Menu.Item>
      )}
      {access.isLoggedin && (
        <Menu.Item key="/add-category">
          <PlusOutlined />
          Add Category
        </Menu.Item>
      )}
      {access.isLoggedin && (
        <Menu.Item key="/account/center">
          <UserOutlined />
          Personal Center
        </Menu.Item>
      )}
      {access.isLoggedin && (
        <Menu.Item key="/account/settings">
          <SettingOutlined />
          Settings
        </Menu.Item>
      )}
      {access.isLoggedin && <Menu.Divider />}

      {access.isLoggedin ? (
        <Menu.Item key="logout">
          <LogoutOutlined />
          Logout
        </Menu.Item>
      ) : (
        <Menu.Item key="login">
          <LoginOutlined />
          Login
        </Menu.Item>
      )}
    </Menu>
  );
  return (
    <HeaderDropdown overlay={menuHeaderDropdown}>
      <span className={`${styles.action} ${styles.account}`}>
        <Avatar
          size="small"
          className={styles.avatar}
          src="https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png"
          alt="avatar"
        />
        <span className={`${styles.name} anticon`}>
          {currentUser?.firstName || currentUser?.userName || 'Guest'}
        </span>
      </span>
    </HeaderDropdown>
  );
};

export default AvatarDropdown;
