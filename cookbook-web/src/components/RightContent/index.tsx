import { Space } from 'antd';
import React, { useState } from 'react';
import { useModel, useRequest } from 'umi';
import Avatar from './AvatarDropdown';
import HeaderSearch from '../HeaderSearch';
import styles from './index.less';

export type SiderTheme = 'light' | 'dark';

const GlobalHeaderRight: React.FC = () => {
  const { initialState } = useModel('@@initialState');
  // const [params, setParams] = useState('');
  const { data, run: search } = useRequest((value) => `/api/bing_search?q=${value}`, {
    manual: true,
    debounceInterval: 200,
  });

  if (!initialState || !initialState.settings) {
    return null;
  }

  const { navTheme, layout } = initialState.settings;
  let className = styles.right;

  if ((navTheme === 'dark' && layout === 'top') || layout === 'mix') {
    className = `${styles.right}  ${styles.dark}`;
  }

  return (
    <Space className={className}>
      <HeaderSearch
        className={`${styles.action} ${styles.search}`}
        placeholder="global search"
        defaultValue=""
        options={data?.results?.map((result: any) => ({
          label: <a href={result.link}>{result.title}</a>,
          value: result.title,
        }))}
        // [
        //   {
        //     label: <a href="https://umijs.org/zh/guide/umi-ui.html">umi ui</a>,
        //     value: 'umi ui',
        //   },
        //   {
        //     label: <a href="next.ant.design">Ant Design</a>,
        //     value: 'Ant Design',
        //   },
        //   {
        //     label: <a href="https://protable.ant.design/">Pro Table</a>,
        //     value: 'Pro Table',
        //   },
        //   {
        //     label: <a href="https://prolayout.ant.design/">Pro Layout</a>,
        //     value: 'Pro Layout',
        //   },
        // ]
        onChange={(value) => {
          search(value);
        }}
      />
      {/* <span
        className={styles.action}
        onClick={() => {
          window.open('https://pro.ant.design/docs/getting-started');
        }}
      >
        <QuestionCircleOutlined />
      </span> */}
      <Avatar menu={initialState?.currentUser?.access !== 'guest'} />
    </Space>
  );
};

export default GlobalHeaderRight;
