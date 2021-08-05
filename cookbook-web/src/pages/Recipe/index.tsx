import { LikeOutlined } from '@ant-design/icons';
import { PageContainer } from '@ant-design/pro-layout';
import { Descriptions, List, Space, Spin, Comment, Avatar, Form, Button, message } from 'antd';
import { useParams, useRequest } from 'umi';
import ProCard from '@ant-design/pro-card';
import styles from './index.less';
import { avatars } from '@/global';
import TextArea from 'antd/lib/input/TextArea';
import { useMemo, useState } from 'react';

const Editor = ({ onRefresh }) => {
  const [form] = Form.useForm();
  const { recipeId } = useParams<{ recipeId: string }>();
  const { run } = useRequest(
    (values) => ({
      url: `/api/recipe/${recipeId}/add_review/`,
      method: 'post',
      data: values,
    }),
    {
      manual: true,
      onSuccess: (result) => {
        if (result?.userName) {
          message.success('Successfully commented.');
        }
      },
    },
  );

  const { getFieldValue, resetFields, submit } = form;

  const onSubmit = () => {
    const content = getFieldValue('content');
    if (!content) {
      message.warn('Empty content!');
      return;
    }
    submit();
    run({ id: 3, content });
    resetFields();
    setTimeout(() => {
      onRefresh();
    }, 100);
  };

  return (
    <Form form={form}>
      <Form.Item name="content">
        <TextArea rows={4} />
      </Form.Item>
      <Form.Item>
        <Button onClick={onSubmit} type="primary">
          Add Comment
        </Button>
      </Form.Item>
    </Form>
  );
};

export default function Recipe() {
  const [randAvatars, setRandAvatars] = useState<string[]>([]);
  const { recipeId } = useParams<{ recipeId: string }>();
  const { data, run } = useRequest(`/api/recipe/${recipeId}/`,
  {
    onSuccess: (result) => {
      const newArr = [...randAvatars];
      for (let i = 0; i < result?.reviews?.length - randAvatars.length; i++) {
        newArr.unshift(avatars[Math.floor(Math.random() * avatars.length)]);
      }
      setRandAvatars(newArr);
    }
  });
  // console.log('data: ', data);

  return (
    <PageContainer
      title={`Recipe: ${data?.recipeTitle}`}
      extra={
        data ? (
          <span>
            <LikeOutlined />
            <span className={styles['comment-action']}>{data?.recipeLike}</span>
          </span>
        ) : null
      }
    >
      <Space size="large" direction="vertical" className={styles['page-card']}>
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
                  <div key={`ing-idx-${index}`}>{`${
                    index + 1
                  }.${'\u00A0'}${'\u00A0'}${ingredient}`}</div>
                ))}
              </Descriptions.Item>
            </Descriptions>
          </ProCard>
        </ProCard>
        <ProCard title="Directions" className={styles['desc']}>
          {data?.recipeDirections.map((dir: any, index: number) => (
            <div key={`ing-idx-${index}`}>{`Step ${
              index + 1
            }:${'\u00A0'}${'\u00A0'}${'\u00A0'}${dir}`}</div>
          ))}
        </ProCard>
        <ProCard title="Comment">
          <Comment
            avatar={
              <Avatar
                src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                alt="Han Solo"
              />
            }
            content={<Editor onRefresh={run} />}
          />
          {data?.reviews ? (
            <List
              className="comment-list"
              header={`${data?.reviews?.length} repl${data?.reviews?.length > 1 ? 'ies' : 'y'}`}
              itemLayout="horizontal"
              dataSource={data?.reviews}
              renderItem={(item: any, index: number) => {
                return (
                  <li>
                    <Comment
                      author={item.posterName}
                      avatar={randAvatars[index]}
                      content={item.reviewContent}
                      // datetime={item.datetime}
                    />
                  </li>
                );
              }}
            />
          ) : null}
        </ProCard>
      </Space>
    </PageContainer>
  );
}
