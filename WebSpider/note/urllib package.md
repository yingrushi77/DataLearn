## urllib package

URL handling modules

![image-20201127123645331](https://gitee.com/smithbee/image_bed/raw/master/image-20201127123645331.png)

[urllib功能简介]([urllib — URL handling modules — Python 3.9.0 documentation](https://docs.python.org/3/library/urllib.html))

urllib 是 Python 标准库中用于网络请求的库。该库有四个模块，分别是`urllib.request`，`urllib.error`，`urllib.parse`，`urllib.robotparser`。其中`urllib.request`，`urllib.error`两个库在爬虫程序中应用比较频繁。那我们就开门见山，直接讲解这两个模块的用法。

### 1  发起请求

模拟浏览器发起一个 HTTP 请求，我们需要用到 urllib.request 模块。urllib.request 的作用不仅仅是发起请求， 还能获取请求返回结果。发起请求，单靠 `urlopen()` 方法就可以叱咤风云。我们先看下 urlopen() 的 API

- urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
  - 第一个参数 String 类型的地址或者
  - `data` 是 bytes 类型的内容，可通过 bytes()函数转为化字节流。它也是可选参数。使用 data 参数，请求方式变成以 POST 方式提交表单。使用标准格式是`application/x-www-form-urlencoded`
  - `timeout` 参数是用于设置请求超时时间。单位是秒。
  - `cafile`和`capath`代表 CA 证书和 CA 证书的路径。如果使用`HTTPS`则需要用到。
  - `context`参数必须是`ssl.SSLContext`类型，用来指定`SSL`设置
  - `cadefault`参数已经被弃用，可以不用管了。
  - 该方法也可以单独传入`urllib.request.Request`对象
  - 该函数返回结果是一个`http.client.HTTPResponse`对象。

#### 1.1 简单抓取网页

我们使用 urllib.request.urlopen() 去请求百度贴吧，并获取到它页面的源代码。

```python
import urllib.request

url = "http://tieba.baidu.com"
response = urllib.request.urlopen(url)
html = response.read()         # 获取到页面的源代码
print(html.decode('utf-8'))    # 转化为 utf-8 编码
```

#### 1.2 设置请求超时

有些请求可能因为网络原因无法得到响应。因此，我们可以手动设置超时时间。当请求超时，我们可以采取进一步措施，例如选择直接丢弃该请求或者再请求一次。



```python
import urllib.request

url = "http://tieba.baidu.com"
response = urllib.request.urlopen(url, timeout=1)
print(response.read().decode('utf-8'))
```

#### 1.3 使用 data 参数提交数据

在请求某些网页时需要携带一些数据，我们就需要使用到 data 参数。



```python
import urllib.parse
import urllib.request

url = "http://127.0.0.1:8000/book"
params = {
  'name':'浮生六记',
  'author':'沈复'
}

data = bytes(urllib.parse.urlencode(params), encoding='utf8')
response = urllib.request.urlopen(url, data=data)
print(response.read().decode('utf-8'))
```

params 需要被转码成字节流。而 params 是一个字典。我们需要使用 urllib.parse.urlencode() 将字典转化为字符串。再使用 bytes() 转为字节流。最后使用 urlopen() 发起请求，请求是模拟用 POST 方式提交表单数据。

#### 1.4 使用 Request

由上我们知道利用 urlopen() 方法可以发起简单的请求。但这几个简单的参数并不足以构建一个完整的请求，如果请求中需要加入headers（请求头）、指定请求方式等信息，我们就可以利用更强大的Request类来构建一个请求。
 按照国际惯例，先看下 Request 的构造方法：



```python
urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
```

- `url 参数`是请求链接，这个是必传参数，其他的都是可选参数。
- `data 参数`跟 urlopen() 中的 data 参数用法相同。
- `headers 参数`是指定发起的 HTTP 请求的头部信息。headers 是一个字典。它除了在 Request 中添加，还可以通过调用 Reques t实例的 add_header() 方法来添加请求头。
- `origin_req_host 参数`指的是请求方的 host 名称或者 IP 地址。
- `unverifiable 参数`表示这个请求是否是无法验证的，默认值是False。意思就是说用户没有足够权限来选择接收这个请求的结果。例如我们请求一个HTML文档中的图片，但是我们没有自动抓取图像的权限，我们就要将 unverifiable 的值设置成 True。
- `method 参数`指的是发起的 HTTP 请求的方式，有 GET、POST、DELETE、PUT等

##### 1.4.1 简单使用 Request

使用 Request 伪装成浏览器发起 HTTP 请求。如果不设置 headers 中的 User-Agent，默认的`User-Agent`是`Python-urllib/3.5`。可能一些网站会将该请求拦截，所以需要伪装成浏览器发起请求。我使用的 User-Agent 是 Chrome 浏览器。



```python
import urllib.request

url = "http://tieba.baidu.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
```

#### 1.4.2 Request 高级用法

如果我们需要在请求中添加代理、处理请求的 Cookies，我们需要用到`Handler`和`OpenerDirector`。

1） `Handler`
 Handler 的中文意思是处理者、处理器。 Handler 能处理请求（HTTP、HTTPS、FTP等）中的各种事情。它的具体实现是这个类 `urllib.request.BaseHandler`。它是所有的 Handler 的基类，其提供了最基本的Handler的方法，例如default_open()、protocol_request()等。
 继承 BaseHandler 有很多个，我就列举几个比较常见的类：

- `ProxyHandler`：为请求设置代理
- `HTTPCookieProcessor`：处理 HTTP 请求中的 Cookies
- `HTTPDefaultErrorHandler`：处理 HTTP 响应错误。
- `HTTPRedirectHandler`：处理 HTTP 重定向。
- `HTTPPasswordMgr`：用于管理密码，它维护了用户名密码的表。
- `HTTPBasicAuthHandler`：用于登录认证，一般和 `HTTPPasswordMgr` 结合使用。

2） `OpenerDirector`
 对于 OpenerDirector，我们可以称之为 Opener。我们之前用过 urlopen() 这个方法，实际上它就是 urllib 为我们提供的一个Opener。那 Opener 和 Handler 又有什么关系？opener 对象是由 build_opener(handler) 方法来创建出来 。我们需要创建自定义的 opener，就需要使用 `install_opener(opener)`方法。值得注意的是，install_opener 实例化会得到一个全局的 OpenerDirector 对象。

#### 1.5 使用代理

我们已经了解了 opener 和 handler，接下来我们就通过示例来深入学习。第一个例子是为 HTTP 请求设置代理
 有些网站做了浏览频率限制。如果我们请求该网站频率过高。该网站会被封 IP，禁止我们的访问。所以我们需要使用代理来突破这“枷锁”。



```python
import urllib.request

url = "http://tieba.baidu.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

proxy_handler = urllib.request.ProxyHandler({
    'http': 'web-proxy.oa.com:8080',
    'https': 'web-proxy.oa.com:8080'
})
opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(opener)

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
```

##### 1.6 认证登录

有些网站需要携带账号和密码进行登录之后才能继续浏览网页。碰到这样的网站，我们需要用到认证登录。我们首先需要使用 HTTPPasswordMgrWithDefaultRealm() 实例化一个账号密码管理对象；然后使用 add_password() 函数添加账号和密码；接着使用 HTTPBasicAuthHandler() 得到 hander；再使用 build_opener() 获取 opener 对象；最后使用 opener 的 open() 函数发起请求。

第二个例子是携带账号和密码请求登录百度贴吧，代码如下：



```python
import urllib.request

url = "http://tieba.baidu.com/"
user = 'user'
password = 'password'
pwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
pwdmgr.add_password(None，url ，user ，password)

auth_handler = urllib.request.HTTPBasicAuthHandler(pwdmgr)
opener = urllib.request.build_opener(auth_handler)
response = opener.open(url)
print(response.read().decode('utf-8'))
```

##### 1.7 Cookies设置

如果请求的页面每次需要身份验证，我们可以使用 Cookies 来自动登录，免去重复登录验证的操作。获取 Cookies 需要使用 http.cookiejar.CookieJar() 实例化一个 Cookies 对象。再用 urllib.request.HTTPCookieProcessor 构建出 handler 对象。最后使用 opener 的 open() 函数即可。

第三个例子是获取请求百度贴吧的 Cookies 并保存到文件中，代码如下：



```python
import http.cookiejar
import urllib.request

url = "http://tieba.baidu.com/"
fileName = 'cookie.txt'

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open(url)

f = open(fileName,'a')
for item in cookie:
    f.write(item.name+" = "+item.value+'\n')
f.close()
```

#### 1.8 HTTPResponse

从上面的例子可知， 使用 urllib.request.urlopen() 或者 opener.open(url) 返回结果是一个 http.client.HTTPResponse 对象。它具有 msg、version、status、reason、debuglevel、closed等属性以及read()、readinto()、getheader(name)、getheaders()、fileno()等函数。

### 2  错误解析

发起请求难免会出现各种异常，我们需要对异常进行处理，这样会使得程序比较人性化。
 异常处理主要用到两个类，`urllib.error.URLError`和`urllib.error.HTTPError`。

- `URLError`
   URLError 是 urllib.error 异常类的基类, 可以捕获由urllib.request 产生的异常。
   它具有一个属性`reason`，即返回错误的原因。

捕获 URL 异常的示例代码：



```python
import urllib.request
import urllib.error

url = "http://www.google.com"
try:
    response = request.urlopen(url)
except error.URLError as e:
    print(e.reason)
```

- `HTTPError HTTPError 是 UEKRrror 的子类，专门处理 HTTP 和 HTTPS 请求的错误。它具有三个属性。 1)`code`：HTTP 请求返回的状态码。 1)`renson`：与父类用法一样，表示返回错误的原因。 1)`headers`：HTTP 请求返回的响应头信息。

获取 HTTP 异常的示例代码, 输出了错误状态码、错误原因、服务器响应头



```python
import urllib.request
import urllib.error

url = "http://www.google.com"
try:
    response = request.urlopen(url)
except error.HTTPError as e:
   print('code: ' + e.code + '\n')
   print('reason: ' + e.reason + '\n')
   print('headers: ' + e.headers + '\n')
```



