import React from 'react';
import { Button, Form, message } from 'antd';
import ProForm, { ProFormText } from '@ant-design/pro-form';
import { useRequest } from 'umi';
import styles from './BaseView.less';
import { history, useModel } from 'umi';
import { stringify } from 'querystring';
import { loginOut } from '@/components/RightContent/AvatarDropdown';

const SecurityView: React.FC = () => {
  const [form] = Form.useForm();
  const { getFieldValue, resetFields } = form;
  const { initialState, setInitialState } = useModel('@@initialState');

  const { run } = useRequest(
    (values) => ({
      url: '/api/user/update_password/',
      method: 'post',
      data: values,
    }),
    {
      manual: true,
      onSuccess: (result) => {
        if (result?.status === 'ok') {
          message.success('Password Updated.');
          message.info('Please log in again.');
          const { query = {}, pathname } = history.location;
          const { redirect } = query;
          if (window.location.pathname !== '/user/login' && !redirect) {
            history.replace({
              pathname: '/user/login',
              search: stringify({
                redirect: pathname,
              }),
            });
          }
        } else if (result?.status === 'error') {
          message.error('Cannot update.');
        }
      },
    },
  );

  const handleFinish = async (values) => {
    run(values);
  };

  return (
    <div className={styles.baseView}>
      <>
        <div className={styles.left}>
          <ProForm
            form={form}
            layout="vertical"
            onFinish={handleFinish}
            submitter={{
              render: (props, doms) => {
                return [
                  // <Button key="reset" onClick={() => props.form?.resetFields()}>
                  //   reset
                  // </Button>,
                  <Button type="primary" key="submit" onClick={() => props.form?.submit?.()}>
                    Update
                  </Button>,
                ];
              },
            }}
            // initialValues={currentUser}
            hideRequiredMark
          >
            <ProFormText
              width="md"
              name="oldPassword"
              label="Current Password"
              placeholder=""
              rules={[
                {
                  required: true,
                  message: 'Please enter your current password!',
                },
              ]}
            />
            <ProFormText
              width="md"
              name="newPassword"
              label="New Password"
              placeholder=""
              rules={[
                {
                  required: true,
                  message: 'Please enter your new password!',
                },
              ]}
            />
          </ProForm>
        </div>
      </>
    </div>
  );
};

export default SecurityView;
