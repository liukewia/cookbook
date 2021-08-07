// @ts-ignore
/* eslint-disable */
import { request } from 'umi';
import Cookies from 'universal-cookie';

/** get_csrf_token GET /api/get_csrf_token */
export async function getCsrfToken(options?: { [key: string]: any }) {
  return new Cookies().get('csrftoken') || request('/api/get_csrf_token/', {
    method: 'GET',
    ...(options || {}),
  });
}


/** getuserinfo GET /api/getuserinfo */
export async function queryCurrentUser(options?: { [key: string]: any }) {
  return request('/api/user/getuserinfo/', {
    method: 'GET',
    ...(options || {}),
  });
}

/** log out POST /api/logout */
export async function logout(options?: { [key: string]: any }) {
  return request<Record<string, any>>('/api/user/logout/', {
    method: 'GET',
    ...(options || {}),
  });
}

/** log in POST /api/login/account */
export async function login(body: API.LoginParams, options?: { [key: string]: any }) {
  return request('/api/user/login/', {
    method: 'POST',
    // headers: {
    //   'Content-Type': 'application/json',
    // },
    data: body,
    ...(options || {}),
  });
}

/** get newly pushed messages GET /api/notices */
export async function getNotices(options?: { [key: string]: any }) {
  return request<API.NoticeIconList>('/api/notices', {
    method: 'GET',
    ...(options || {}),
  });
}

/** 获取规则列表 GET /api/rule */
export async function rule(
  params: {
    // query
    /** 当前的页码 */
    current?: number;
    /** 页面的容量 */
    pageSize?: number;
  },
  options?: { [key: string]: any },
) {
  return request<API.RuleList>('/api/rule', {
    method: 'GET',
    params: {
      ...params,
    },
    ...(options || {}),
  });
}

/** 新建规则 PUT /api/rule */
export async function updateRule(options?: { [key: string]: any }) {
  return request<API.RuleListItem>('/api/rule', {
    method: 'PUT',
    ...(options || {}),
  });
}

/** 新建规则 POST /api/rule */
export async function addRule(options?: { [key: string]: any }) {
  return request<API.RuleListItem>('/api/rule', {
    method: 'POST',
    ...(options || {}),
  });
}

/** 删除规则 DELETE /api/rule */
export async function removeRule(options?: { [key: string]: any }) {
  return request<Record<string, any>>('/api/rule', {
    method: 'DELETE',
    ...(options || {}),
  });
}
