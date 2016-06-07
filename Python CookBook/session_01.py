# coding: utf-8

# 第一章：数据结构与算法


# -----------------------------------------------------------------------------
# 1.解压序列赋值给多个变量
def find_argument(list=(2,3,4,5)):
	_, x, y, _ = list;
	return x, y
# print find_argument()


# -----------------------------------------------------------------------------
# 2.解压可迭代对象赋值给多个变量 # todo Python3?
# def drop_first_last(grades=(60, 70, 77, 80, 99, 100)):
# 	first, *middle, last = grades
# 	return avg(middle)
# print drop_first_last()


# -----------------------------------------------------------------------------
# 3.保留最后 N 个元素 # todo Python3
def search(lines, pattern, history=5):
	from collections import deque
	previous_lines = deque(maxlen=history)
	for li in lines:
		if pattern in li:
			yield li, previous_lines
		previous_lines.append(li)

 # if __name__ == '__main__':
 # 	with open(r'...txt') as f:
 # 		for line, prevlines in search(f, 'python', 5):
 # 			for pline in prevlines:
 # 				print (pline, end='')
 # 			print(line, end='')
 # 			print('-' * 20)


# -----------------------------------------------------------------------------
# 4.查找最大或最小的 N 个元素
def largest_and_smallest(nums=[1,8,11,-4,18,23 ]):
	import heapq
	print heapq.nlargest(3, nums), heapq.nsmallest(3, nums)
# largest_and_smallest()

def lrgst_nd_smlst_by_kywrd():		
	import heapq
	portfolio = [ 
		{'name': 'IBM', 'shares': 100, 'price': 91.1},
		{'name': 'AAPL', 'shares': 50, 'price': 543.22}, 
		{'name': 'FB', 'shares': 200, 'price': 21.09}, 
		{'name': 'HPQ', 'shares': 35, 'price': 31.75}, 
		{'name': 'YHOO', 'shares': 45, 'price': 16.35}, 
		{'name': 'ACME', 'shares': 75, 'price': 115.65}
	]
	cheap = heapq.nlargest(1, portfolio, key=lambda s:s['price'])
	expensive = heapq.nsmallest(1, portfolio, key=lambda s:s['price'])
	print cheap, expensive
# lrgst_nd_smlst_by_kywrd()

# 需要在正确场合使用函数 nlargest() 和 nsmallest() 才能发挥它们的优势 
	# 1.要查找的元素个数比较小时，函数 nlargest() 和 nsmallest() 很合适的。	
	# 2.如果仅仅查找唯一的最小或最大 (N=1) 的元素，那么使用 min() 和 max() 函数会更快些。
	# 3.如果 N 的大小和集合大小接近的时候，通常先排序这 个集合然后再使用切片操作会更快点 ( sorted(items)[:N] 或者是 sorted(items)[N:] )。


# -----------------------------------------------------------------------------
# 5.实现一个优先级队列
import heapq

class PriorityQueue:
	def __init__(self):
		self._queque = []
		self._index = 0
	def push(self, item, priority):
		heapq.heappush(self._queque, (-priority, self._index, item))
		self._index += 1
	def pop(self):
		return heapq.heappop(self._queque)[-1]

class Item:
	def __init__(self, name):
		self.name = name
	def __repr__(self):
		return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print q.pop()
print q.pop()