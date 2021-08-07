import React from 'react';
import { PageContainer } from '@ant-design/pro-layout';
import { Card, Image, Space, Typography } from 'antd';
import { Link, useRequest } from 'umi';
import MultiClamp from 'react-multi-clamp';
import CenteredSpinner from '@/components/CenteredSpinner';
import styles from './Home.less';

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
                      <div style={{ width: '100%' }}>
                        <Typography.Title level={3}>
                          <MultiClamp ellipsis="..." clamp={1}>
                            {recipe.recipeTitle}
                          </MultiClamp>
                        </Typography.Title>
                        <Typography.Text>
                          <MultiClamp ellipsis="..." clamp={3}>
                            {recipe.recipeDirection}
                          </MultiClamp>
                        </Typography.Text>
                      </div>
                    </Space>
                  </Card>
                </Link>
              ))
            : <CenteredSpinner />}
        </Space>
      </Card>
    </PageContainer>
  );
};
