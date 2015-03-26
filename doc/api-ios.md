 # API 说明文档

该文档主要是说明 XXX 新闻 APP 客户端后台 API 说明规范，包括数据调用接口 URL、数据调用方式、数据示例类型，帮助开发人员通过 API 获取数据，快速开发和部署。

```
请求 BASEURL: http://aero.wisdomriver.com.cn/
请求发送数据头部: Content-Type="application/json;odata=verbose"

```

## 1. 用户API


### 1.0 用户注册

* url: news/register

```
Request
Post:

{
  "account":"test00",
  "password":"1234",
  "name":"test99",
  "company":"fdfa",
  "phone_number" : "12312421312",
  "email":"fdsfa",
  "title":"副总"
}
```

```
Response:
同1.1

```


### 1.1 用户登录

* url : news/login

```
Request
Post: {"account":"xxx", "password":"fdsfa"}
```

```
Response:
{
    "account": "system",
    "company": null,
    "department": null,
    "description": "fdsafsadfa",
    "email": "327272993@qq.com",
    "header_large": "file:///Users/globit/git/news_api/app/extensions/userimages/user-header/1/0/1.480x108.jpe?_ts=20150318013815000000",
    "header_small": "file:///Users/globit/git/news_api/app/extensions/userimages/user-header/1/0/1.150x33.jpe?_ts=20150318013815000000",
    "id": 1,
    "is_active": true,
    "is_vip": false,
    "lastlogin_time": "2014-12-01",
    "myattr": "fsdfsa",
    "name": "bcd",
    "nickname": "abc",
    "password": "",
    "phone_number": "1231241241",
    "registered_time": "2014-12-01",
    "role": "admin",
    "title": null,
    "token": "b6b22322c3be6bd06b8bd2911567bc1b:1419465662",
    "work_phone": null,
    "zone": null
}
```

### 1.2 修改姓名和昵称

* url : news/user/<int:id>/update_name

```
Request
Post: {"name":"xxx", "nickname":"xxx","token":"fdsafsa"}
```


```
Response:
同1.1
```

### 1.3 上传图像
* url: news/user/upload_icon
* method :post

这里要去掉 content-type
```
Request:
   "file" : 图片  //这里post要按照提交文件的方式提交
```

```
Response:
 {"filename":"fsdfsdaf.jpg"}
```
用于填充update_header中的header字段


### 1.4 修改用户头像
* url: news/user/update_header
* method: post

```
Request:
   {"header":"fsdafsadfsa.jpg"}
   //注明： header是调用 uoload_icon接口返回的图片名字
```

```
Response:
同1.1
```

### 1.5 修改姓名和昵称和头像

* url : news/user/<int:id>/update_profile
* method :post

```
Request
Post: {"name":"xxx", "nickname":"xxx","token":"fdsafsa","header":"fsdafsadfsa.jpg"}
```


```
Response:
同1.1
```

### 1.6 修改用户基本信息

* url: news/user/<int:id>/update_user_profile
* method: post

```
Request
Post: 
{
  "name":"xxx", 
  "title":"xxx",
  "token":"fdsafsa",
  "company":"fsdafsadfsa.jpg"
  "phone_number":"fsdafsadfsa.jpg"
  "email":"fsdafsadfsa.jpg"
}
```

```
Response:
同1.1

```



## 2. 广告 API 和获取文件

### 2.1 获取广告图片

* url: news/mockimage
* method:get

### 2.2 获取主页滚动的广告图片列表
* url: news/mainpage_images
* method: get

### 2.3 获取视频流文件
* url: /news/send_file/<string:filename>  //视频url最后的那个文件名 如 xxx.mp4
* method: get




## 3. 留言 API

### 3.1 获取所有留言

url: news/messages
method: get

```
Response:
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
* url: news/message/send
* method: post

```
Request:
	{"token":"xxx",content:"fdsfa"}

```
```
Response:
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

### 4.1 获取主题列表 (弃用)

url: news/topics
method: get

```
Response:
[{"images": "file:///Users/globit/git/news_api/app/extensions/userimages/topic-image-store/1/0/1.100x66.jpe?_ts=20141209000645000000", "id": 1, "title": "test topic"}]
```

### 4.2 获取一个主题的内容（弃用）
* url: news/topic/<int:id>
* method: get

```
Response:
{ "id": 1, "images": [ { "id": 1, "image_path": "file:///Users/globit/git/news_api/app/extensions/userimages/topic-image-store/1/0/1.690x460.jpe?_ts=20141209000421000000" } ], "newses": [], "title": "test topic" }

```

