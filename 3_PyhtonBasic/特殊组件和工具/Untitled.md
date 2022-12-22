Python标准数据库接口为 Python DB-API，Python DB-API为开发人员提供了数据库应用编程接口。



```
traceback
traceback模块用于追踪报错
https://blog.csdn.net/wenph2008/article/details/41399397
```



```
适用于 Python 的 AWS 开发工具包 (Boto3)
通过适用于 Python 的 AWS 开发工具包 [boto3](https://github.com/boto/boto3) 快速开始使用 AWS。Boto3 可以支持您轻松将 Python 应用程序、库或脚本与 AWS 服务进行集成，包括 Amazon S3、Amazon EC2 和 Amazon DynamoDB 等。
https://aws.amazon.com/cn/sdk-for-python/
```







Python 微服务框架 - Nameko



Cassandra

https://zhuanlan.zhihu.com/p/265027506

https://zh.wikipedia.org/wiki/Cassandra



Firebase

https://zh.m.wikipedia.org/zh-hk/Firebase

https://blog.back4app.com/zh/%E4%BB%80%E4%B9%88%E6%98%AF-firebase/





pyhtonic

### python库

turtle库

random库

PyInstaller库

jieba库

worldcloud库

os库





###### 网站

[PyPI pyphon package index](https://pypi.org/)

https://python123.io/

###### 库

os：操作系统交互，文件路径、进程管理、环境参数

turtle：绘图库，标准库

time：标准库

random：标准库

Pyinstaller

jieba：中文分词库，pip即可





wordcloud

词云

```
#GovRptWordCloudv1.py
import jieba
import wordcloud
f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
 
t = f.read()
f.close()
ls = jieba.lcut(t)
 
txt = " ".join(ls)
w = wordcloud.WordCloud( \
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc"    
    )
w.generate(txt)
w.to_file("grwordcloud.png")
```

```
#GovRptWordCloudv2.py
import jieba
import wordcloud
from scipy.misc import imread
mask = imread("chinamap.jpg")
excludes = { }
f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(\
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc", mask = mask
    )
w.generate(txt)
w.to_file("grwordcloudm.png")
```









python struct包

按照指定格式将Python数据转换为字符串,该字符串为字节流,如网络传输时,不能传输int,此时先将int转化为字节流,然后再发送;
按照指定格式将字节流转换为Python指定的数据类型;
处理二进制数据,如果用struct来处理文件的话,需要用’wb’,’rb’以二进制(字节流)写,读的方式来处理文件;
处理c语言中的结构体;
