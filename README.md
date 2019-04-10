# master_worker demo

## 分布式学习中遇到的坑


* Windows下，master把Queue注册到网络上时, `callable`参数不能以`lambda`表达式
* Windows下，adddress 不能为空
* Windows运行分布式进程，需要先启动`freeze_support()`
`freeze_support()`"冻结"时生成Windows可执行文件
Window没有fork调用,需要"模拟"出fork的效果
`freeze_support()`函数的任务是检查它正在运行的进程是否应该通过管道或不运行代码。