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
