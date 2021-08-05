import { LikeOutlined } from '@ant-design/icons';
import { PageContainer } from '@ant-design/pro-layout';
import { Card, Descriptions, Space, Spin } from 'antd';
import { Link, useLocation, useParams, useRequest } from 'umi';
import MultiClamp from 'react-multi-clamp';
import ProCard from '@ant-design/pro-card';
import styles from './index.less';

export default function Recipe() {
  const { recipeId } = useParams<{ recipeId: string }>();
  const { data } = useRequest(`/api/recipe/${recipeId}/`);
  console.log('data: ', data);

  return (
    <PageContainer
      title={data?.recipeTitle || ''}
      extra={
        data ? (
          <span>
            <LikeOutlined />
            <span className={styles['comment-action']}>{data?.recipeLike}</span>
          </span>
        ) : null
      }
    >
      <Space size="large" direction="vertical">
        <ProCard split="vertical" layout="center">
          <ProCard colSpan="30%">
            {data ? (
              <img
                alt={`${data?.recipeTitle} Picture`}
                src={data?.recipeUrl}
                className={styles['recipe-img']}
              />
            ) : (
              <Spin />
            )}
          </ProCard>
          <ProCard>
            <Descriptions
              title="Recipe Detail"
              column={1}
              bordered
              labelStyle={{ fontSize: '1.005rem' }}
              contentStyle={{ fontSize: '1.005rem' }}
            >
              <Descriptions.Item label="Recipe Name">{data?.recipeTitle}</Descriptions.Item>
              <Descriptions.Item label="Ingredients">
                {data?.recipeIngredients.map((ingredient: any, index: number) => (
                  <div key={`ing-idx-${index}`}>{`${index + 1}.${'\u00A0'}${'\u00A0'}${ingredient}`}</div>
                ))}
              </Descriptions.Item>
            </Descriptions>
          </ProCard>
        </ProCard>
        <ProCard title="Direction" style={{ fontSize: '1.005rem' }}>
          {data?.recipeDirections.map((dir: any, index: number) => (
            <div key={`ing-idx-${index}`}>{`Step ${index + 1}:${'\u00A0'}${'\u00A0'}${dir}`}</div>
          ))}
        </ProCard>
      </Space>
    </PageContainer>
  );
}
