export default [
  {
    path: '/',
    redirect: '/home',
  },
  {
    path: '/home',
    component: './Home',
  },
  // {
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
        name: 'Login',
        component: './user/Login',
      },
      {
        path: '/user/register',
        layout: false,
        name: 'Register',
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
  // if 'name' is not presented, it will not be added to header.
  // {
  //   path: '/about',
  //   routes: [
  //     {
  //       name: 'About',
  //       path: '/about',
  //       component: './About',
  //     },
  //   ],
  // },
  {
    path: '/about',
    component: './About',
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
    path: 'tmp',
    routeKey: 'tmp',
    component: './CategoryHub',
  },
  {
    component: './404',
  },
];
