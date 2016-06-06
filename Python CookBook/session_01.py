# coding: utf-8

# 第一章：数据结构与算法


# 1.解压序列赋值给多个变量
def find_argument(list=(2,3,4,5)):
	_, x, y, _ = list;
	return x, y
# print find_argument()


# 2.解压可迭代对象赋值给多个变量 # todo Python3?
# def drop_first_last(grades=(60, 70, 77, 80, 99, 100)):
# 	first, *middle, last = grades
# 	return avg(middle)
# print drop_first_last()


# 3.保留最后 N 个元素
def search(lines, pattern, history=5):
	from collections import deque
	previous_lines = deque(maxlen=history)
	for li in lines:
		if pattern in li:
			yield li, previous_lines
		previous_lines.append(li)

 if __name__ == '__main__':
 	with open(r'...txt') as f:
 		for line, prevlines in search(f, 'python', 5):
 			for pline in prevlines:
 				print (pline, end='')
 			print(line, end='')
 			print('-' * 20)


