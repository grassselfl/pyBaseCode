js

async的内部实现原理就是如果该函数中有一个返回值，当调用该函数时，默认会在内部调用Promise.solve() 方法把它转化成一个Promise 对象作为返回，
若函数内部抛出错误，则调用Promise.reject()返回一个Promise 对象

await即等待，用于等待一个Promise对象。它只能在异步函数 async function中使用，否则会报错
它的返回值不是Promise对象而是Promise对象处理之后的结果
await表达式会暂停当前 async function的执行，等待Promise 处理完成。若 Promise 正常处理(fulfilled)，其回调的resolve函数参数作为 await 表达式的值，继续执行 async function，若 Promise 处理异常(rejected)，await 表达式会把 Promise 的异常原因抛出。​如果 await 操作符后的表达式的值不是一个 Promise，那么该值将被转换为一个已正常处理的 Promise。

与Promise对比
1、不再需要多层.then方法
假设一个业务分很多步骤完成，并且每个步骤都是异步，依赖上一个步骤的结果。





py

关于协程的语法糖async和await


在3.5过后，我们可以使用async修饰将普通函数和生成器函数包装成异步函数和异步生成器

现在知道，完成异步的代码不一定要用async/await，使用了async/await的代码也不一定能做到异步，async/await是协程的语法糖，使协程之间的调用变得更加清晰，使用async修饰的函数调用时会返回一个协程对象，await只能放在async修饰的函数里面使用，await后面必须要跟着一个协程对象或Awaitable，await的目的是等待协程控制流的返回，而实现暂停并挂起函数的操作是yield。