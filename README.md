# 食谱发布与分享网站 Cookbook

🌟🌟🌟online demo🌟🌟🌟: http://finnlewis.pythonanywhere.com/

## 解决的问题

* 修改权限逻辑，在路由配置内可声明式地配置权限，在组件内可以 hook 形式调用权限信息集合，实现细粒度的权限控制; 用户既可以游客身份浏览，也可以注册或登录后进行评论、点赞和发布食谱等操作。

* 进入首屏时使用服务端传回的食谱种类数据加载路由，并展示在顶栏，实现不依赖前端初始路由的动态菜单栏。

* 借 webpack 能力将前端构建中的静态产物部署在 /static/ 子路由上，供 django 后端识别; 首次加载时从服务端获取 CSRF token 并附在后 续 POST 请求头部，提高站点通信安全性。

* 支持响应式布局，完全适配各类移动端浏览。

* 按工业级标准设计前后端通信 JSON 格式。

  ```js
  {
    success: bool,
    data: {
      ...
    }
    code: number,
    message?: string,
  }
  ```

* 外部 Bing API 通过 django 后端来代理请求，再将 json response 返回前端。

## 著作声明

项目流程原因导致本仓库需要 fork 另一个同名仓库。原仓库和本 fork 仓库的前端部分均为本人完成，详见原仓库前端部分提交者名字。

---

# Cookbook

## Problems solved

* Modified the permission logic. The permissions can be configured declaratively in the routing configuration, and the permission information collection can be called in the form of hooks in the component to achieve fine-grained permission control; users can browse as tourists, or register or log in to comment and click Like and publish recipes and other operations.

* When entering the first screen, used the recipe type data returned by the server to load the route and display it on the top bar to realize a dynamic menu bar that does not rely on the initial route of the front end.

* Used webpack capabilities to deploy the static products in the front-end construction on the /static/ sub-route for identification by the django back-end; obtain the CSRF token from the server when it is first loaded and attach it to the header of the subsequent POST request to improve site communication security.

* Supports responsive layout, fully adapt to all kinds of mobile terminal browsing.

* The front-end and back-end communication JSON format is designed according to industrial standards.

  ```js
  {
    success: bool,
    data: {
      ...
    }
    code: number,
    message?: string,
  }
  ```

* The external Bing API proxy requests through the django backend, and then returns the json response to the frontend.

## Integrity statement

The project process causes this repo to have forked another one with the same name. The front-end parts of the original repo and this fork one were completed by myself, please see the submitter's name in the front end part of the original repo for details.
