# -*- coding: utf-8 -*-
from __future__ import absolute_import


# 解析命令行参数，传入 master 组内编号，根据组号（指定）和组内编号--

# 加载 master 配置， 建立 master rpc 监听
# 并建立 publisher 服务。

# 当收到 rpc 请求，选择路由到不同的 rpc client, 或者 publish


class MasterServer(object):
    def __init__(self, addr):
        pass

    def serve_forever(self):
        pass