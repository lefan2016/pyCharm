# coding=utf8
import threading, time


class MyThead(threading.Thread):
    def __init__(self, func, arg):
        super(MyThead, self).__init__()
        self.func = func
        self.arg = arg

    def run(self):
        apply(self.func, self.arg)


def sum(n):
    sum_r = 0
    for i in range(n + 1):
        sum_r += 1
        time.sleep(0.001)
    print sum_r


print(u'单线程')
time1 = time.time()
sum(10000)
sum(10000)
interval = time.time() - time1
print('time:{}'.format(interval))

print(u'多线程')
n = [10000, 10000]
mythead = []
time2 = time.time()
for i in range(len(n)):
    t = MyThead(func=sum, arg=(n[i],))
    mythead.append(t)

for i in range(len(n)):
    mythead[i].start()

for i in range(len(n)):
    mythead[i].join()

interval2 = time.time() - time2
print('time:{}'.format(interval2))
