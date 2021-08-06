import { LikeFilled, LikeOutlined } from '@ant-design/icons';
import { PageContainer } from '@ant-design/pro-layout';
import { Card, message, Space } from 'antd';
import { Link, useLocation, useRequest } from 'umi';
import MultiClamp from 'react-multi-clamp';
import { createElement, useState } from 'react';
import { useAccess } from 'umi';

export default function CategoryHub() {
  const { pathname } = useLocation();
  const { data, run: refresh } = useRequest(`/api/category${pathname}/`);

  const [didLike, setDidLike] = useState(false);
  const { run: runLike } = useRequest(`/api/category${pathname}/cate_add_like/`, {
    manual: true,
  });
  const access = useAccess();

  const like = () => {
    if (!access.isLoggedin) {
      message.warn('Need login to like');
      return;
    }
    if (!didLike) {
      setDidLike(true);
      runLike();
      setTimeout(() => {
        refresh();
      }, 100);
    }
  };

  return (
    <PageContainer
      extra={
        data ? (
          <span onClick={like} style={didLike ? undefined : { cursor: 'pointer' }}>
            {createElement(didLike ? LikeFilled : LikeOutlined)}
            <span style={{ paddingLeft: 8 }}>{data?.categoryLikes}</span>
          </span>
        ) : null
      }
    >
      <Space wrap size="middle">
        {data?.recipes?.map((recipe: any) => (
          <Link to={`/recipe/${recipe.recipeId}`} key={`recipe-${recipe.recipeId}`}>
            <Card
              hoverable
              style={{ width: 240 }}
              cover={
                <img
                  alt={`${recipe.recipeTitle} Picture`}
                  src={recipe.recipeUrl}
                  style={{ width: 240, height: 240, objectFit: 'cover' }}
                />
              }
            >
              <Card.Meta
                title={recipe.recipeTitle}
                description={
                  <MultiClamp ellipsis="..." clamp={1}>
                    {recipe.recipeDirection}
                  </MultiClamp>
                }
              />
            </Card>
          </Link>
        ))}
      </Space>
    </PageContainer>
  );
}
