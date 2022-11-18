"""
python性能分析
时间戳相减：基本相减、装饰器实现

timeit







python -m cProfile test.py
python -m cProfile -o profile.stats test.py
生成一个统计文件然后通过python进行分析
import pstats
p = pstats.Stats(“profile.stats”)
p.print_stats()






用cProfile找到需要分析的函数，然后用line_profiler对函数进行分析。line_profiler可以帮你一行一行分析函数性能
pip install line_profiler

运行kernprof 逐行分析被修饰函数的CPU开销
kernprof.py -l -v test.py
-v 显示输出
-l 代表逐行分析而不是逐函数分析

Total Time：测试代码的总运行时间
Hits：表示每行代码运行的次数
Time：每行代码运行的总时间
Per Hits：每行代码运行一次的时间
% Time：每行代码运行时间的百分比

备注
使用time.perf_counter() 能够提供给定平台上精度最高的计时器，但是，它计算的仍然是时钟时间，很多因素会影响到它的精确度，比如机器负载。
如果你对于执行时间更感兴趣，使用time.process_time() 来代替它。



重要的三篇文章

https://zhuanlan.zhihu.com/p/83421076
https://blog.csdn.net/GuoQiZhang/article/details/105408009
https://blog.csdn.net/Bit_Coders/article/details/120154767


Scalene似乎是一个比内置分析工具更加厉害的工具



python实用工具类大全



openxl
https://www.cnblogs.com/programmer-tlh/p/10461353.html

python-docx
https://zhuanlan.zhihu.com/p/423704887



为什么python中==和is与java中==和equal的含义是相反的

因为python中一切皆对象，实际上==会调用__eq__双下方法，而这个方法效果等同于java中的equal，

常量值==好像不同于对象



而is才是对引用值的判断



Rich美化终端输出，与logging结合可以输出彩色日志，rich进度条
https://rich.readthedocs.io/en/stable/traceback.html



python引用复制问题



https://python123.io/index/py_env



pretty errors
https://www.cnblogs.com/wongbingming/p/12450565.html







"""
