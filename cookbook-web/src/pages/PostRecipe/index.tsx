import { PageContainer } from '@ant-design/pro-layout';
import { Form, Input, Button, Card, message, Select } from 'antd';
import { useRequest } from 'umi';

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 8 },
};
const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};
const { Option } = Select;

export default function AddCategory() {
  const [form] = Form.useForm();
  const { data } = useRequest('/api/get_all_categories/');
  const { run } = useRequest(
    (values) => ({
      url: 'api/add_category/',
      method: 'post',
      data: values,
    }),
    {
      manual: true,
      onSuccess: (result) => {
        if (result?.status === 'ok') {
          message.success('Successfully posted.');
        }
      },
    },
  );
  console.log('data: ', data);

  const onFinish = (values: any) => {
    run(values);
  };

  return (
    <PageContainer title="Post Recipe">
      <Card>
        <Form {...layout} form={form} name="add-category" onFinish={onFinish}>
          <Form.Item name="category" label="Category" rules={[{ required: true }]}>
            <Select allowClear 
            placeholder='Select one'>
              {data?.categories?.map((category) => (
                <Option key={category.categorySlug} value={category.categorySlug}>
                  {category.categoryName}
                </Option>
              ))}
            </Select>
          </Form.Item>
          <Form.Item name="recipeName" label="Recipe Name" rules={[{ required: true }]}>
            <Input />
          </Form.Item>
          <Form.Item {...tailLayout}>
            <Button type="primary" htmlType="submit">
              Submit
            </Button>
          </Form.Item>
        </Form>
      </Card>
    </PageContainer>
  );
}
