# -*- coding: utf-8 -*-
"""
@Created On 2019-04-09
@Updated On 2019-04-09
@Author: tx
master/worker
"""
import random
import time
import queue
import requests
from multiprocessing.managers import BaseManager
from pyexcel_xls import save_data, get_data


class QueueManager(BaseManager):
	pass
		

# worker 的事务（发请求，解析出数据）
def find_data(url):
	pass
	result.put("{} result".format(url))
	

def main():
	global result

	# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
	QueueManager.register('get_task_queue')
	QueueManager.register('get_result_queue')


	manager = QueueManager(address=('192.168.3.61', 5000), authkey=b'abc')
	manager.connect()

	task = manager.get_task_queue()
	result = manager.get_result_queue()
	while not task.empty():
		time.sleep(2)
		url = task.get(timeout=100)
		find_data(url)

	manager.shutdown()


if __name__ == '__main__':
	main()
