from threading import *
from time import sleep

class hello(Thread):
    def run(self):
        for i in range(10):
            print("HELLO")
            sleep(1)


class hi(Thread):
    def run(self):
        for i in range(10):
            print("HI")
            sleep(1)


t1 = hello()
t2 = hi()

t1.start()
sleep(0.5)
t2.start()
t2.join()

print(current_thread())