# -*- coding: utf-8 -*-
"""
@Created On 2019-04-09
@Updated On 2019-04-09
@Author: tx
master/worker
"""
import random, time, queue
import threading
import multiprocessing
from multiprocessing.managers import BaseManager
from pyexcel_xls import save_data, get_data


task_queue = queue.Queue()
result_queue = queue.Queue()

	
def return_task():
	global task_queue
	return task_queue

def return_result():
	global result_queue
	return result_queue


class QueueManager(BaseManager):
	pass


# 生产贝壳网上成都在售全部房源
def get_url():
	url_list = []
	for i in range(30):  # 85
		url_list.append('https://cd.fang.ke.com/loupan/nhs1pg{0}'.format(i+1))
	return url_list


# 处理worker返回的结果
def write_excel(reusult):
	try:
		while (not task.empty()) or (not reusult.empty()):
			res = reusult.get(timeout=100)
			pass
			# for i in range(len(res[0]))
			print('In write_excel  hand result, res: {0}'.format(res))
	except Exception as e:
		raise e


def run():
	global task

	# 把两个Queue注册到网络上， callable关联了Queue对象
	QueueManager.register('get_task_queue', callable=return_task)
	QueueManager.register('get_result_queue', callable=return_result)

	manager = QueueManager(address=('192.168.3.61', 5000), authkey=b'abc')

	# 启动Queue
	manager.start()

	task = manager.get_task_queue()
	result = manager.get_result_queue()
	url_list = get_url()

	# 放几个任务进去:
	for url in url_list:
		task.put(url)

	# 多线程支持
	thd = threading.Thread(target=write_excel, args=(result,))
	thd.start()
	print('task ----> over\t', task.qsize())


	# 等待任务队列结束:
	while (not task.empty()) or (not result.empty()):
		pass
	print("Over")

	# 关闭 
	manager.shutdown()


if __name__ == '__main__':
	# Windows 运行下需要(检查它正在运行的进程是否应该通过管道或不运行代码。)
	multiprocessing.freeze_support()

	run()
