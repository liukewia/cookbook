import React from 'react';
import { List } from 'antd';
import { Button, Input, Upload, message } from 'antd';
import ProForm, {
  ProFormDependency,
  ProFormFieldSet,
  ProFormSelect,
  ProFormText,
  ProFormTextArea,
} from '@ant-design/pro-form';

import styles from './BaseView.less';

const SecurityView: React.FC = () => {
  const handleFinish = async () => {
    message.success('Password Updated.');
  };

  return (
    <div className={styles.baseView}>
      <>
        <div className={styles.left}>
          <ProForm
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
              name="currentPassword"
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
