import { HeartOutlined, LikeFilled, LikeOutlined } from '@ant-design/icons';
import { PageContainer } from '@ant-design/pro-layout';
import { Descriptions, List, Space, Comment, Avatar, Form, Button, message } from 'antd';
import { useModel, useParams, useRequest } from 'umi';
import ProCard from '@ant-design/pro-card';
import styles from './index.less';
import { avatars } from '@/global';
import TextArea from 'antd/lib/input/TextArea';
import { createElement, useState } from 'react';
import { useAccess } from 'umi';
import Exception404Page from '../404';
import RcResizeObserver from 'rc-resize-observer';
import CenteredSpinner from '@/components/CenteredSpinner';

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
  const { initialState } = useModel('@@initialState');

  const { getFieldValue, resetFields, submit } = form;

  const onSubmit = () => {
    const content = getFieldValue('content');
    if (!content) {
      message.warn('Empty content!');
      return;
    }
    submit();
    run({ id: initialState?.currentUser?.id, content });
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
  const {
    data,
    run: refresh,
    loading,
  } = useRequest(`/api/recipe/${recipeId}/`, {
    onSuccess: (result) => {
      const newArr = [...randAvatars];
      for (let i = 0; i < result?.reviews?.length - randAvatars.length; i++) {
        newArr.unshift(avatars[Math.floor(Math.random() * avatars.length)]);
      }
      setRandAvatars(newArr);
    },
  });

  const access = useAccess();
  const { initialState } = useModel('@@initialState');
  const [didLike, setDidLike] = useState(false);
  const { run: runLike } = useRequest(`/api/recipe/${recipeId}/rec_add_like/`, {
    manual: true,
  });

  const { run: runAddToFav } = useRequest(
    (values) => ({
      url: '/api/add_to_favourite_recipe/',
      method: 'post',
      data: values,
    }),
    {
      manual: true,
      onSuccess: (result) => {
        if (result?.status === 'ok') {
          message.success('Successfully added to favourite!');
          return;
        }
        message.error('Cannot add to favourite!');
      },
    },
  );
  const [responsive, setResponsive] = useState(false);

  if (!loading && !data) {
    return <Exception404Page />;
  }

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

  const addToFav = () => {
    if (!access.isLoggedin) {
      message.warn('Need login to add to favourite!');
      return;
    }
    runAddToFav({ userId: initialState?.currentUser?.id, recipeId: data?.recipeId });
  };

  return (
    <PageContainer
      title={`Recipe: ${data?.recipeTitle || ''}`}
      extra={
        data
          ? [
              access.isLoggedin && (
                <Button
                  shape="round"
                  icon={<HeartOutlined />}
                  style={{ marginRight: 10 }}
                  key="dasdase3qe"
                  onClick={addToFav}
                >
                  Add to favourite
                </Button>
              ),
              <span onClick={like} style={didLike ? undefined : { cursor: 'pointer' }} key="3x321d">
                {createElement(didLike ? LikeFilled : LikeOutlined)}
                <span style={{ paddingLeft: 8 }}>{data?.recipeLike}</span>
              </span>,
            ]
          : null
      }
    >
      {loading ? (
        <CenteredSpinner />
      ) : (
        <Space size="large" direction="vertical" className={styles['page-card']}>
          <RcResizeObserver
            key="resize-observer"
            onResize={(offset) => {
              setResponsive(offset.width < 596);
            }}
          >
            <ProCard split={responsive ? 'horizontal' : 'vertical'} layout="center">
              <ProCard colSpan="30%">
                {data ? (
                  <img
                    alt={`${data?.recipeTitle} Picture`}
                    src={data?.recipeUrl}
                    className={styles['recipe-img']}
                  />
                ) : (
                  <CenteredSpinner />
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
          </RcResizeObserver>
          <ProCard title="Directions" className={styles['desc']}>
            {data?.recipeDirections.map((dir: any, index: number) => (
              <div key={`ing-idx-${index}`}>{`Step ${
                index + 1
              }:${'\u00A0'}${'\u00A0'}${'\u00A0'}${dir}`}</div>
            ))}
          </ProCard>
          <ProCard title="Comment">
            {access.isLoggedin && (
              <Comment
                avatar={
                  <Avatar
                    src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                    alt="Han Solo"
                  />
                }
                content={<Editor onRefresh={refresh} />}
              />
            )}
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
      )}
    </PageContainer>
  );
}
