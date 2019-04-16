# views 视图
# 1. 视图概述
- 视图即视图函数,接收web请求并返回web响应的事物处理函数.
- 响应指符合http协议要求的任何内容,包括json,string, html等
- 本章忽略事务处理,重点在如何返回处理结果上
# 2 其他简单视图
- django.http给我们提供类很多和HttpResponse类似的简单视图,
通过查看django.http代码我们知道,
- 此类视图使用方法基本类似,可以通过return语句昨晚直接反馈返回给浏览器
- Http404为Exception子类,所以需要raise使用       

# 3. HttpResponse详解
- 方法
    - init ：使用页内容实例化HttpResponse对象
    - write(content)：以文件的方式写
    - flush()：以文件的方式输出缓存区
    - set_cookie(key, value='', max_age=None, expires=None)：设置Cookie
       -  key,value都是字符串类型
       -  max_age是一个整数，表示在指定秒数后过期
       -  expires是一个datetime或timedelta对象，会话将在这个指定的日期/时间过期，注意datetime和timedelta值只有在使用PickleSerializer时才可序列化
       -  max_age与expires二选一
       -  如果不指定过期时间，则两个星期后过期
    - delete_cookie(key)：删除指定的key的Cookie，如果key不存在则什么也不发生

# 4. HttpResponseRedirect
   - 重定向，服务器端跳转
   - 构造函数的第一个参数用来指定重定向的地址
   - 案例 ShowViews/views.py
        ```python
           # 在 east/urls中添加一下内容
           url(r'^v10_1/', views.v10_1),
           url(r'^v10_2/', views.v10_2),
           url(r'^v11/', views.v11, name="v11"), 
        ```
        ```python
        # /east/ShowViews/views中添加一下内容
        def v10_1(request):
            return HttpResponseRedirect("/v11")

        def v10_2(request):
            return HttpResponseRedirect(reverse("v11"))

        def v11(request):
            return HttpResponse("哈哈，这是v11的访问返回呀")

        ```

# 5.Request对象
- Request介绍
    - 服务器接收到http协议的请求后，会根据报文创建HttpRequest对象
    - 视图函数的第一个参数是HttpRequest对象
    - 在django.http模块中定义了HttpRequest对象的API
- 属性
    - 下面除非特别说明，属性都是只读的
    - path：一个字符串，表示请求的页面的完整路径，不包含域名
    - method：一个字符串，表示请求使用的HTTP方法，常用值包括：'GET'、'POST'
    - encoding：一个字符串，表示提交的数据的编码方式
        - 如果为None则表示使用浏览器的默认设置，一般为utf-8
        - 这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值
    - GET：一个类似于字典的对象，包含get请求方式的所有参数
    - POST：一个类似于字典的对象，包含post请求方式的所有参数
    - FILES：一个类似于字典的对象，包含所有的上传文件
    - COOKIES：一个标准的Python字典，包含所有的cookie，键和值都为字符串
    - session：一个既可读又可写的类似于字典的对象，表示当前的会话
        - 只有当Django 启用会话的支持时才可用，
        - 详细内容见“状态保持”
- 方法
    - is_ajax()：如果请求是通过XMLHttpRequest发起的，则返回True
    
- QueryDict对象
    - 定义在django.http.QueryDict
    - request对象的属性GET、POST都是QueryDict类型的对象
    - 与python字典不同，QueryDict类型的对象用来处理同一个键带有多个值的情况
    - 方法get()：根据键获取值
        - 只能获取键的一个值
        - 如果一个键同时拥有多个值，获取最后一个值
    - 方法getlist()：根据键获取值
        - 将键的值以列表返回，可以获取一个键的多个值
- GET属性
    - QueryDict类型的对象
    - 包含get请求方式的所有参数
    - 与url请求地址中的参数对应，位于?后面
    - 参数的格式是键值对，如key1=value1
    - 多个参数之间，使用&连接，如key1=value1&key2=value2
    - 键是开发人员定下来的，值是可变的
    - 案例/views/v8_get

- POST属性
    - QueryDict类型的对象
    - 包含post请求方式的所有参数
    - 与form表单中的控件对应
    - 表单中空间必须有name属性，name为键，value为值
        - checkbox存在一键多值的问题
    - 键是开发人员定下来的，值是可变的
    - 案例/views/v9_post
        - settings中设置模板位置(已经设置完毕)
        - 设置get页面的urls和函数
        ```python
            # east/urls.py
            # 需要在路由文件中添加两个路由
            url(r'^v9_get/', views.v9_get),
            url(r'^v9_post/', views.v9_post),
        ```
        ```python

             # ShowViews/views.py
             # 在文件中添加下面两个处理函数
            def v9_get(request):
                return  render_to_response("for_post.html")

            def v9_post(request):
                rst = ""
                for k,v in request.POST.items():
                    rst += k + "-->" + v
                    rst += ","

                return HttpResponse("Get value of POST is {0} ".format(rst))
        ```
        - 添加文件/east/templates/for_post.html
        - 由于安全原因，需要在设置中安全选项中删除csrf设置
        ```python
          # settings.py
          

            MIDDLEWARE = [
                'django.middleware.security.SecurityMiddleware',
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.middleware.common.CommonMiddleware',
                  #  下面这句话被注释掉
                #'django.middleware.csrf.CsrfViewMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'django.contrib.messages.middleware.MessageMiddleware',
                'django.middleware.clickjacking.XFrameOptionsMiddleware',
            ]
        ```
