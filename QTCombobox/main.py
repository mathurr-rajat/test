from PyQt5 import uic
# # import sys
# # from PyQt5 import QtGui, QtCore, QtWidgets
# # from PyQt5.QtWidgets import QApplication
# #
# #
# # class Window(QtWidgets.QMainWindow):
# #
# #     def __init__(self):
# #         super(Window, self).__init__()
# #         self.setGeometry(50, 50, 500, 300)
# #         self.setWindowTitle("PyQT tuts!")
# #         self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
# #         # QGuiApplication
# #         extractAction = QApplication("&GET TO THE CHOPPAH!!!", self)
# #         # extractAction = QtGui.QAction("&GET TO THE CHOPPAH!!!", self)
# #         extractAction.setShortcut("Ctrl+Q")
# #         extractAction.setStatusTip('Leave The App')
# #         extractAction.triggered.connect(self.close_application)
# #
# #         self.statusBar()
# #
# #         mainMenu = self.menuBar()
# #         fileMenu = mainMenu.addMenu('&File')
# #         fileMenu.addAction(extractAction)
# #
# #         self.home()
# #
# #     def home(self):
# #         btn = QtGui.QPushButton("Quit", self)
# #         btn.clicked.connect(self.close_application)
# #         btn.resize(btn.minimumSizeHint())
# #         btn.move(0, 100)
# #
# #         extractAction = QtGui.QAction(QtGui.QIcon('todachoppa.png'), 'Flee the Scene', self)
# #         extractAction.triggered.connect(self.close_application)
# #
# #         self.toolBar = self.addToolBar("Extraction")
# #         self.toolBar.addAction(extractAction)
# #
# #         checkBox = QtGui.QCheckBox('Shrink Window', self)
# #         checkBox.move(100, 25)
# #         checkBox.stateChanged.connect(self.enlarge_window)
# #
# #         self.progress = QtGui.QProgressBar(self)
# #         self.progress.setGeometry(200, 80, 250, 20)
# #
# #         self.btn = QtGui.QPushButton("Download", self)
# #         self.btn.move(200, 120)
# #         self.btn.clicked.connect(self.download)
# #
# #         print(self.style().objectName())
# #         self.styleChoice = QtGui.QLabel("Windows Vista", self)
# #
# #         comboBox = QtGui.QComboBox(self)
# #         comboBox.addItem("motif")
# #         comboBox.addItem("Windows")
# #         comboBox.addItem("cde")
# #         comboBox.addItem("Plastique")
# #         comboBox.addItem("Cleanlooks")
# #         comboBox.addItem("windowsvista")
# #         comboBox.move(50, 250)
# #
# #         self.styleChoice.move(50, 150)
# #         comboBox.activated[str].connect(self.style_choice)
# #
# #         self.show()
# #
# #     def style_choice(self, text):
# #         self.styleChoice.setText(text)
# #         QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))
# #
# #     def download(self):
# #         self.completed = 0
# #
# #         while self.completed < 100:
# #             self.completed += 0.0001
# #             self.progress.setValue(self.completed)
# #
# #     def enlarge_window(self, state):
# #         if state == QtCore.Qt.Checked:
# #             self.setGeometry(50, 50, 1000, 600)
# #         else:
# #             self.setGeometry(50, 50, 500, 300)
# #
# #     def close_application(self):
# #         choice = QtGui.QMessageBox.question(self, 'Extract!',
# #                                             "Get into the chopper?",
# #                                             QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
# #         if choice == QtGui.QMessageBox.Yes:
# #             print("Extracting Naaaaaaoooww!!!!")
# #             sys.exit()
# #         else:
# #             pass
# #
# #
# # def run():
# #     # app = QtGui.QApplication(sys.argv)
# #     app = QtGui.QGuiApplication(sys.argv)
# #     GUI = Window()
# #     sys.exit(app.exec_())
# #
# #
# # run()
# from PyQt5.QtWidgets import QItemDelegate, QComboBox
#
#
# class ComboDelegate(QItemDelegate):
#     """
#     A delegate to add QComboBox in every cell of the given column
#     """
#
#     def __init__(self, parent):
#         super(ComboDelegate, self).__init__(parent)
#         self.parent = parent
#
#     def createEditor(self, parent, option, index):
#         combobox = QComboBox(parent)
#         version_list = []
#         for item in index.data():
#             if item not in version_list:
#                 version_list.append(item)
#
#         combobox.addItems(version_list)
#         combobox.currentTextChanged.connect(lambda value: self.currentIndexChanged(index, value))
#         return combobox
#
#     def setEditorData(self, editor, index):
#         value = index.data()
#         if value:
#             maxval = len(value)
#             editor.setCurrentIndex(maxval - 1)
#
#
# ComboDelegate.createEditor(parent=QWidget, option=QStyleOptionViewItem, index=QModelIndex) -> QWidge)
# # parent: QWidget | None,
# #                  option: QStyleOptionViewItem,
# #                  index:
#
#
#
# ComboDelegate.createEditor(QWidget,QStyleOptionViewItem, QModelIndex) -> QWidget)