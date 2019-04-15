# 执行性能测试
## 启动性能测试

cmd.exe
> locust -f locustfile.py --host=https://www.baidu.com 
[2017-01-01 19:55:43,741] fnngj-PC/INFO/locust.main: Starting web monitor at 
*:8089 
[2017-01-01 19:55:43,755] fnngj-PC/INFO/locust.main: Starting Locust 0.7.5 
 
-f：　指定性能测试脚本文件。
--host：　指定被测试应用的URL地址，注意访问百度使用的HTTPS协议。
通过浏览器访问：http://127.0.0.1:8089（Locust启动网络监控器，默认为端口号为8089）。显示如图15.1所示。


## 创建新的测试集

- Number of users to simulate：　设置模拟用户数。
- Hatch rate（users spawned/second）：　每秒产生（启动）的虚拟用户数。
- 单击“Start swarming”按钮，开始运行性能测试，如图15.2所示。


## 性能测试参数如下。

- Type：　请求的类型，例如GET/POST。
- Name：　请求的路径。这里为百度首页，即https://www.baidu.com/。
- request：　当前请求的数量。
- fails：　当前请求失败的数量。
- Median：　中间值，单位毫秒，一半的服务器响应时间低于该值，而另一半高于该值。
- Average：　平均值，单位毫秒，所有请求的平均响应时间。
- Min：　请求的最小服务器响应时间，单位毫秒。
- Max：　请求的最大服务器响应时间，单位毫秒。
- Content Size：　单个请求的大小，单位字节。
- reqs/sec：　每秒钟请求的个数。
