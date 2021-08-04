import { Typography, Space } from 'antd';
import classNames from 'classnames';
import styles from './index.less';

const { Text, Link } = Typography;

interface ILoadingFailureTipProp {
  description?: string;
  onRetry?: (args: unknown) => void;
  centered?: boolean;
}

const LoadingFailureTip = (props: ILoadingFailureTipProp) => (
  <Space className={classNames({ [styles.centered]: props.centered })}>
    <Text type="secondary">{props.description || 'Failed to load data'}</Text>
    {props.onRetry ? <Link onClick={props.onRetry}>Retry</Link> : null}
  </Space>
);

export default LoadingFailureTip;
