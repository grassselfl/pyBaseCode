# import 内置模块、三方模块、自定义模块

# from module import ver可能会被本地 名称（引用 ） 覆盖
# 所以from moudle import * 十分的不安全


# __all__ 是 list 类型, 不要写表达式
# 按照 PEP8 建议的风格，__all__ 应该写在所有 import 语句下面，和函数、常量等模块成员定义的上面
# 正式代码中尽量不要使用 from XXX import *
#
# 约定公开接口 ： 可以清晰明了的知道该文件暴露的接口， 约定成俗的调用该接口。
# 限制该行为from XXX import * ： code当中不建议使用 from xxx import * 的写法的，但线下调试的时候经常用到。如果模块中没有定义 __all__，执行 from XXX import * 的时候会将模块中非下划线开头的成员都导入当前命名空间中，这样就有可能弄脏当前命名空间， 调试容易产生问题。如果显式声明了 __all__，import * 就只会导入 __all__ 列出的成员。但它只对import *起作用，对from XXX import XXX不起作用。
#
# 模块就是py文件
#
# 可以import的是包、模块、变量、函数，本质是导入变量和函数
print(__name__)