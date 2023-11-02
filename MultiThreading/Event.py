from threading import Thread, Event
from time import sleep


def light_switch():
    sleep(3)
    e.set()
    print("Green light is ON")
    sleep(5)
    print("Red light is ON")
    e.clear()


def traffic():
    e.wait()
    while e.is_set():
        print("You can Go")
    print("\nProgram done")


e = Event()
t1 = Thread(target=light_switch())
t2 = Thread(target=traffic())
t1.start()
t2.start()
