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
'''

