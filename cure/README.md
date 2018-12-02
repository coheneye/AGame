# TheCure Game Engin

一个简单的游戏服务器引擎。 The Cure 一个英伦乐队名稱。

## Language

No limitations

## Dependencies

 - pyuv(libuv): Eventloop，Native thread
 - python-nanomsg(libnanomsg): IPC
 - redis: redis client
 - pymysql: mysql driver
 - kazoo: zookeeper driver
 - flask: HTTP
 - others:
    protobuf
    zookeeper
    kafka
    mysql
    redis

## More

这是 The Cure 的 Python 实现版本，C 版本为类似的组合，添加了 luajit，绑定了 lua 脚本

## Architecture

- 协议支持 Websocket, 和 Tcp, KCP 等
- 数据编码支持 json, protobuf, msgpack 等
- 逻辑服务器：后端支持任意个逻辑服务器， 逻辑服务器之间独立。
- 接入层：前端支持 TCP, Websocket 接入层，每个接入进程同后端各个 LogicServer 有 PAIR 一对一连接
- MasterServer: 未定义
- 每个进程都能直接操作 redis
- 数据库操作分为写操作，和读操作。方便负载均衡。
- 日志：分为系统运行状态日志和系统内部状态日志。每个进程都能进行 pub, 日志消费者 sub 这些日志，或者直接push 到队列
- 事件：分为系统运行事件和系统逻辑事件。同日志。
- Timer: libuv
- file: 一般不进行文件操作
- 线程： 为单线程服务
- HTTP: 每个进程支持 HTTP 接口查询状态

## 热更新

1，配置热更新
    通过 http 接口控制重新加载

2，代码热更新
    A/B 服务器方案。

## 崩溃处理

1，zookeeper 监控报警。

## 第三方接口，HTTP 交互
