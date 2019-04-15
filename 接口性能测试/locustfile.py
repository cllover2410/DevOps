from locust import HttpLocust, TaskSet, task 
 
#定义用户行为 
class UserBehavior(TaskSet): 
 
    @task 
    def baidu_page(self): 
        self.client.get("/") 
 
 
class WebsiteUser(HttpLocust): 
    task_set = UserBehavior 
    min_wait = 3000 
    max_wait = 6000  




'''
UserBehavior类继承TaskSet类，用于描述用户行为。

baidu_page()方法表示一个用户行为，访问百度首页。使用@task装饰该方法为一个事务。client.get()用于指定请求的路径“/”，因为是百度首页，所以指定为根路径。

WebsiteUser类用于设置性能测试。

task_set：　指向一个定义的用户行为类。
min_wait：　执行事务之间用户等待时间的下界（单位：毫秒）。
max_wait：　执行事务之间用户等待时间的上界（单位：毫秒）。



2．执行性能测试
首先，启动性能测试。

cmd.exe
> locust -f locustfile.py --host=https://www.baidu.com 
[2017-01-01 19:55:43,741] fnngj-PC/INFO/locust.main: Starting web monitor at 
*:8089 
[2017-01-01 19:55:43,755] fnngj-PC/INFO/locust.main: Starting Locust 0.7.5 
 
-f：　指定性能测试脚本文件。
--host：　指定被测试应用的URL地址，注意访问百度使用的HTTPS协议。
通过浏览器访问：http://127.0.0.1:8089（Locust启动网络监控器，默认为端口号为8089）。显示如图15.1所示。


图15.1　创建新的测试集

Number of users to simulate：　设置模拟用户数。
Hatch rate（users spawned/second）：　每秒产生（启动）的虚拟用户数。
单击“Start swarming”按钮，开始运行性能测试，如图15.2所示。


图15.2　性能测试执行情况

性能测试参数如下。

Type：　请求的类型，例如GET/POST。
Name：　请求的路径。这里为百度首页，即https://www.baidu.com/。
request：　当前请求的数量。
fails：　当前请求失败的数量。
Median：　中间值，单位毫秒，一半的服务器响应时间低于该值，而另一半高于该值。
Average：　平均值，单位毫秒，所有请求的平均响应时间。
Min：　请求的最小服务器响应时间，单位毫秒。
Max：　请求的最大服务器响应时间，单位毫秒。
Content Size：　单个请求的大小，单位字节。
reqs/sec：　每秒钟请求的个数。
关于性能测试结果分析，由于是针对百度首页的性能测试，性能需求不明，服务器配置未知，网络环境复杂，因此没有分析的必要。
'''