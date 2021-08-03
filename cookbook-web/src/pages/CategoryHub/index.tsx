import { PageContainer } from '@ant-design/pro-layout';
import { useLocation } from 'umi';

export default function CategoryHub() {
  const { pathname } = useLocation();
  const categoryName = pathname.replace(/\//g, '');

  return <PageContainer>{categoryName}</PageContainer>;
}