- 手动编写视图    
    - 实验目的:
        - 利用django快捷函数手动编写视图处理函数
        - 编写过程中理解视图运行原理
    
    - 分析:
        - django把所有请求信息封装入request
        - django通过urls模块把相应请求跟事件处理函数链接起来,
                 并把request昨晚参数传入
        - 在相应的处理函数中,我们需要完成两部分
            - 处理业务
            - 把结果封装并返回,我们可以使用简单HttpResponse,同样也可以自己处理此功能,例如我们本例需要做的
        - 本案例不介绍业务处理,把目光集中在如何渲染结果并返回
        
    - render(request, template_name[, context][, context_instance][, content_type][, status][, current_app][, dirs][, using])
        - 使用模板和一个给定的上下文环境,返回一个渲染和的HttpResponse对象
        - request: django的传入请求
        - template_name: 模板名称
        - content_instance: 上下文环境
        - 案例参看代码 teacher_app/views/render_test
        
    - render_to_response
        - 根据给定的上下文字典渲染给定模板,返回渲染后的HttpResponse

- 系统内建视图
    - 系统内建视图，可以直接实用
    - 404
        - default.page_not_found(request, template_name='404.html')
        - 系统引发Http404时出发
        - 默认船体request_path变量给模板,即导致错误的URL
        - DEBUG=True则不会调用404, 取而代之是调试信息
        - 404视图会被传递一个RequestContext对象并且可以访问模板上下文处理器提供的变量(MEDIA_URL等)

    - 500(server error)
        -  defaults.server_error(request, template_name='500.html')
        - 需要DEBUG=False,否则不调用
    - 403 (HTTP Forbidden) 视图
        - defaults.permission_denied(request, template_name='403.html')
        - 通过PermissionDenied触发
    - 400 (bad request) 视图
        - defaults.bad_request(request, template_name='400.html')
        - DEBUG=False
    
# 8. 基于类的视图
- 和基于函数的视图的优势和区别:
    - HTTP方法的methode可以有各自的方法,不需要使用条件分支来解决
    - 可以使用OOP技术(例如Mixin)
- 概述
    - 核心是允许使用不同的实例方法来相应不同的HTTP请求方法,而避开条件分支实现
    - as_view函数昨晚类的可调用入库,该方法创建一个实例并调用dispatch方法,按照请求方法对请求进行分发,如果该
    方法没有定义,则引发HttpResponseNotAllowed
- 类属性使用
    - 在类定义时直接覆盖
    - 在调用as_view的时候直接昨晚参数使用,例如:
        ```
        urlpatterns = [
            url(r'^about/', GreetingView.as_view(greeting="G'day")),
            ]
        ```
- 对基于类的视图的扩充大致有三种方法: Mixin, 装饰as_view, 装饰dispatch
- 使用Mixin
    - 多继承的一种形式,来自弗雷的行为和属性组合在一起
    - 解决多继承问题
    - View的子类只能单继承,多继承会导致不可期问题
    - 多继承带来的问题:
        - 结构复杂
        - 优先顺序模糊
        - 功能冲突
    - 解决方法
        - 规格继承 - java interface
        - 实现继承 - python,ruby
- 在URLconf中装饰
    ```
    from django.contrib.auth.decorators import login_required, permission_required
    from django.views.generic import TemplateView

    from .views import VoteView

    urlpatterns = [
        url(r'^about/', login_required(TemplateView.as_view(template_name="secret.html"))),
        url(r'^vote/', permission_required('polls.can_vote')(VoteView.as_view())),
    ]

    ```
- 装饰类
    - 类的方法和独立方法不同,不能直接运用装饰器,需要用methode_decorator进行装饰
        ```
        from django.contrib.auth.decorators import login_required
        from django.utils.decorators import method_decorator
        from django.views.generic import TemplateView

        class ProtectedView(TemplateView):
            template_name = 'secret.html'

            @method_decorator(login_required)
            def dispatch(self, *args, **kwargs):
                return super(ProtectedView, self).dispatch(*args, **kwargs)
        ```