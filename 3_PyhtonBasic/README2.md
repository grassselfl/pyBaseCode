# pyBaseCode
Python Base Code





```
builtins中__import__
手动导入模块


```



```
try:
    gs_async = __import__('gsasync')
except ImportError:
    if callable(log_to):
        log_to('persistence_cache_save try_delay failed.')
        
callable，p
```

```
sys.stdout.write("xxx")
类似print
```





types包

```python
def load_as_module(text=None, filename=None,
                   s3_bucket=None, s3_key=None,
                   module_name="config"):
    '''
    Load the code as a python module, and return the module.
    '''
    # TODO 学习一下
    config_module = types.ModuleType(module_name)
    load_to_dict(config_module.__dict__,
                 text=text, filename=filename,
                 s3_bucket=s3_bucket, s3_key=s3_key)
    return config_module
```





Cryptodome，加密解密



inspect

https://zhuanlan.zhihu.com/p/290018252



无缝缓存，





bottle

https://www.osgeo.cn/bottle/



python chalice



谷歌流量分析工具Google Analytics



python pprint

https://zhuanlan.zhihu.com/p/508317313







python官方文档

https://docs.python.org/3/contents.html



python书籍

https://github.com/WeitaoZhu/Python





流畅的python笔记

https://www.zhihu.com/column/c_1526275373855289345

https://blog.csdn.net/senior218218/article/details/105144181

https://zhuanlan.zhihu.com/p/59698230







async await语法

locals()定义本地变量

sys.version_info.major

python判空，复制粘贴要改



历史

异常重试

virtualenv
打包为exe
环境
规范
运算符
函数
数据类型
流程控制
注释
数学
时间
IO
元编程
单元测试
并发编程
内置数据结构
编解码、字符集
异常处理
函数式编程
图形用户界面
日志
网络编程
面向对象编程
系统

```python
# python源码分析
# https://zhuanlan.zhihu.com/p/127440493
# https://blog.csdn.net/fragmentalice/article/details/84571252
```

```python
# https://www.cnblogs.com/Eva-J/p/7277026.html
# import this

print(...)
```