from queue import Queue
from threading import Thread
from time import sleep


class Producer:
    def __int__(self):
        self.q = Queue()

    # self.q = Queue()
    def produce(self):
        for i in range(1, 6):
            print("item produces ", i)
            # Queue.put(item=i)
            self.q.put(i)
            sleep(1)


class Consumer:
    def __init__(self, prod):
        self.prod = prod

    def consume(self):
        for i in range(1, 6):
            print("item received ", self.prod.q.get(i))


p = Producer()
C = Consumer(p)

# creating threads
t1 = Thread(target=p.produce())
t2 = Thread(target=C.consume())

t1.start()
t2.start()
