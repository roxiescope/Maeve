import sys
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QDateEdit
import Settings
from utils import todolist_handler

'''
Todo list - Microsoft API (currently doesn't work, won't connect.):
1. Get Todo password from Settings
2. Pull all lists from Microsoft Todo List
3. Display on window

app secret: 0jk8Q~IzHks--tU1.JuU2q.zMIOp_CvjZ.7uOaYR
app name: Graph Python Quickstart
app ID (or client ID): aaa995d4-cd05-4f22-80f6-97d4084d4121

Todo List - Tasks from scratch:
1. Pull tasks from xml file
2. Display on screen
3. User clicks on a task, it pops into a separate window
4. User clicks "Create Task" button, window pops up
5. User fills in task fields and clicks "submit"
'''


class MTaskCreator(QMainWindow):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        # Main window properties
        # todo: set theme based on settings
        self.setStyleSheet(Settings.get_theme('background_color'))
        self.setWindowTitle('M: Create a New Task')
        # create widgets
        self.generalLayout = QVBoxLayout()
        self.taskName = QLineEdit()
        self.dueDate = QDateEdit(calendarPopup=True) # don't listen to pycharm; this works
        self.dueDate.setDateTime(QtCore.QDateTime.currentDateTime())
        self.summary = QLineEdit()
        self.create_task_button = QPushButton('Create Task')
        self.create_task_button.setStyleSheet(Settings.get_theme('button_color'))
        self.generalLayout.addWidget(self.taskName)
        self.generalLayout.addWidget(self.dueDate)
        self.generalLayout.addWidget(self.summary)
        self.generalLayout.addWidget(self.create_task_button)

        self.create_task_button.clicked.connect(self.create_task)

        # add everything into the window
        widget = QWidget()
        widget.setLayout(self.generalLayout)
        self.setCentralWidget(widget)

    def create_task(self, event):
        # todo - call todolist_handler.py
        print(self.taskName.text())
        print(self.dueDate.text())
        print(self.summary.text())
        todolist_handler.addTask(self.taskName.text(), self.dueDate.text(), self.summary.text())

    def closeEvent(self, event):
        self.window_closed.emit()
        event.accept()
        # event.ignore() # if you want the window to never be closed



