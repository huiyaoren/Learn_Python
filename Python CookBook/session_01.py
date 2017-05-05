# coding: utf-8

# 第一章：数据结构与算法


# -----------------------------------------------------------------------------
# 1.解压序列赋值给多个变量
def find_argument(list=(2, 3, 4, 5)):
    _, x, y, _ = list
    return x, y


# print find_argument()


# -----------------------------------------------------------------------------
# 2.解压可迭代对象赋值给多个变量 # todo Python3?
def drop_first_last(grades=(60, 70, 77, 80, 99, 100)):
    first, *middle, last = grades
    return (middle)


# print(drop_first_last())


# -----------------------------------------------------------------------------
# 3.保留最后 N 个元素 # todo Python3
def search_last():
    def search(lines, pattern, history=5):
        from collections import deque
        previous_lines = deque(maxlen=history)
        for li in lines:
            if pattern in li:
                yield li, previous_lines  # todo??
            previous_lines.append(li)

    with open(r'test.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)


# search_last()


# -----------------------------------------------------------------------------
# 4.查找最大或最小的 N 个元素
def largest_and_smallest(nums=[1, 8, 11, -4, 18, 23]):
    import heapq
    print(heapq.nlargest(3, nums), heapq.nsmallest(3, nums))


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
    cheap = heapq.nlargest(1, portfolio, key=lambda s: s['price'])
    expensive = heapq.nsmallest(1, portfolio, key=lambda s: s['price'])
    print(cheap, expensive)


# lrgst_nd_smlst_by_kywrd()

# 需要在正确场合使用函数 nlargest() 和 nsmallest() 才能发挥它们的优势 
# 1.要查找的元素个数比较小时，函数 nlargest() 和 nsmallest() 很合适的。
# 2.如果仅仅查找唯一的最小或最大 (N=1) 的元素，那么使用 min() 和 max() 函数会更快些。
# 3.如果 N 的大小和集合大小接近的时候，通常先排序这 个集合然后再使用切片操作会更快点 ( sorted(items)[:N] 或者是 sorted(items)[N:] )。


# -----------------------------------------------------------------------------
# 5.实现一个优先级队列
def priority_queue():
    import heapq

    class PriorityQueue:
        def __init__(self):
            self._queque = []
            self._index = 0

        def push(self, item, priority):
            heapq.heappush(self._queque, (-priority, self._index, item))  # self._index?
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
    print(q.pop())
    print(q.pop())


# priority_queue()

# 代码中包含了一个 (-priority, index, item) 的元组。
# priority 为负数的目的是使得元素按照优先级从高到低排序。
# index 变量的作用是保证同等优先级元素的正确排序。
# 通过保存一个不断增加的 index 下标变量，可以确保元素按照它们插入的顺序排序。
# index 变量也在相同优先级元素比较的时候起到重要作用。

# 如果使用元组 (priority, item) ，只要两个元素的优先级不同就能比较。
# 但如果两个元素优先级一样，那么比较操作就会出错
# todo 元组对比大小
# (2, 2, "d") > (2, 1, "a") True
# (2, item("a")) > (2, item("d")) 无法对比


# -----------------------------------------------------------------------------
# 6.字典中的键值映射多个值

def create_dict():
    from collections import defaultdict

    d = {
        'a': [1, 2, 3],
        'b': [4, 5]
    }

    e = {
        'a': {1, 2, 3},
        'b': {4, 5}
    }

    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)

    e = defaultdict(set)
    e['a'].add(1)
    e['a'].add(2)
    e['b'].add(4)

    return d, e


# print create_dict()


# -----------------------------------------------------------------------------
# 7.字典排序
def odered_dict():
    from collections import OrderedDict
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['foo'] = 4

    e = {}
    e['foo'] = 1
    e['bar'] = 2
    e['spam'] = 3
    e['foo'] = 4

    print(d, e)


# odered_dict()
# OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。
# 对于已经存在的键的重复赋值不会改变键的顺序。 
# 一个 OrderedDict 的大小是普通字典的两倍，因为它内部维护着另外一个链表。
# 如果你要构建一个需要大量 OrderedDict 实例的数据结构的时候 
# 得仔细权衡一下是否使用 OrderedDict 带来的好处要大过额外内存消耗的影响。


