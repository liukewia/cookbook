import { MailOutlined, HomeOutlined, ContactsOutlined, ClusterOutlined, IdcardOutlined, CrownOutlined } from '@ant-design/icons';
import { Avatar, Card, Col, Divider, Input, Row, Tag } from 'antd';
import React, { useState, useRef } from 'react';
import { GridContent } from '@ant-design/pro-layout';
import { Link, useRequest } from 'umi';
import type { RouteChildrenProps } from 'react-router';
import Favourites from './components/Favourites';
import Articles from './components/Articles';
import Applications from './components/Applications';
import type { CurrentUser, TagType, tabKeyType } from './data.d';
import styles from './Center.less';
import { queryCurrentUser } from '@/services/ant-design-pro/api';

const operationTabList = [
  {
    key: 'posts',
    tab: <span>Posts</span>,
  },
  {
    key: 'favourites',
    tab: <span>Favourites</span>,
  },
  // {
  //   key: 'favourites',
  //   tab: (
  //     <span>
  //       项目 <span style={{ fontSize: 14 }}>(8)</span>
  //     </span>
  //   ),
  // },
];

// const TagList: React.FC<{ tags: CurrentUser['tags'] }> = ({ tags }) => {
//   const ref = useRef<Input | null>(null);
//   const [newTags, setNewTags] = useState<TagType[]>([]);
//   const [inputVisible, setInputVisible] = useState<boolean>(false);
//   const [inputValue, setInputValue] = useState<string>('');

//   const showInput = () => {
//     setInputVisible(true);
//     if (ref.current) {
//       // eslint-disable-next-line no-unused-expressions
//       ref.current?.focus();
//     }
//   };

//   const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
//     setInputValue(e.target.value);
//   };

//   const handleInputConfirm = () => {
//     let tempsTags = [...newTags];
//     if (inputValue && tempsTags.filter((tag) => tag.label === inputValue).length === 0) {
//       tempsTags = [...tempsTags, { key: `new-${tempsTags.length}`, label: inputValue }];
//     }
//     setNewTags(tempsTags);
//     setInputVisible(false);
//     setInputValue('');
//   };

//   return (
//     <div className={styles.tags}>
//       <div className={styles.tagsTitle}>标签</div>
//       {(tags || []).concat(newTags).map((item) => (
//         <Tag key={item.key}>{item.label}</Tag>
//       ))}
//       {inputVisible && (
//         <Input
//           ref={ref}
//           type="text"
//           size="small"
//           style={{ width: 78 }}
//           value={inputValue}
//           onChange={handleInputChange}
//           onBlur={handleInputConfirm}
//           onPressEnter={handleInputConfirm}
//         />
//       )}
//       {!inputVisible && (
//         <Tag onClick={showInput} style={{ borderStyle: 'dashed' }}>
//           <PlusOutlined />
//         </Tag>
//       )}
//     </div>
//   );
// };

const Center: React.FC<RouteChildrenProps> = () => {
  const [tabKey, setTabKey] = useState<tabKeyType>('posts');

  const { data: currentUser, loading } = useRequest(queryCurrentUser);
  const renderUserInfo = ({}: Partial<CurrentUser>) => {
    return (
      <div className={styles.detail}>
        <p>
          <IdcardOutlined
            style={{
              marginRight: 8,
            }}
          />
          {currentUser?.userName}
        </p>
        <p>
          <MailOutlined
            style={{
              marginRight: 8,
            }}
          />
          {currentUser?.email}
        </p>
        <p>
          <CrownOutlined
            style={{
              marginRight: 8,
            }}
          />
          {currentUser?.access}
        </p>
        {/* <p>
          <ClusterOutlined
            style={{
              marginRight: 8,
            }}
          />
          {group}
        </p>
        <p>
          <HomeOutlined
            style={{
              marginRight: 8,
            }}
          />
          {(geographic || { province: { label: '' } }).province.label}
          {
            (
              geographic || {
                city: {
                  label: '',
                },
              }
            ).city.label
          }
        </p> */}
      </div>
    );
  };

  // 渲染tab切换
  const renderChildrenByTabKey = (tabValue: tabKeyType) => {
    if (tabValue === 'posts') {
      return <Articles />;
    }
    if (tabValue === 'favourites') {
      return <Favourites />;
    }
    // if (tabValue === 'applications') {
    //   return <Applications />;
    // }
    return null;
  };

  return (
    <GridContent>
      <Row gutter={24}>
        <Col lg={7} md={24}>
          <Card bordered={false} style={{ marginBottom: 24 }} loading={loading}>
            {!loading && currentUser && (
              <div>
                <div className={styles.avatarHolder}>
                  <img
                    alt=""
                    src="https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png"
                  />
                  <div className={styles.name}>
                    {currentUser.firstName + ' ' + currentUser.lastName}
                  </div>
                  {/* <div>{currentUser?.signature}</div> */}
                </div>
                <Divider dashed />
                {renderUserInfo(currentUser)}
                {/* 
                <TagList tags={currentUser.tags || []} />
                <Divider style={{ marginTop: 16 }} dashed />
                <div className={styles.team}>
                  <div className={styles.teamTitle}>团队</div>
                  <Row gutter={36}>
                    {currentUser.notice &&
                      currentUser.notice.map((item) => (
                        <Col key={item.id} lg={24} xl={12}>
                          <Link to={item.href}>
                            <Avatar size="small" src={item.logo} />
                            {item.member}
                          </Link>
                        </Col>
                      ))}
                  </Row>
                </div> */}
              </div>
            )}
          </Card>
        </Col>
        <Col lg={17} md={24}>
          <Card
            className={styles.tabsCard}
            bordered={false}
            tabList={operationTabList}
            activeTabKey={tabKey}
            onTabChange={(_tabKey: string) => {
              setTabKey(_tabKey as tabKeyType);
            }}
          >
            {renderChildrenByTabKey(tabKey)}
          </Card>
        </Col>
      </Row>
    </GridContent>
  );
};
export default Center;
