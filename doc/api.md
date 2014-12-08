# API 说明文档

该文档主要是说明 XXX 新闻 APP 客户端后台 API 说明规范，包括数据调用接口 URL、数据调用方式、数据示例类型，帮助开发人员通过 API 获取数据，快速开发和部署。

```
请求 BASEURL: http://10.60.43.10:5000/
请求发送数据头部: Content-Type="application/json;odata=verbose"

```

## 1. 用户API

### 1.1 用户登录

* url : news/login

```
Request
Post: {"username":"xxx", "password":"fdsfa"}
```

```
Respone:
{
    "account": "system2",
  "password" : "1234",
    "description": "321312",
    "email": "3272272993@qq.com",
    "header_large": "file:///Users/globit/git/news_api/app/extensions/userimages/user-header/1/0/1.480x320.jpe?_ts=20141207013905000000",
    "is_active": true,
    "lastlogin_time": "2014-12-22",
    "myattr": "",
    "name": "Allen Globit2",
    "phone_number": "2128543587",
    "registered_time": "2014-12-01",
    "role": "admin",
    "small_large": "file:///Users/globit/git/news_api/app/extensions/userimages/user-header/1/0/1.150x100.jpe?_ts=20141207013905000000",
    "token": "1308632dad4990a22f8e1dd8a7414fdc:1418780345"
}
```

### 1.2 修改姓名和昵称

* url : news/user/<int:id>/update_name

```
Request
Post: {"name":"xxx", "nickname":"xxx","token":"fdsafsa"}
```

```
Respone:
{
    "account": "system2",
  "password" : "1234",
    "description": "321312",
    "email": "3272272993@qq.com",
    "header_large": "file:///Users/globit/git/news_api/app/extensions/userimages/user-header/1/0/1.480x320.jpe?_ts=20141207013905000000",
    "is_active": true,
    "lastlogin_time": "2014-12-22",
    "myattr": "",
    "name": "Allen Globit2",
    "phone_number": "2128543587",
    "registered_time": "2014-12-01",
    "role": "admin",
    "small_large": "file:///Users/globit/git/news_api/app/extensions/userimages/user-header/1/0/1.150x100.jpe?_ts=20141207013905000000",
    "token": "1308632dad4990a22f8e1dd8a7414fdc:1418780345"
}
```

## 2. 主程序广告 API

### 2.1 获取广告

url: news/mockimage
method:get


## 3. 留言 API

### 3.1 获取所有留言

url: news/messages
method: get

```
Respone:
[
    {
        "content": "fdsfasfasfas",
        "publisher": "user4025",
        "user": {
            "header_small": "file:///Users/globit/git/news_api/app/extensions/userimages/user-header/1/0/1.150x100.jpe?_ts=20141207063340000000",
            "id": 1,
            "name": "user4025"
        },
        "created_time": 1417999460,
        "is_active": true,
        "id": 2
    },
    {
        "content": "test message",
        "publisher": "testu",
        "user": {
            "header_small": "file:///Users/globit/git/news_api/app/extensions/userimages/user-header/1/0/1.150x100.jpe?_ts=20141207063340000000",
            "id": 1,
            "name": "user4025"
        },
        "created_time": 1417934020,
        "is_active": true,
        "id": 1
    }
]
```

### 3.2 提交留言
url: news/message/send
method: post

```
Request:
	{"token":"xxx",content:"fdsfa"}

```
```
Respone:
	{
  "content": "fdsfasfasfas",
  "created_time": 1417999460.0,
  "id": 2,
  "is_active": true,
  "publisher": "user4025",
  "user": {
    "header_small": "file:///Users/globit/git/news_api/app/extensions/userimages/user-header/1/0/1.150x100.jpe?_ts=20141207063340000000",
    "id": 1,
    "name": "user4025"
  }
}
```

## 4. 新闻 API