# -----------------------------------------------------------------------------
# 8.字典的运算
def dict_compute():
    price = {
        'ACME': 45.23,
        'AAPL': 612.8,
        'IBM': 205,
        'HPQ': 37,
        'FB': 10.75
    }

    min_price = min(zip(price.values(), price.keys()))
    max_price = max(zip(price.values(), price.keys()))
    print(min_price, max_price)

    price_sorted = sorted(zip(price.values(), price.keys()))
    print(price_sorted)
    # 需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器。

    min_key = min(price, key=lambda k: price[k])
    max_key = max(price, key=lambda k: price[k])
    print(min_key, max_key)

    print(sorted(price, key=lambda k: price[k]))
    print(sorted(price, key=lambda d: d[0]))  # ?
    print(sorted(price, key=lambda d: d[1]))  # ?


# dict_compute()


# -----------------------------------------------------------------------------
# 9.查找两字典的相同点 python3
def find_same_in_dict():
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }

    # 集合操作
    print(a.keys() & b.keys())
    print(a.keys() - b.keys())
    print(a.items() & b.items())

    # 排除指定键
    # 由n个键值对 key:a[key] 组成的可迭代对象，参数 key 来自 a.keys()
    c = {key: a[key] for key in a.keys() - {'z', 'w'}}
    print(c)


# find_same_in_dict()

# items() 方法返回包含键值对的元素对象。
# 这个对象同样也支持集合操作，并且可以被用来查找两个字典有哪些相同的键值对。

# values() 方法并不支持集合操作。
# 因为值视图不保证所有值互不相同,某些集合操作会出现问题.
# 如果硬要在值上面执行这些集合操作，可以先将值集合转换成 set，然后再执行集合运算。


# -----------------------------------------------------------------------------
# 10.删除序列相同元素并保持顺序
def dedupe():
    def dedupe_1(items):  # hashable 类型
        seen = set()
        for item in items:
            if item not in seen:
                yield item
                seen.add(item)

    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe_1(a)))  # [1, 5, 2, 9, 10]

    def dedupe_2(items, key=None):  # 非 hashable 类型
        seen = set()
        for item in items:
            val = item if key is None else key(item)
            if val not in seen:
                yield item
                seen.add(val)

    b = [
        {'x': 1, 'y': 2},
        {'x': 1, 'y': 3},
        {'x': 1, 'y': 2},
        {'x': 2, 'y': 4},
        {'x': 1, 'y': 2},
        {'x': 1, 'y': 3},
        {'x': 2, 'y': 4}
    ]
    print(list(dedupe_2(b, lambda d: (d['x'], d['y']))))


# 如果仅消除重复元素，通常只要构造一个集合 set()


# -----------------------------------------------------------------------------
# 11.命名切片
def name_slice():
    record = '..........325..........432.5.........'
    SHARES = slice(10, 13)  # (start, end, step )
    PRICES = slice(23, 28)
    cost = int(record[SHARES]) * float(record[PRICES])
    print(cost)
    # 代码中如果出现大量的硬编码下标值会使得可读性和可维护性大大降低。
    # 内置的 slice() 函数创建了一个切片对象，可以被用在任何切片允许使用的地方。

    a = slice(0, 9, 2)
    s = "hello,world"
    print(a.indices(len(s)))
    for i in range(*a.indices(len(s))):
        print(s[i])
    # 可以通过调用切片的 indices(size) 方法将它映射到一个确定大小的序列上，
    # 这个方法返回一个三元组 (start, stop, step) ，所有值都会被合适的缩小以满足边界限制，


# -----------------------------------------------------------------------------
# 12.序列中出现次数最多的元素
def commen_counter():
    word = ['big', 'big', 'small', 'large', 'large', 'small', 'large']
    from collections import Counter
    word_counts = Counter(word)
    top_three = word_counts.most_common(3)
    print(top_three)


# commen_counter()

# return [('large', 3), ('big', 2), ('small', 2)]
# Counter 对象实际是一个字典：word_counter['large'] == 3
# Counter 对象可以跟数学运算符号结合：
# a = Counter(words)
# b = Counter(morewords)
# c = a + b
# d = a - b


# -----------------------------------------------------------------------------
# 13.通过键排序一个字典列表
def sort_dic_list_by_key():
    rows = [
        {'fname': 'Brain', 'lname': 'Jones', 'uid': '1001'},
        {'fname': 'David', 'lname': 'Beazley', 'uid': '1002'},
        {'fname': 'Jhon', 'lname': 'Cleese', 'uid': '1003'},
        {'fname': 'Big', 'lname': 'Jones', 'uid': '1004'}
    ]

    from operator import itemgetter

    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    print(rows_by_fname)

    rows_by_uid = sorted(rows, key=itemgetter('uid'))
    print(rows_by_uid)

    # itemgetter() 函数支持多个 key
    rows_by_name = sorted(rows, key=itemgetter('fname', 'lname'))
    print(rows_by_name)

# sort_dic_list_by_key()




# cd d:\tmp\huiyaoren\learn_python\'python cookbook'
