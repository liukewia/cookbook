import { PageContainer } from '@ant-design/pro-layout';
import { Form, Input, Button, Card, message } from 'antd';
import { useRequest } from 'umi';

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 8 },
};
const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

export default function AddCategory() {
  const [form] = Form.useForm();
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
          message.success('Successfully added');
        }
      },
    },
  );

  const onFinish = (values: any) => {
    run(values);
  };

  return (
    <PageContainer title="Add Category">
      <Card>
        <Form {...layout} form={form} name="add-category" onFinish={onFinish}>
          <Form.Item name="name" label="Category Name" rules={[{ required: true }]}>
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
