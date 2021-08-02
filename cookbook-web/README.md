## Local development

### 1. install Node LTS (14.x.x)

### 2. update npm version to latest

```shell
npm install -g npm
```

### 3. install yarn

```shell
npm install --global yarn
```

### 4. install dependencies

```shell
cd cookbook-web
yarn
```

If the connection is slow, set yarn's registry as `"https://registry.npm.taobao.org"`.

```shell
yarn config set registry https://registry.npm.taobao.org/
```

### 5. run app locally

```shell
yarn start
```
