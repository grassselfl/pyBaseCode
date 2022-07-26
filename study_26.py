import os, stat, sys

# os是py与操作系统进行交互
# sys是py与py解释器进行交互


"""文件夹相关"""
# 新建单级空文件夹
os.mkdir(r'./dir')
# 删除单级空文件夹
os.rmdir(r'./dir')
# 递归创建空文件夹
os.makedirs(r'.\dir\dir\dir')
# 递归删除空文件夹
os.removedirs(r'.\dir\dir\dir')
# 列出指定文件夹下所有文件和文件夹
os.listdir()

"""文件相关"""
file = open(".\\file2.txt", "w")
file.close()
# 获取文件属性
os.stat(".\\file2.txt")
# 重命名文件
os.rename(".\\file2.txt", "f.txt")
# 修改文件时间戳
os.utime(".\\f.txt")
# 删除文件
os.remove(".\\f.txt")  # os.unlink()等价
# 判断文件权限
os.access("file.txt", 1)
# 修改文件权限
os.chmod("file.txt", stat.S_IXOTH)

"""操作系统相关"""
# 操作系统标识
print(os.name)
# 系统环境变量，就是那个计算机->属性->高级系统设置->环境变量
print(os.environ)
# py执行操作系统命令，无返回值
os.system("dir")
os.popen("dir")
# os.execvp() 启动一个新进程
# os.fork() 获取父进程ID，在子进程返回中返回0
# os.execvp() 执行外部程序脚本（Uinx）
# os.spawn() 执行外部程序脚本（Windows）
# os.wait() 暂时未知


"""路径相关"""
# 系统路径分隔符
print(os.sep)
# 当前文件夹和父文件夹
print(os.curdir)
print(os.pardir)
# 获取当前工作目录
os.getcwd()
# 改变工作目录
os.chdir(r'C:\\')

# os.path，C:\Program Files\Windows Defender，实质上os.path相当于对路径字符串进行操作，并不会分析这个路径是否真实存在
path = "C:\Program Files\Windows Defender\MpCmdRun.exe"

# 判断文件或目录是否存在
print(os.path.exists(path))
# 获得绝对路径
print(os.path.abspath(path))
# 判断是否为绝对路径
print(os.path.isabs(path))
# 将文件路径和文件名分割(会将最后一个目录作为文件名而分离)
print(os.path.split(path))
# 将文件路径和文件扩展名分割成一个元组
print(os.path.splitext(path))
# 把路径分割为挂载点和文件名
# print(os.path.splitunc(path))
# 返回文件路径的目录部分
dirname = os.path.dirname(path)
print(dirname)
# 返回文件路径的文件名部分
basename = os.path.basename(path)
print(basename)
# 将文件路径和文件名凑成完整文件路径
print(os.path.join(dirname, basename))
print(os.path.join("dirname", "basename"))
# 将path修正为对应OS的标准路径格式
print(os.path.normpath(path))

print(sys.platform)
print(sys.version)
print(sys.path)  # 有先后顺序
print(sys.argv)  # python file.py 1 2 3 4 a b c d，命令行参数，实现从程序外部向程序传递参数
print(sys.modules)
# sys.stdin,sys.stdout,sys.stderr 标准输入、标准输出和错误输出

# 推出解释器
sys.exit()
