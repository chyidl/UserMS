用户系统设计
==========

数据库模型设计
------------
``` 
superuser:
    username: admin
    password: root@123
```
   
Url路由和视图
------------
* 路由设计
``` 
    /index/ -- 主页
    /login/ -- 登陆 
    /register/ -- 注册 
    /logout/ -- 注销 
```

* CSRF防护
``` 
django为用户实现防止跨站请求伪造的功能，通过中间件 

Django中CSRF防护原理:
    在用户访问django可信站点时，django反馈给用户的表单中一个隐含字段csrftoken，这个值是在服务器端随机生成的，
    每一次提交表单都会生成不同的值
    
    1. 在返回的HTTP响应的cookie里，django会为你添加一个csrftoken字段，其值为一个自动生成的token 
    2. 在所有的POST表单时，必须包含一个csrfmiddlewaretoken字段 
    3. 
```
   
* Django 表单 
```
准备和重构数据用于页面渲染 
为数据创建HTML表单元素
接受和处理用户从表单发送过来的数据
```

* 图片验证码 
``` 
CAPTCHA: Completely Automated Public Turing test to tell COmputers and Humans Apart
全自动区分计算机和人类的图灵测试 
作为防御手段，至少可以抵挡一些低级入门的攻击手段，抬高攻击者的门槛

django-simple-captcha 是django验证码包 
    验证码生成原理: django-simple-captcha并没有使用session对验证码进行存储，而是使用数据库，首先生成一个表captcha_captchastore
    challenge: 验证码大写 
    response: 验证码小写 
    hashkey: hash值 
    expiration: 

隐藏字段hashkey的值，django将hashkey传给页面以hidden的形式存在，提交表单时hashkey于输入的验证码一起post到服务器，此时服务器验证
captcha_captchastore表中的hashkey对应的response是否于输入的验证码一致，如果一致则正确，不一致返回错误

django-simple-captcha ajax 动态验证:
    
```

* session会话
```
因为因特网HTTP协议的特性，每一次请求request都是无状态的、独立的。无法保存用户状态
为了实现连接状态的保持功能，网站会通过用户浏览器在用户机器上Cookie. 通过Cookie可以保存一些诸如用户名，浏览记录，表单记录，登陆和注销等数据 
这种Cookies不安全，因为Cookie保存在用户机器上，如果Cookie被伪造、篡改或删除，就会造成极大的安全威胁，因此，现代网站设计通常将Cookie用于
保存一些不重要的内容，实际的用户数据和状态还是以Session会话的方式保存在服务器端 

Session依赖Cookie, 但是于Cookie不同的地方在于Session将所有的数据都放在服务器端，用户浏览器的Cookie只会保存一个非明文的识别信息，哈希值

Django提供一个通用的Session框架，并且可以使用多种session数据的保存方式:
    保存在数据库内
    保存在缓存
    保存在文件内
    保存到cookie内
当session启动后，传递给视图request参数的httpRequest对象将包含一个session属性
```

* 密码加密
``` 

```

启动服务
-------
``` 
$ pip3 install django 
$ pip3 install mysqlclient 
$ pip3 install django-simple-captcha 
$ python3 manage.py runserver 0.0.0.0:8989 
```