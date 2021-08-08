# 食谱发布与分享网站

🌟🌟🌟online demo🌟🌟🌟: http://finnlewis.pythonanywhere.com/

## 解决的问题

修改权限逻辑，在路由配置内可声明式地配置权限，在组件内可以 hook 形式调用权限信息集合，实现细粒度的权限控制; 用户既可以游客身份浏览，也可以注册或登录后进行评论、点赞和发布食谱等操作。

进入首屏时使用服务端传回的食谱种类数据加载路由，并展示在顶栏，实现不依赖前端初始路由的动态菜单栏。

借 webpack 能力将前端构建中的静态产物部署在子路由上，供后端识别; 首次加载时从服务端获取 CSRF token 并附在后 续 POST 请求头部，提高站点通信安全性。

支持响应式布局，完全适配各类移动端浏览。

前端构建产物部署时，将文件部署在 /static/ 子路由下，供 django 识别；

外部 Bing API 通过 django 后端来代理请求，再将 json response 返回前端。

## problems solved

Modify the permission logic. The permissions can be configured declaratively in the routing configuration, and the permission information collection can be called in the form of hooks in the component to achieve fine-grained permission control; users can browse as tourists, or register or log in to comment and click Like and publish recipes and other operations.

When entering the first screen, use the recipe type data returned by the server to load the route and display it on the top bar to realize a dynamic menu bar that does not rely on the initial route of the front end.

With the help of webpack capabilities, the static products in the front-end construction are deployed on the sub-routes for the back-end identification; the CSRF token is obtained from the server at the first load and attached to the header of the subsequent POST request to improve site communication security.

Support responsive layout, fully adapt to all kinds of mobile terminal browsing.

When the front-end build product is deployed, the file is deployed under the /static/ sub-route for django to recognize;

The external Bing API proxy requests through the django backend, and then returns the json response to the frontend.