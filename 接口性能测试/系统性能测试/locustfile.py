from locust import HttpLocust, TaskSet, task 


# Web性能测试 
class UserBehavior(TaskSet): 
 
    '''
        UserBehavior类继承TaskSet类，用于描述用户行为。
        baidu_page()方法表示一个用户行为，访问首页。
        使用@task装饰该方法为一个事务。
        client.get()用于指定请求的路径“/”，因为是首页，所以指定为根路径
    '''

    def on_start(self): 
        """ 
        on_start is called when a Locust start before any task is scheduled """ 
        self.login() 
 
    def login(self): 
        self.client.post(
            "/auth/login", {
                "username":"admin", "password":"admin123456"
                }) 
 

    @task(2) 
    def event_manage(self): 
        '''
            该方法表示一个用户行为，访问首页。
            使用@task装饰该方法为一个事务。
            client.get()用于指定请求的路径“/”，因为是首页，所以指定为根路径
        '''
        self.client.get("/event_manage/") 
    
    @task(2) 
    def guest_manage(self): 
        self.client.get("/guest_manage/") 
 
    @task(1) 
    def search_phone(self): 
        self.client.get("/search_phone/",params={"phone":'13800112541'}) 

 
class WebsiteUser(HttpLocust): 
    '''
        WebsiteUser类用于设置性能测试。
        task_set：　指向一个定义的用户行为类。
        min_wait：　执行事务之间用户等待时间的下界（单位：毫秒）。
        max_wait：　执行事务之间用户等待时间的上界（单位：毫秒）。
    '''
    task_set = UserBehavior 
    min_wait = 3000  # 3秒
    max_wait = 6000  # 6秒


# 启动命令 ：locust -f 脚本名 --host=https://www.baidu.com 



