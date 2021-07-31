import { Button, Result } from 'antd';
import React from 'react';
import { history } from 'umi';

const Exception403Page: React.FC = () => (
  <Result
    status="403"
    title="403"
    subTitle="Sorry, you don't have access to this page."
    extra={
      <Button type="primary" onClick={() => history.push('/')}>
        Back to Home
      </Button>
    }
  />
);

export default Exception403Page;
