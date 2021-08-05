/**
 * @see https://umijs.org/zh-CN/plugins/plugin-access
 * */
export default function access(initialState: { currentUser?: any }) {
  const { currentUser } = initialState || {};
  return {
    isAdmin: currentUser?.access === 'admin',
    isLoggedin: currentUser?.access === 'admin' || currentUser?.access === 'user',
  };
}
