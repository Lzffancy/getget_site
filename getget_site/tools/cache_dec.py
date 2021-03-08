"""

用于redis chache中的访问权限分类
"""
from django.core.cache import cache


from tools.login_dec import get_user_by_request

# 三层装饰器！！！！
def topic_cache(expire):
    def _topic_cache(func):
        def wrapper(request, *args, **kwargs):
            # 如果是详情页，不做缓存,直接调用被修饰的函数
            # 详细内容修改可能较为频繁！所以不做缓存
            if 't_id' in request.GET.keys():
                return func(request, *args, **kwargs)
            # 1 获取访问者用户名称
            visitor = get_user_by_request(request)
            # 2 获取作者的用户名称
            author = kwargs['author_id']
            if visitor==author:
                #博主字节访问
                cache_key='topic_cache_self_%s'%(request.get_full_path())
            else:
                cache_key='topic_cache_s%s'%(request.get_full_path())
                # 非博主访问
            print('-------------------cache key is',cache_key)
            # 按照缓存思想去做
            res=cache.get(cache_key)
            if res:
                print('------------------cache in',res)
                return res
            res =func(request, *args, **kwargs)
            cache.set(cache_key,res,expire)
            return res

        return wrapper

    return _topic_cache


# if __name__ == '__main__':
#      a(55)
