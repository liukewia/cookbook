import { GithubOutlined } from '@ant-design/icons';
import { DefaultFooter } from '@ant-design/pro-layout';

export default () => {
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
