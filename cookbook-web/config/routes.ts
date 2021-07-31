export default [
  {
    path: '/',
    redirect: '/home',
  },
  {
    path: '/home',
    name: 'Home',
    icon: 'Home',
    component: './Home',
  }, // {
  //   path: '/user',
  //   layout: false,
  //   routes: [
  //     {
  //       path: '/user',
  //       routes: [
  //         {
  //           name: 'Login',
  //           path: '/user/login',
  //           component: './user/Login',
  //         },
  //       ],
  //     },
  //     {
  //       component: './404',
  //     },
  //   ],
  // },
  {
    path: '/user',
    layout: false,
    routes: [
      {
        path: '/user/login',
        layout: false,
        name: 'login',
        component: './user/Login',
      },
      {
        path: '/user/register',
        layout: false,
        name: 'register',
        component: './user/Register',
      },
      {
        path: '/user',
        redirect: '/user/login',
      },
      // {
      //   name: 'register-result',
      //   layout: false,
      //   path: '/user/register-result',
      //   component: './user/register-result',
      // },
      {
        component: '404',
      },
    ],
  },
  // 'layout: false' means a component will not be wrapped in BasicLayout.
  {
    path: '/account',
    routes: [
      {
        name: 'center',
        path: '/account/center',
        component: './Account/Center',
      },
      {
        name: 'settings',
        path: '/account/settings',
        component: './Account/Setting',
      },
      {
        path: '/account',
        redirect: '/account/center',
      },
      {
        component: '404',
      },
    ],
  },
  {
    name: 'Demo Table Page',
    icon: 'table',
    path: '/list',
    component: './TableList',
  },
  // {
  //   name: '注册页',
  //   icon: 'smile',
  //   path: '/register',
  //   component: './user/Register',
  // },
  
  // not enterable
  // {
  //   path: '/admin',
  //   name: '管理页',
  //   icon: 'crown',
  //   access: 'canAdmin',
  //   component: './Admin',
  //   routes: [
  //     {
  //       path: '/admin/sub-page',
  //       name: '二级管理页',
  //       icon: 'smile',
  //       component: './Home',
  //     },
  //     {
  //       component: './404',
  //     },
  //   ],
  // },
  {
    component: './404',
  },
];
