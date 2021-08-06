import React from 'react';
import { Link, useRequest, useModel } from 'umi';
import { Card, List } from 'antd';
import MultiClamp from 'react-multi-clamp';
import styles from './index.less';

const Articles: React.FC = () => {
  const { initialState } = useModel('@@initialState');
  const { data: listData } = useRequest(
    `/api/my_recipe/${initialState?.currentUser?.id}/`,
  );
  return (
    <List
      className={styles.coverCardList}
      rowKey="id"
      grid={{ gutter: 24, xxl: 3, xl: 2, lg: 2, md: 2, sm: 2, xs: 1 }}
      dataSource={listData?.recipes || []}
      renderItem={(recipe: any) => (
        <List.Item>
          <Link to={`/recipe/${recipe.recipeId}`} key={`recipe-${recipe.recipeId}`}>
            <Card
              hoverable
              cover={
                <img
                  alt={`${recipe.recipeTitle} Picture`}
                  src={recipe.recipePic}
                  style={{ width: '100%', height: 240, objectFit: 'cover' }}
                />
              }
            >
              <Card.Meta
                title={
                  <MultiClamp ellipsis="..." clamp={1}>
                    {recipe.recipeTitle}
                  </MultiClamp>
                }
              />
            </Card>
          </Link>
        </List.Item>
      )}
    />
  );
};

export default Articles;
