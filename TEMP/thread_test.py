# coding=utf8

import threading, time


class MyThread(threading.Thread):
    def __init__(self, func, arg):
        super(MyThread, self).__init__()
        self.func = func
        self.arg = arg

    def run(self):
        apply(self.func, self.arg)


def sum(n):
    sum_r = 0
    for i in range(n + 1):
        sum_r += i
        time.sleep(0.001)
    print sum_r


print u'单线程'
time1 = time.time()
sum(1000)
sum(1000)
interval = time.time() - time1
print 'time:', interval

print u'多线程1'
n = [1000, 1000]
mythread = []
time2 = time.time()
for i in range(len(n)):
    t = threading.Thread(target=sum, args=(n[i],))
    mythread.append(t)

for i in range(len(n)):
    mythread[i].start()

for i in range(len(n)):
    mythread[i].join()

interval2 = time.time() - time2
print 'time:', interval2

print u'多线程2'
n = [1000, 1000]
my = []
time3 = time.time()
for i in range(len(n)):
    t = MyThread(func=sum, arg=(n[i],))
    my.append(t)

for i in range(len(n)):
    my[i].start()

for i in range(len(n)):
    my[i].join()

interval3 = time.time() - time3
print 'time:', interval3
