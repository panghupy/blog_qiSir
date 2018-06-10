from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        # 给表单类传入一个字典类型的数据，来建立一个绑定实例。
        login_form = LoginForm(request.POST)
        # 验证输入的数据是否合法
        if login_form.is_valid():
            # user_info中记录了用户名和密码
            user_info = login_form.cleaned_data
            # authenticate()函数，其作用是检验此用户是否为本网站的用户，以及密码是否正确。是用户切密码正确就返回User的实例对象，否则就返回None
            user = authenticate(username=user_info['username'], password=user_info['password'])
            if user:
                # 把user这个实例对象当做一个参数，login()实现用户登录，这里会自动调用默认的session应用，将用户ID保存在session中，完成用户操作登录
                login(request, user)
                return HttpResponse('登录成功')
            else:
                return HttpResponse('账号或密码错误')
        else:
            return HttpResponse('无效的输入')
    if request.method == 'GET':
        login_form = LoginForm()
        # 这里login_form是未绑定实例，然后反馈到前段页面，等待用户填写内容
        return render(request, 'login.html', {'form': login_form})
