
from locust import HttpLocust, TaskSet, task 
from random import randint 
 
# Web接口测试 
class UserBehavior(TaskSet): 
 
    @task() 
    def user_sign(self): 
        number = randint(1,3001) 
        phone = 13800110000 + number 
        str_phone = str(phone) 
        self.client.post("/api/user_sign/",data={"eid":"1", 
                                                 "phone":str_phone}) 
 
class WebsiteUser(HttpLocust): 
    task_set = UserBehavior 
    min_wait = 0 
    max_wait = 0 


# locust -f locustfile.py --host=http://192.168.127.134:8089  --no-web -c 10 -r 10 -n 3000

'''
--no-web：　表示不使用Web界面运行测试。
-c：　设置虚拟用户数。
-r：　设置每秒启动虚拟用户数。
-n：　设置请求个数。
'''