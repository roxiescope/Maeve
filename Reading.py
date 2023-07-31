from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, \
    QVBoxLayout, QLabel, QScrollArea, QDesktopWidget, \
    QCheckBox, QLineEdit, QDateEdit, QMenu, QListWidget, QListWidgetItem
from PyQt5 import QtCore
from PyQt5.QtCore import QEvent
import Settings
from utils import readinglist_handler

'''
Reading List
1. Get info from Goodreads (if possible)
2. Display three sections - books in progress, books not started, and books finished
3. For each book, show a card that has % complete (probably # of chapters) and due date
4. Show top bar with "number of books read this year/total"
'''


class MReading(QMainWindow):
    window_closed = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        # Main window properties
        self.setStyleSheet(Settings.get_theme('background_color'))
        self.setWindowTitle('M: Reading List')
        self.dialogs = list()
        self.idList = {}
        self.listWidget = QListWidget()
        # create layout and add widgets
        self.generalLayout = QVBoxLayout()
        self._createButtons()
        self._displaybooks()
        self.scroll = QScrollArea()
        # add everything into the window
        self.widget = QWidget()
        self.widget.setLayout(self.generalLayout)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)

    def _createButtons(self):
        # todo - fix button page so it doesn't scroll, and set to the side
        # self.buttons = {}
        create_book_button = QPushButton('Add Task +')
        create_book_button.setStyleSheet(Settings.get_theme('button_color'))
        select_all_check = QCheckBox("Select All")
        self.generalLayout.addWidget(create_book_button)

        create_book_button.clicked.connect(self.open_task_dialog)

    def _displaybooks(self):
        listItem = {}
        self.listWidget.setStyleSheet(Settings.get_theme('list_item_color'))
        self.idList = readinglist_handler.getBook("id")
        nameList = readinglist_handler.getBook("name")
        duedateList = readinglist_handler.getBook("duedate")
        summaryList = readinglist_handler.getBook("summary")
        statusList = readinglist_handler.getBook("status")
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

        self.bookName = QLineEdit()
        self.dueDate = QDateEdit(calendarPopup=True)  # don't listen to pycharm; this works
        self.dueDate.setDateTime(QtCore.QDateTime.currentDateTime())
        self.summary = QLineEdit()
        self.add_book_button = QPushButton('Add Book')
        self.bookName.setStyleSheet(Settings.get_theme('open_item_color'))
        self.dueDate.setStyleSheet(Settings.get_theme('open_item_color'))
        self.summary.setStyleSheet(Settings.get_theme('open_item_color'))
        self.add_book_button.setStyleSheet(Settings.get_theme('button_color'))
        self.generalLayout.addWidget(self.bookName)
        self.generalLayout.addWidget(self.dueDate)
        self.generalLayout.addWidget(self.summary)
        self.generalLayout.addWidget(self.add_book_button)

        self.add_book_button.clicked.connect(self.add_book)

        self._displaybooks()
        self.scroll = QScrollArea()
        # add everything into the window
        self.widget = QWidget()
        self.widget.setLayout(self.generalLayout)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)

    def add_book(self, event):
        # print(self.bookName.text())
        # print(self.dueDate.text())
        # print(self.summary.text())
        readinglist_handler.addBook(self.bookName.text(), self.dueDate.text(), self.summary.text())
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
        self._displaybooks()
        self.scroll = QScrollArea()
        # add everything into the window
        self.widget = QWidget()
        self.widget.setLayout(self.generalLayout)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)
        # print("you refreshed the window")

    def delete_book(self, index):
        # print("delete this book:" + str(index))
        index = index + 1
        for x in self.idList:
            if x == str(index):
                id_value = int(x) - 1
                # print(id_value)
                readinglist_handler.removeBook(self.idList[id_value])
        self.refresh()

    def orderby_date(self):
        # todo - order by due date
        print("order tasks by due date")

    def location_on_the_screen(self):
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        x = ag.width() - widget.width() - 600
        y = 2 * ag.height() - sg.height() - widget.height()
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
                self.delete_book(self.listWidget.currentRow())
            return True
        return super().eventFilter(source, event)

    def MarkDone(self, index):
        # print("you're marking this task done: " + str(index))
        index = index + 1
        for x in self.idList:
            if x == str(index):
                id_value = int(x) - 1
                readinglist_handler.changeStatus(self.idList[id_value], True)
        self.refresh()

    def MarkUndone(self, index):
        # print("you're marking this task not done: " + str(index))
        index = index + 1
        for x in self.idList:
            if x == str(index):
                id_value = int(x) - 1
                # print(id_value)
                readinglist_handler.changeStatus(self.idList[id_value], False)
        self.refresh()

    def closeEvent(self, event):
        self.window_closed.emit()
        event.accept()
        # event.ignore() # if you want the window to never be closed
