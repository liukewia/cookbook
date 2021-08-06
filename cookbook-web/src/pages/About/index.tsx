import React from 'react';
import { PageContainer } from '@ant-design/pro-layout';
import { Card, Typography } from 'antd';

const { Title, Paragraph, Text } = Typography;

export default (): React.ReactNode => {
  return (
    <PageContainer title="About">
      <Card>
        <Title level={2}>Hi! Meet Team Yellow Duck</Title>
        <Paragraph>
          Hi! We're Team Yellow Duck. Kick back, stay a while, won't you? When you visit our corner of the internet, we want you to feel comfortable. Like <Text italic>did we just become best friends?!</Text> kind of comfortable. We're not here to shame you into making beef bourguignon when all you really want is Fireball meatballs. And if you do attempt that fancy-shmancy dish and fail spectacularly, we're not going to <Text italic>tsk-tsk</Text> you—because we've had plenty of <Text italic>OH, S#!T</Text> moments, too.
        </Paragraph>
        <Paragraph>
          That's not to say we're not serious about food. If you've come here to finally tackle an exasperatingly intense sourdough recipe, we can help explain the technique, step by step. We celebrate anyone who really loves to eat as much as those who actually get in the kitchen to cook. So wherever you fall on that spectrum, you'll find your people here.
        </Paragraph>
        <Paragraph>
          That's why we want you to get to know us, too—the team behind Yellow Duck. We want you to love reading on and cooking from Delish as much as we love creating this space for you, so holler if you've got something you want us to know. We're all ears. (Did you know you can rate and comment on all our recipes, too?)
        </Paragraph>
      </Card>
    </PageContainer>
  );
};
