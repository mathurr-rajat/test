# Python program to illustrate the concept
# of threading
# importing the threading module
import threading

sp = False
def print_hello():
    global sp
    for i in range(100):
        while not sp:
            pass
        print("Hello")
        sp = not sp



def print_hi():
    global sp
    for i in range(100):
        while sp:
            pass
        print("Hi")
        sp = not sp

if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_hello)
    t2 = threading.Thread(target=print_hi)

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # t2.start()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done!")