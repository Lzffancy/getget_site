"""

用于验证登录状态

"""
import jwt
from django.http import JsonResponse
from django.conf import settings
from user.models import UserProfile

"""
def login_check(func):
    def wrap(request,*args,**kwargs):
           ...
        return JsonResponse(request, *args, **kwargs)
    return wrap
"""

#装饰器用于用户的登录检查
def login_check(func):
    def wrap(request, *args, **kwargs):
        # token
        # request.META包含了所有本次HTTP请求的Header信息
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            result = {'code': 403, 'error': '请先登录'}
            return JsonResponse(result)
        # 校验token
        try:
            # jwt.decode 自动校验key,过期时间
            payload = jwt.decode(token, settings.JWT_TOKEN_KEY, algorithms='HS256')
        except:
            result = {'code': 403, 'error': '请先登录'}
            return JsonResponse(result)

        else:
            username = payload['username']
            # 根据用户获取对象
            user_obj = UserProfile.objects.get(username=username)

            # 将user_obj作为请求对象request的附加属性
            request.myuser = user_obj
        return func(request, *args, **kwargs)

    return wrap


#判断用户的类别　区别,登录用户,非登录用户（游客）
def get_user_by_request(request):
    #1 获取token,如果不存在,返回None
    token = request.META.get('HTTP_AUTHORIZATION')
    if not token:
        return  None
    #2 token 不能通过验证,返回None
    else:
        try:
            payload=jwt.decode(token, settings.JWT_TOKEN_KEY, algorithms='HS256')
        except:
            return None
    #3 从私有声明中获取username,返回
        username=payload['username']
        return username


