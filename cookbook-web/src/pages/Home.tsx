import React from 'react';
import { PageContainer } from '@ant-design/pro-layout';
import { Card, Image, Space, Descriptions } from 'antd';
import styles from './Home.less';
import { Link, useRequest } from 'umi';
import MultiClamp from 'react-multi-clamp';

// const CodePreview: React.FC = ({ children }) => (
//   <pre className={styles.pre}>
//     <code>
//       <Typography.Text copyable>{children}</Typography.Text>
//     </code>
//   </pre>
// );

export default (): React.ReactNode => {
  const { data } = useRequest('/api/get_all_recipes/');

  return (
    <PageContainer title="Home">
      <Card title="Most Liked Recipes">
        <Space direction="vertical" style={{ width: '100%' }}>
          {data?.recipes
            ? data?.recipes?.map((recipe: any) => (
                <Link to={`/recipe/${recipe.recipeId}/`} key={`recipe-${recipe.recipeId}`}>
                  <Card hoverable>
                    <Space size="large" style={{ width: '100%' }}>
                      <Image
                        preview={false}
                        alt={`${recipe.recipeTitle} Picture`}
                        style={{ width: 200, height: 200, objectFit: 'cover' }}
                        src={recipe.recipePicture}
                      />
                      <Descriptions title={recipe.recipeTitle} style={{ width: '100%' }}>
                        <Descriptions.Item style={{ width: '100%' }}>
                          <MultiClamp ellipsis="..." clamp={3}>
                            {recipe.recipeDirection as string}
                          </MultiClamp>
                        </Descriptions.Item>
                      </Descriptions>
                    </Space>
                  </Card>
                </Link>
              ))
            : null}
        </Space>
      </Card>
      {/* <Card
      style={{ overflow: 'hidden' }}
      >
        <Space>
          <Image width={200} placeholder src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png" />
          <Descriptions title="User Info">
            <Descriptions.Item label="UserName">Zhou Maomao</Descriptions.Item>
          </Descriptions>
        </Space>
      </Card> */}
      {/* <Card>
        <Alert
          message={'更快更强的重型组件，已经发布。'}
          type="success"
          showIcon
          banner
          style={{
            margin: -12,
            marginBottom: 24,
          }}
        />
        <Typography.Text strong>
          高级表格{' '}
          <a
            href="https://procomponents.ant.design/components/table"
            rel="noopener noreferrer"
            target="__blank"
          >
            欢迎使用
          </a>
        </Typography.Text>
        <CodePreview>yarn add @ant-design/pro-table</CodePreview>
        <Typography.Text
          strong
          style={{
            marginBottom: 12,
          }}
        >
          高级布局{' '}
          <a
            href="https://procomponents.ant.design/components/layout"
            rel="noopener noreferrer"
            target="__blank"
          >
            欢迎使用
          </a>
        </Typography.Text>
        <CodePreview>yarn add @ant-design/pro-layout</CodePreview>
      </Card> */}
    </PageContainer>
  );
};
