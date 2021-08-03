import { GithubOutlined } from '@ant-design/icons';
import { DefaultFooter } from '@ant-design/pro-layout';
import { useModel } from 'umi';

export default () => {
  const { initialState } = useModel('@@initialState');
  // console.log('initialState: ', initialState);
  const defaultMessage = 'Crafted with ❤ by the Yellow Duck';
  return (
    <DefaultFooter
      copyright={`2021 ${defaultMessage}`}
      links={[
        {
          key: 'Contact Us',
          title: 'Contact Us',
          href: 'mailto:fo1ivoraaa@gmail.com',
          blankTarget: true,
        },
        {
          key: 'Github',
          title: <GithubOutlined />,
          href: 'https://github.com/SH-giant/cookbook',
          blankTarget: true,
        },
        {
          key: 'About',
          title: 'About',
          href: '/about',
          blankTarget: false,
        },
      ]}
    />
  );
};
