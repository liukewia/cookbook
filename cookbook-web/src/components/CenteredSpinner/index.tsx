import React from 'react';
import { Spin } from 'antd';
import { SpinProps } from 'antd/lib/spin';

const CenteredSpinner = (props: SpinProps) => (
  <div style={{ padding: '50px 0px', textAlign: 'center' }}>
    <Spin size='large' {...props} />
  </div>
);

export default CenteredSpinner;
