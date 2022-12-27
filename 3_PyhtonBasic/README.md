



引用计数法为主

分代回收

​	标记清除算法







```c
// Programs/python.c:16

int
main(int argc, char **argv)
{
    return Py_BytesMain(argc, argv);
}
```





在 Python 中，内存管理机制被抽象成一种层次结构，共 4 层。

在最底层 (第 0 层)，是操作系统提供的内存管理接口，Python 不能干涉这一层的行为。剩余的 3 层都是由 Python 实现并维护的。

在第 1 层，是 Python 基于第 0 层操作系统的内存管理接口包装而成的。以 PyMem_为前缀的函数族。

```c
PyAPI_FUNC(void *) PyMem_Malloc(size_t size);
PyAPI_FUNC(void *) PyMem_Realloc(void *ptr, size_t new_size);
PyAPI_FUNC(void) PyMem_Free(void *ptr);

//obmalloc.c
void *PyMem_Malloc(size_t size)
{
    /* see PyMem_RawMalloc() */
    if (size > (size_t)PY_SSIZE_T_MAX)
        return NULL;
    return _PyMem.malloc(_PyMem.ctx, size);
}

void *PyMem_Realloc(void *ptr, size_t new_size)
{
    /* see PyMem_RawMalloc() */
    if (new_size > (size_t)PY_SSIZE_T_MAX)
        return NULL;
    return _PyMem.realloc(_PyMem.ctx, ptr, new_size);
}

void PyMem_Free(void *ptr)
{
    _PyMem.free(_PyMem.ctx, ptr);
}

```



在第 2 层，对 Python 中的一些常用对象，比如整数对象、字符串对象。

第二层是一组以PyObject_为前缀的函数簇，这一层主要是为了给Python对象的创建提供接口。我们知道Python对象的创建需要很多初始化的操作，例如引用计数，对象参数的类型等，原始的raw memory午饭完成这些工作，因此需要构建第二层内存管理

在第 3 层，主要是对象缓冲池机制。

真正在 Python 中发挥巨大作用的，是第 2 层的内存管理机制。这部分包括了 GC。













内存结构

在 Python 中，内存管理机制被抽象成一种层次结构，共 4 层。 在最底层 (第 0 层)，是操作系统提供的内存管理接口，Python 不能干涉这一层的行为。 剩余的 3 层都是由 Python 实现并维护的。



栈内存区

栈内存(Stack)：栈内存比较小，但是速度快。一般存储运行方法的形参、局部变量、返回值。由系统自动分配和回收

堆内存

堆内存(Heap)：对内存一般比较大，但是速度慢。一般放对象

静态存储区

静态存储区(Stastic)：这个区域也可以叫做常量池。存储全局变量、静态变量、常量，常量包括final修饰的常量和String常量。系统自动分配和回收

数据区

数据区(Data)：这个区域专门加载代码字节数据，方法数据、函数等.高级调度(作业调度)、中级调度(内存调度)、低级调度(进程调度)控制代码区执行代码的切换.



引用计数法

分代回收机制





粗略地认为interpreter = 编译器 + 虚拟机



我们在编写Python程序的时候，会注意到当使用impor关键字引入一个Python模块时，就会生成一个pyc文件。那么当我们使用import关键字的时候，Python会先在设定好的path中取寻找是否有xxx.pyc文件，如果没有而且只有py文件，那么Python就先将此py文件编译成PyCodeObject对象，然后再创建pyc文件，将PyCodeObject写入到该文件。然后才对该pyc文件进行import操作。其实当你用编辑器去打开pyc文件时，你会发现全是一些二进制的字节流，如果我们要了解pyc文件就必须了解PyCodeObject对象底层定义的每个成员变量究竟是什么。这就需要你再次回到上面的代码中去看我的注释，我们接着会一一讲解。需要注意的一点是在co_lnotab这个域中，并不会去直接记录它们的对应关系。它是以PyBytesObject数组的形式存在，数组中两个成对，第一个为字节码在co_code中的偏移量增量，第二个为py文件中行号的增量，注意，是增量。假如我们有如下的对应关系







