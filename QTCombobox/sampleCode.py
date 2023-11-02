from PySide6.QtCore import Qt, Signal
import threading


def response():
    return "0b01"


def check():
    return print(response())


response_thread = threading.Thread(target=response)
check_thread = threading.Thread(target=check)

response_thread.start()
check_thread.start()
response_thread.join()


# signal1 = Signal(check_thread.start())
# print(signal1)

check_thread.join()
