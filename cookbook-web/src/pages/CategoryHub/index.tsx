import { LikeOutlined } from '@ant-design/icons';
import { PageContainer } from '@ant-design/pro-layout';
import { Card, Space } from 'antd';
import { Link, useLocation, useRequest } from 'umi';
import MultiClamp from 'react-multi-clamp';
import styles from './index.less';

export default function CategoryHub() {
  const { pathname } = useLocation();
  // const categoryName = pathname.replace(/\//g, '');
  const { data } = useRequest(`/api/category${pathname}/`);

  return (
    <PageContainer
      extra={
        data ? (
          <span>
            <LikeOutlined />
            <span className={styles['comment-action']}>{data?.categoryLikes}</span>
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
