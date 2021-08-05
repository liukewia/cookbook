import { PageContainer } from '@ant-design/pro-layout';
import { Form, Input, Button, Card, message, Select } from 'antd';
import TextArea from 'antd/lib/input/TextArea';
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
  const { getFieldValue, resetFields } = form;

  const { data } = useRequest('/api/get_all_categories/');
  const { run } = useRequest(
    (values) => ({
      url: '/api/add_recipe/',
      method: 'post',
      data: values,
    }),
    {
      manual: true,
      onSuccess: (result) => {
        if (result?.status === 'ok') {
          message.success('Successfully posted.');
          resetFields();
        }
      },
    },
  );

  const onFinish = (values: any) => {
    console.log('values: ', values);
    run({
      slug: getFieldValue('category'),
      id: 3, // TODO change id
      title: getFieldValue('recipeName'),
      ingredients: getFieldValue('ingredients'),
      directions: getFieldValue('directions'),
      url: getFieldValue('imageUrl'),
    });
    resetFields();
  };

  return (
    <PageContainer title="Post Recipe">
      <Card>
        <Form {...layout} form={form} name="add-category" onFinish={onFinish}>
          <Form.Item name="category" label="Category" rules={[{ required: true }]}>
            <Select allowClear placeholder="Select one">
              {data?.categories?.map((category: any) => (
                <Option key={category.categorySlug} value={category.categorySlug}>
                  {category.categoryName}
                </Option>
              ))}
            </Select>
          </Form.Item>
          <Form.Item name="recipeName" label="Recipe Name" rules={[{ required: true }]}>
            <Input />
          </Form.Item>
          <Form.Item name="imageUrl" label="Image URL" rules={[{ required: true }]}>
            <Input />
          </Form.Item>
          <Form.Item name="ingredients" label="Ingredients" rules={[{ required: true }]}>
            <TextArea rows={4} />
          </Form.Item>
          <Form.Item name="directions" label="Directions" rules={[{ required: true }]}>
            <TextArea rows={4} />
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
