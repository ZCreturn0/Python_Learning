#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psutil

# print('CPU逻辑数量:',psutil.cpu_count())
# print('CPU物理核心:',psutil.cpu_count(logical=False))

# #统计CPU的用户／系统／空闲时间
# print(psutil.cpu_times())

# #实现类似top命令的CPU使用率
# for i in range(10):
#     print(psutil.cpu_percent(interval=1,percpu=True))

# #获取物理内存和交换内存信息
# print(psutil.virtual_memory())
# print(psutil.swap_memory())

# # 磁盘分区信息
# print(psutil.disk_partitions())
# # 磁盘使用情况
# print(psutil.disk_usage('/'))
# # 磁盘IO
# print(psutil.disk_io_counters())

# # 获取网络读写字节／包的个数
# print(psutil.net_io_counters())
# # 获取网络接口信息
# print(psutil.net_if_addrs())
# # 获取网络接口状态
# print(psutil.net_if_stats())
# #获取当前网络连接信息
# print(psutil.net_connections())