### 4.3 获取一个新闻的内容

* url: news/news/<int:id>
* method: get

```
Response:
{
    "awesome_count": 0,
    "view_count": 0,
    "update_time": "2015-03-18T23:27:08",
    "author": "管理员",
    "title": "中航工业成飞圆满完成2014年全年任务",
    "has_video": false,
    "content": "n",
    "create_time": "2015-01-15T09:59:55",
    "video_link": null,
    "news_language": "en",
    "is_draft": false,
    "id": 33,
    "icon": "file:///Users/globit/git/news_api/app/extensions/userimages/news-image/33/0/33.639x363.jpe?_ts=20150315201115000000"
}
```

### 4.4 获取新闻列表

url: news/simple_news
method: get

```
Response:
[
    {
        "awesome_count": 3,
        "view_count": 5,
        "author": "管理员",
        "title": "Assembly of China's First Large Aircraft C919 Almost Complete",
        "has_video": false,
        "create_time": "2015-01-14T15:08:09",
        "video_link": null,
        "news_language": "zhen",
        "id": 25,
        "icon": "file:///Users/globit/git/news_api/app/extensions/userimages/news-image/25/0/25.100x59.jpe?_ts=20150315201257000000"
    },
    {
        "awesome_count": 0,
        "view_count": 0,
        "author": "管理员",
        "title": "中航工业成飞圆满完成2014年全年任务",
        "has_video": false,
        "create_time": "2015-01-15T09:59:55",
        "video_link": null,
        "news_language": "en",
        "id": 33,
        "icon": "file:///Users/globit/git/news_api/app/extensions/userimages/news-image/33/0/33.100x56.jpe?_ts=20150315201257000000"
    }
    ...
 ]
```

### 4.5 点赞

* url: news/news/<int:id>/awesome
* method:get

```
{
	"awesome_count":1,
	"id":1
}
```



## 5. 会展 API


### 5.0 获取会展 key value 列表

列出所有 active 的会展

* url :/news/conferences/list/ios
* method:get

```
[
    {
        "view_count": 111,
        "is_show_android": true,
        "started_time": "2015-04-21T00:00:00",
        "title": "CAIF2015民用飞机航电国际论坛",
        "updated_time": "2015-03-18T17:14:34",
        "is_show_ios": true,
        "created_time": "2014-12-10T00:00:00",
        "is_draft": false,
        "id": 1
    },
    {
        "view_count": 0,
        "is_show_android": true,
        "started_time": "2015-03-04T06:00:00",
        "title": "fsadf",
        "updated_time": "2015-03-18T22:47:11",
        "is_show_ios": true,
        "created_time": "2015-03-18T22:47:11",
        "is_draft": false,
        "id": 2
    }
]

```


### 5.1 获取会展介绍

这里的会展介绍包含了介绍、交通住宿、组委会、会场布局、会议日程。都是以 HTML 的形式返回到前端，和夏老板讨论了觉得这样更加科学。

* url: news/conferences/content  |  news/conferences/simple_content   
* method: get

```
Response:
//请查看返回的列表
```


### 5.2 根据 id 获取会展介绍

* url: news/conferences/<int:id> 
* method: get

```
Response:
//请查看返回的列表
```


### 5.3 获取会议报告和会议PDF列表

会议报告和会议PDF都是列表，这里返回列表项目的值和列表内容 PDF 的下载链接。

* url: news/conferences/<int:id>/get_file/<string:ftype>  
	* id: Integer 会展 ID
	* ftype: REPORT|PDF
* method: get

```
Response:
//查看返回的列表
```

## 6 通用 api

### 6.1 获取3个系统通知
* url: /news/informs
* method:get

```
[
    {
        "create_time": "2015-01-12T17:52:13",
        "id": 10,
        "title": "场馆信息已经更新，您可在“会展”版块进行查询。Venue info has been updated, and you can check it in \"Conference\" section."
    },
    {
        "create_time": "2015-01-08T23:51:40",
        "id": 9,
        "title": "Shanghai VisionMC will join the forum with LDRA in UK and AbsInt in Germany."
    },
    {
        "create_time": "2015-01-08T23:51:15",
        "id": 8,
        "title": "上周服务器维护更新，现已恢复正常。The server has been  maintained and updated last week, while it gets back to normal now."
    }
]
```


### 6.2 获取系统时间
* url :/news/system_time
* method:get

```
{
    "system_time": "2015-03-20T11:41:54.394987"
}

```