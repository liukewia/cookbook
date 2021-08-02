// https://umijs.org/config/
import { defineConfig } from 'umi';
import { join } from 'path';
import defaultSettings from './defaultSettings';
import proxy from './proxy';
import routes from './routes';
const { REACT_APP_ENV } = process.env;
export default defineConfig({
  hash: true,
  antd: {},
  dva: {
    hmr: true,
  },
  layout: {
    // https://umijs.org/zh-CN/plugins/plugin-layout
    locale: false,
    siderWidth: 208,
    ...defaultSettings,
  },
  dynamicImport: {
    loading: '@ant-design/pro-layout/es/PageLoading',
  },
  targets: {
    ie: 11,
  },
  // umi routes: https://umijs.org/docs/routing
  routes,
  // Theme for antd: https://ant.design/docs/react/customize-theme-cn
  theme: {
    'primary-color': defaultSettings.primaryColor,
  },
  // esbuild is father build tools
  // https://umijs.org/plugins/plugin-esbuild
  esbuild: {},
  title: false,
  ignoreMomentLocale: true,
  proxy: proxy[REACT_APP_ENV || 'dev'],
  manifest: {
    basePath: '/',
  },
  // Fast Refresh 热更新
  fastRefresh: {},
  openAPI: [
    {
      requestLibPath: "import { request } from 'umi'",
      // 或者使用在线的版本
      // schemaPath: "https://gw.alipayobjects.com/os/antfincdn/M%24jrzTTYJN/oneapi.json"
      schemaPath: join(__dirname, 'oneapi.json'),
      mock: false,
    },
    {
      requestLibPath: "import { request } from 'umi'",
      schemaPath: 'https://gw.alipayobjects.com/os/antfincdn/CA1dOm%2631B/openapi.json',
      projectName: 'swagger',
    },
  ],
  nodeModulesTransform: {
    type: 'none',
  },
  // http://localhost:8000
  // mfsu: {},
  webpack5: {},
  exportStatic: {},
  locale: {
    default: 'en-US',
    antd: true,
  },
  // chainWebpack(config) {
  //   const isDev = process.env.NODE_ENV === 'development';
  //   const hash = !isDev ? '.[contenthash:8]' : '';
  //   config.output.chunkFilename(`static/[name]${hash}.async.js`);

  //   config.plugin('extract-css').tap((args) => [
  //     {
  //       ...args[0],
  //       chunkFilename: `static/[name]${hash}.chunk.css`,
  //     },
  //   ]);
  //   config.output.filename(`static/[name]${hash}.js`);
  //   config.output.filename(`static/[name]${hash}.css`);
  // },
  // chainWebpack(config, { webpack }) {
  //   const isDev = process.env.NODE_ENV === 'development';
  //   const hash = !isDev ? '.[contenthash:8]' : '';
  //   config.output.chunkFilename(`static/[name]${hash}.async.js`);
  //   config.output.filename(`static/[name]${hash}.js`);
  //   config.plugin('extract-css').tap((args) => [
  //     {
  //       ...args[0],
  //       chunkFilename: `static/[name]${hash}.chunk.css`,
  //       filename: `static/[name]${hash}.css`,
  //     },
  //   ]);
  // },
  publicPath: process.env.NODE_ENV === 'production' ? '/static/' : '/',
});
