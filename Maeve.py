import sys
import DailyUpdates
from Settings import MSettings
import Settings
from Todo import MTodo
from Reading import MReading
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, \
    QVBoxLayout, QGridLayout, QLabel

__version__ = '0.1'
ERROR_MSG = 'ERROR'



class MaeveUI(QMainWindow):
    def __init__(self):
        super().__init__()
        # Variables to track which windows are open
        self.settings_open = False
        self.Maeve_open = False
        self.Todo_open = False
        self.Reading_open = False
        # Setting window color based on theme from settings
        self.setStyleSheet(Settings.get_theme('background_color'))
        self.setWindowTitle('Maeve')
        # Central widget and general layout of window
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # List of windows created
        self.dialogs = list()
        # Display and buttons
        self.label = QLabel()
        self.dateAndTime = {}
        self.DateTime()
        self._createQuote()
        self._createButtons()

    def showTime(self):
        current_time = QTime.currentTime()
        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')
        # showing it to the label
        self.label.setText(label_time)

    def DateTime(self):
        # This function adds the date and time
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        stuffLayout = QGridLayout()
        stuffLayout.addWidget(self.label,0,1)
        self.generalLayout.addLayout(stuffLayout)

        # stuffLayout = QGridLayout()
        # stuff = {QLabel(DailyUpdates.updateDate()): (0, 0),
        #          self.label: (0, 3), # todo - make this dynamically change while window is open
        #          }
        # for stfText, pos in stuff.items():
        #     self.dateAndTime[stfText].setWordWrap(True)
        #     self.dateAndTime[stfText].setFixedSize(120, 40)
        #     self.dateAndTime[stfText].setStyleSheet(Settings.get_theme('text_color'))
        #     stuffLayout.addWidget(self.dateAndTime[stfText], pos[0], pos[1])
        #
        # self.generalLayout.addLayout(stuffLayout)

    def _createQuote(self):
        self.quote = QLabel(DailyUpdates.updateQuote())
        self.quote.setWordWrap(True)
        self.quote.resize(self.quote.sizeHint())
        self.quote.setAlignment(Qt.AlignCenter)
        self.quote.setStyleSheet(Settings.get_theme('text_color'))
        # Add display to general layout
        self.generalLayout.addWidget(self.quote)

    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        buttons = {'To-Do List': (0, 1),
                   'Reading List': (1, 1),
                   'Wardrobe': (2, 1),
                   'Banking': (3, 1),
                   'Settings': (4, 1),
                   }
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setStyleSheet(Settings.get_theme('button_color'))
            self.buttons[btnText].setFixedSize(100, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])

        self.buttons['Wardrobe'].setStyleSheet(Settings.get_theme('unused_button_color'))
        self.buttons['Banking'].setStyleSheet(Settings.get_theme('unused_button_color'))
        self.generalLayout.addLayout(buttonsLayout)

        self.buttons['Settings'].clicked.connect(self.settings_clicked)
        self.buttons['To-Do List'].clicked.connect(self.todo_clicked)
        self.buttons['Reading List'].clicked.connect(self.reading_clicked)

    def settings_clicked(self):
        if self.settings_open:
            print("Settings is already open")
        else:
            self.settings_dialog = MSettings()
            self.dialogs.append(self.settings_dialog)
            self.settings_dialog.location_on_the_screen()
            self.settings_dialog.show()
            self.settings_open = True
            self.settings_dialog.theme_changed.connect(self.reload_windows)
            self.settings_dialog.window_closed.connect(self.settings_closed)



    def settings_closed(self):
        self.settings_open = False

    def todo_clicked(self):
        if self.Todo_open:
            print("To-Do is already open")
        else:
            self.todo_dialog = MTodo()
            self.dialogs.append(self.todo_dialog)
            self.todo_dialog.location_on_the_screen()
            self.todo_dialog.show()
            self.Todo_open = True
            self.todo_dialog.window_closed.connect(self.todo_closed)

    def todo_closed(self):
        self.Todo_open = False

    def reading_clicked(self):
        if self.Reading_open:
            print("Reading is already open")
        else:
            self.reading_dialog = MReading()
            self.dialogs.append(self.reading_dialog)
            self.reading_dialog.location_on_the_screen()
            self.reading_dialog.show()
            self.Reading_open = True
            self.reading_dialog.window_closed.connect(self.reading_closed)

    def reading_closed(self):
        self.Reading_open = False

    def closeEvent(self, event):
        for window in QApplication.topLevelWidgets():
            window.close()


    def reload_windows(self):
        if self.settings_open == True:
            self.settings_dialog.close()
            self.settings_open = False
            self.settings_clicked()
        if self.Todo_open == True:
            self.todo_dialog.close()
            self.Todo_open = False
            self.todo_clicked()
        if self.Reading_open == True:
            self.reading_dialog.close()
            self.Reading_open = False
            self.reading_clicked()
        if self.Maeve_open == True:
            d = self._centralWidget.children()
            e = reversed(d)

            for g in e:
                g.deleteLater()
            self.setStyleSheet(Settings.get_theme('background_color'))
            self.setWindowTitle('Maeve')
            # Central widget and general layout of window
            self.generalLayout = QVBoxLayout()
            self._centralWidget = QWidget(self)
            self.setCentralWidget(self._centralWidget)
            self._centralWidget.setLayout(self.generalLayout)
            self.dialogs = list()
            # Display and buttons
            self.DateTime()
            self._createQuote()
            self._createButtons()

    def implement_MainSettings(self):
        print("eventually this is gonna implement settings")
        # TODO: change how many widgets to display


def main():
    # todo: make app run in taskbar
    # check if any items are past due on startup
    # check if toast_test.py is running
    # if it is: do nothing
    # if it isn't: start it up
    maeve = QApplication(sys.argv)
    maeve.setStyle("Fusion")
    view = MaeveUI()
    view.show()
    view.Maeve_open = True
    sys.exit(maeve.exec_())


if __name__ == '__main__':
    main()

# TODO: button for "wardrobe"
# TODO: button for "banking"
# TODO: display weather
# TODO: display fun fact of the day
# TODO: display copyright/author info
