from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, \
    QVBoxLayout, QLabel, QScrollArea, QDesktopWidget, \
    QCheckBox, QLineEdit, QDateEdit, QMenu, QListWidget, QListWidgetItem
from PyQt5 import QtCore
from PyQt5.QtCore import QEvent
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


class MTodo(QMainWindow):
    window_closed = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        # Main window properties
        # todo: set theme based on settings
        self.setStyleSheet(Settings.get_theme('background_color'))
        self.setWindowTitle('M: Todo List')

        self.dialogs = list()
        self.idList = {}
        self.listWidget = QListWidget()
        # create layout and add widgets
        self.generalLayout = QVBoxLayout()
        self._createButtons()
        self._displayTasks()
        self.scroll = QScrollArea()
        # add everything into the window
        self.widget = QWidget()
        self.widget.setLayout(self.generalLayout)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)

    def _createButtons(self):
        # todo - fix button page so it doesn't scroll, and set to the side
        self.buttons = {}
        create_task_button = QPushButton('Add Task +')
        create_task_button.setStyleSheet(Settings.get_theme('button_color'))
        select_all_check = QCheckBox("Select All")
        self.generalLayout.addWidget(create_task_button)

        create_task_button.clicked.connect(self.open_task_dialog)

    def _displayTasks(self):
        listItem = {}
        self.listWidget.setStyleSheet(Settings.get_theme('list_item_color'))
        self.idList = todolist_handler.getTask("id")
        nameList = todolist_handler.getTask("name")
        duedateList = todolist_handler.getTask("duedate")
        summaryList = todolist_handler.getTask("summary")
        statusList = todolist_handler.getTask("status")
        for x in range(len(nameList)):
            # todo: add border around each list item so they're visually separated more
            listItem[x] = QListWidgetItem(nameList[x] + '\n' + duedateList[x] + '\n' + summaryList[x])
            if statusList[x] == "closed":
                f = listItem[x].font()
                f.setStrikeOut(True)
                # todo: get background and text color change to work
                # f.setBackgroundColor(QColor("#79519a"))
                # f.setTextColor(QColor("white"))
                listItem[x].setFont(f)
                # listItem[x].setBackgroundColor(QColor("#79519a"))
                # listItem[x].setTextColor(QColor("white"))

            self.listWidget.addItem(listItem[x])

        self.listWidget.setSpacing(2)
        self.listWidget.installEventFilter(self)
        self.generalLayout.addWidget(self.listWidget)

    def open_task_dialog(self):
        d = self.widget.children()
        e = reversed(d)

        for g in e:
            g.deleteLater()
        self.widget.deleteLater()
        self.listWidget = QListWidget()
        self.generalLayout = QVBoxLayout()

        self.taskName = QLineEdit()
        self.dueDate = QDateEdit(calendarPopup=True)  # don't listen to pycharm; this works
        self.dueDate.setDateTime(QtCore.QDateTime.currentDateTime())
        self.summary = QLineEdit()
        self.add_task_button = QPushButton('Add Task')
        self.taskName.setStyleSheet(Settings.get_theme('open_item_color'))
        self.dueDate.setStyleSheet(Settings.get_theme('open_item_color'))
        self.summary.setStyleSheet(Settings.get_theme('open_item_color'))
        self.add_task_button.setStyleSheet(Settings.get_theme('button_color'))
        self.generalLayout.addWidget(self.taskName)
        self.generalLayout.addWidget(self.dueDate)
        self.generalLayout.addWidget(self.summary)
        self.generalLayout.addWidget(self.add_task_button)
        self.generalLayout.setContentsMargins(2, 2, 2, 2)

        self.add_task_button.clicked.connect(self.add_task)

        self._displayTasks()
        self.scroll = QScrollArea()
        # add everything into the window
        self.widget = QWidget()
        self.widget.setLayout(self.generalLayout)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)

    def add_task(self, event):
        # todo: Schedule windows notification reminder(s) for this task
        todolist_handler.addTask(self.taskName.text(), self.dueDate.text(), self.summary.text())
        self.refresh()

    def refresh(self):
        d = self.widget.children()
        e = reversed(d)

        for g in e:
            g.deleteLater()
        self.widget.deleteLater()
        self.generalLayout = QVBoxLayout()
        self.listWidget = QListWidget()
        self._createButtons()
        self._displayTasks()
        self.scroll = QScrollArea()
        # add everything into the window
        self.widget = QWidget()
        self.widget.setLayout(self.generalLayout)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)

    def delete_task(self, index):
        # todo: Remove any scheduled windows notification reminders for this task
        index = index + 1
        for x in self.idList:
            if x == str(index):
                id_value = int(x) - 1
                # print(id_value)
                todolist_handler.removeTask(self.idList[id_value])
        self.refresh()

    def orderby_date(self):
        print("order tasks by due date")

    def location_on_the_screen(self):
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        x = ag.width() - widget.width() - 600
        y = 2 * ag.height() - sg.height() - widget.height() - 600
        self.move(x, y)

    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu and source is self.listWidget:
            menu = QMenu()
            markDoneButton = menu.addAction("Mark 'Done'")
            markUndoneButton = menu.addAction("Mark 'Not Done'")
            deleteButton = menu.addAction("Delete")
            action = menu.exec_(self.mapToGlobal(event.pos()))
            if action == markDoneButton:
                self.MarkDone(self.listWidget.currentRow())
            elif action == markUndoneButton:
                self.MarkUndone(self.listWidget.currentRow())
            elif action == deleteButton:
                self.delete_task(self.listWidget.currentRow())
            return True
        return super().eventFilter(source, event)

    def MarkDone(self, index):
        for x in range(len(self.idList)):
            if x == int(index):
                id_value = self.idList[x]
                todolist_handler.changeStatus(id_value, True)
        self.refresh()

    def MarkUndone(self, index):
        for x in range(len(self.idList)):
            if x == int(index):
                id_value = self.idList[x]
                todolist_handler.changeStatus(id_value, False)
        self.refresh()

    def closeEvent(self, event):
        self.window_closed.emit()
        event.accept()
        # event.ignore() # if you want the window to never be closed
