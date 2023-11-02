from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget
import threading


# class Button(QWidget):
#     clicked = Signal(Qt.MouseButton)
#
#     ...
#
#     def mousePressEvent(self, event):
#         self.clicked.emit(event.button())


def fun():
    return "0b01"


def check(t1):
    t1.join()
    return print(fun())


a = fun()
# signal1 = Signal(a)  # Python types
# signal2 = Signal(QUrl)  # Qt Types
# signal3 = Signal(int, str, int)  # more than one type
# signal4 = Signal((float,), (QDate,))  # optional types

# print(f"signal1 = {signal1}")
# print(f"signal3 = {signal3}")


t1 = threading.Thread(target=fun)
# print(t1)
t2 = threading.Thread(target=check)

# signal1 = Signal(t2)  # Python types
signal1 = fun()
print(signal1)
