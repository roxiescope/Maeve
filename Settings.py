import sys
from PyQt5.QtCore import Qt
from utils import xml_handler
from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit, QPushButton, \
    QCheckBox, QVBoxLayout, QLabel, QComboBox, QDesktopWidget
import DailyUpdates
from PyQt5 import QtCore

# TODO - option to open on startup

'''
Settings for:
* What widgets to display
* themes - dark, light, other colors/backgrounds
* Set passwords for external services - banking, to-do list, goodreads
* Notification settings - on, off, off for X hours
* Later: set where to display the widgets, and whether to break them out into separate windows

1. get values on the form and send them to setXML()
2. update the form values with getXML()
'''

global displayed_label
global weather_checkbox
global weather_zip
global banking_checkbox
global todo_checkbox
global reading_checkbox
global wardrobe_checkbox
global theme_label
global theme
global mintP_label
global mint_pass
global notif_label
global notification_delay


def set_weatherW(s):
    xml_handler.setXML('weather', s)

def set_bankingW(s):
    xml_handler.setXML('banking', s)

def set_todoW(s):
    xml_handler.setXML('todo', s)

def set_readingW(s):
    xml_handler.setXML('reading', s)

def set_wardrobeW(s):
    xml_handler.setXML('wardrobe', s)

def set_MintP(s):
    xml_handler.setXML('MintPass', s)

def set_notifications(s):
    x = 100
    if s == "On":
        x = 0
    elif s == "Off for 1 hour":
        x = 1
    elif s == "Off for 2 hours":
        x = 2
    elif s == "Off until I turn on":
        x = 3
    xml_handler.setXML('notifications', x)

def set_weatherZip(s):
    print("you're setting weather zip code")
    print(s)
    # DailyUpdates.updateWeather(s)


def get_Everything(weath, bank, td, read, ward, thm, mp, notif):
    # weather value
    weath_value = xml_handler.getXML('weather')
    if weath_value == str(0):
        weath.setCheckState(Qt.Unchecked)
    elif weath_value == str(2):
        weath.setCheckState(Qt.Checked)
    else:
        print("get_Everything invalid value for weather")
    # banking value
    bank_value = xml_handler.getXML('banking')
    if bank_value == str(0):
        bank.setCheckState(Qt.Unchecked)
    elif bank_value == str(2):
        bank.setCheckState(Qt.Checked)
    else:
        print("get_Everything invalid value for banking")
    # to-do value
    td_value = xml_handler.getXML('todo')
    if td_value == str(0):
        td.setCheckState(Qt.Unchecked)
    elif td_value == str(2):
        td.setCheckState(Qt.Checked)
    else:
        print("get_Everything invalid value for todo")
    # reading value
    read_value = xml_handler.getXML('reading')
    if read_value == str(0):
        read.setCheckState(Qt.Unchecked)
    elif read_value == str(2):
        read.setCheckState(Qt.Checked)
    else:
        print("get_Everything invalid value for reading")
    # wardrobe value
    ward_value = xml_handler.getXML('wardrobe')
    if ward_value == str(0):
        ward.setCheckState(Qt.Unchecked)
    elif ward_value == str(2):
        ward.setCheckState(Qt.Checked)
    else:
        print("get_Everything invalid value for wardrobe")
    # theme value
    thm_value = xml_handler.getXML('theme')
    if thm_value == "light":
        thm.setCurrentText("Light Mode")
    elif thm_value == "dark":
        thm.setCurrentText("Dark Mode")
    elif thm_value == "hawkeye":
        thm.setCurrentText("Hawkeye")
    elif thm_value == "daredevil":
        thm.setCurrentText("Daredevil")
    elif thm_value == "cottage":
        thm.setCurrentText("Cottage Life")
    elif thm_value == "teal":
        thm.setCurrentText("Teal")
    elif thm_value == "pastel":
        thm.setCurrentText("Pastel")
    else:
        print("get_Everything invalid value for theme")
    # notification value
    notif_value = xml_handler.getXML('notifications')
    if notif_value == str(0):
        notif.setCurrentText("On")
    elif notif_value == str(1):
        notif.setCurrentText("Off for 1 hour")
    elif notif_value == str(2):
        notif.setCurrentText("Off for 2 hours")
    elif notif_value == str(3):
        notif.setCurrentText("Off until I turn on")
    else:
        print("get_Everything invalid value for notifications")
    # MintPass value
    mp_value = xml_handler.getXML('MintPass')
    mp.setText(str(mp_value))

def get_theme(attribute):
    thm_value = xml_handler.getXML('theme')
    background_color = "background-color: white;"
    button_color = "background-color: gray; color: black;"
    unused_button_color = "background-color: gray; color: black; text-decoration: line-through"
    open_item_color = "background-color: gray; color: black;"
    completed_item_color = "background-color: dark-gray; color: white; text-decoration: line-through;"
    text_color = "color: black;"
    list_item_color = "QListWidget{color: black;}" \
                      "QListWidget QScrollBar{background : white;}" \
                      "QListView::item:selected{background: dark-gray; color: white;}"
    if thm_value == "light":
        background_color = "background-color: #c0c2ce;"
        button_color = "background-color: #e9e9ef; color: black;"
        open_item_color = "background-color: #e5e6eb; color: black;"
        completed_item_color = "background-color: #d2d4dc; color: black; text-decoration: line-through;"
        list_item_color = "QListWidget{color: black;}" \
                          "QListWidget QScrollBar{background : #c0c2ce;}" \
                          "QListView::item:selected{background: #d2d4dc; color: black;}"
        unused_button_color = "background-color: #b6b6c4; color: black; text-decoration: line-through;"
        text_color = "color: black;"
    elif thm_value == "dark":
        background_color = "background-color: #1e2020;"
        button_color = "background-color: #3b444b; color: white;"
        unused_button_color = "background-color: gray; color: black; text-decoration: line-through"
        open_item_color = "background-color: #232b2b; color: white;"
        completed_item_color = "background-color: #0e1111; color: white; text-decoration: line-through;"
        list_item_color = "QListWidget{color: white;}" \
                          "QListWidget QScrollBar{background : #1e2020; color: white;}" \
                          "QListView::item:selected{background: #232b2b; color: white;}"
        text_color = "color: white;"
    elif thm_value == "hawkeye":
        background_color = "background-color: #4a454f;"
        button_color = "background-color: #5f68ab; color: #cfd1e5;"
        open_item_color = "background-color: #bc8fc4; color: black;"
        completed_item_color = "background-color: #79519a; color: white;"
        list_item_color = "QListWidget{color: #e2cfe6;}" \
                          "QListWidget QScrollBar{background : #4a454f;}" \
                          "QListView::item:selected{background: #bc8fc4; color: black;}"
        unused_button_color = "background-color: #393e66; color: #cfd1e5; text-decoration: line-through;"
        text_color = "color: #e2cfe6;"
    elif thm_value == "daredevil":
        background_color = "background-color: #522022;"
        button_color = "background-color: #3a1618; color: #f4e4e5;"
        open_item_color = "background-color: #873438; color: #f4e4e5;"
        completed_item_color = "background-color: #ac4e48; color: #f4e4e5; text-decoration: line-through;"
        list_item_color = "QListWidget{color: #f4e4e5;}" \
                          "QListWidget QScrollBar{background : #522022;}" \
                          "QListView::item:selected{background: #873438; color: black;}"
        unused_button_color = "background-color: #230d0e; color: #f4e4e5; text-decoration: line-through;"
        text_color = "color: #f4e4e5;"
    elif thm_value == "cottage":
        background_color = "background-color: #4a3636;"
        button_color = "background-color: #7b2727; color: #d7bebe;"
        unused_button_color = "background-color: #31413f; color: #d7bebe; text-decoration: line-through"
        open_item_color = "background-color: #819b97; color: black;"
        completed_item_color = "background-color: dark-gray; color: white; text-decoration: line-through;"
        text_color = "color: #d7bebe;"
        list_item_color = "QListWidget{color: #d7bebe;}" \
                          "QListWidget QScrollBar{background : #4a3636;}" \
                          "QListView::item:selected{background: #819b97; color: black;}"
    elif thm_value == "teal":
        background_color = "background-color: #007777;"
        button_color = "background-color: #004444; color: #e5f1f1"
        unused_button_color = "background-color: #003333; color: #e5f1f1; text-decoration: line-through"
        open_item_color = "background-color: #005555; color: black;"
        completed_item_color = "background-color: #003333; color: #e5f1f1; text-decoration: line-through;"
        text_color = "color: black;"
        list_item_color = "QListWidget{color: black;}" \
                          "QListWidget QScrollBar{background : #007777;}" \
                          "QListView::item:selected{background: #003333; color: #e5f1f1;}"
    elif thm_value == "pastel":
        background_color = "background-color: #f7cac9;"
        button_color = "background-color: #c5b9cd; color: black;"
        unused_button_color = "background-color: #92a8d1; color: black; text-decoration: line-through"
        open_item_color = "background-color: #dec2cb; color: black;"
        completed_item_color = "background-color: #abb1cf; color: black; text-decoration: line-through;"
        text_color = "color: black;"
        list_item_color = "QListWidget{color: black;}" \
                          "QListWidget QScrollBar{background : #f7cac9;}" \
                          "QListView::item:selected{background: #abb1cf; color: black;}"
    else:
        print("theme is fucked up")

    if attribute == "background_color":
        return background_color
    elif attribute == "button_color":
        return button_color
    elif attribute == "open_item_color":
        return open_item_color
    elif attribute == "completed_item_color":
        return completed_item_color
    elif attribute == "list_item_color":
        return list_item_color
    elif attribute == "text_color":
        return text_color
    elif attribute == "unused_button_color":
        return unused_button_color
    else:
        print("theme attribute doesn't exist")


class MSettings(QMainWindow):
    window_closed = QtCore.pyqtSignal()
    theme_changed = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        # Default Theme
        # Main window properties
        # todo: set theme based on settings
        self.setStyleSheet(get_theme('background_color'))
        self.setWindowTitle('M: Settings')
        self.setBaseSize(180,300)
        # create widgets
        displayed_label = QLabel("Widgets Displayed:")
        weather_checkbox = QCheckBox("weather")
        weather_zip_label = QLabel("Zip Code: ")
        weather_zip = QLineEdit()
        weather_zip_submit = QPushButton('Submit', self)
        banking_checkbox = QCheckBox("banking")
        todo_checkbox = QCheckBox("todo")
        reading_checkbox = QCheckBox("reading")
        wardrobe_checkbox = QCheckBox("wardrobe")
        theme_label = QLabel("Theme:")
        theme = QComboBox()
        theme.addItems(["Light Mode", "Dark Mode", "Hawkeye", "Daredevil", "Cottage Life", "Teal", "Pastel"])
        mintP_label = QLabel("Mint Password:")
        mint_pass = QLineEdit("Password")
        notif_label = QLabel("Notifications:")
        notification_delay = QComboBox()
        notification_delay.addItems(["On", "Off for 1 hour", "Off for 2 hours", "Off until I turn on"])
        displayed_label.setStyleSheet(get_theme('text_color'))
        weather_checkbox.setStyleSheet(get_theme('text_color'))
        weather_zip_label.setStyleSheet(get_theme('text_color'))
        weather_zip.setStyleSheet(get_theme('open_item_color'))
        weather_zip_submit.setStyleSheet(get_theme('button_color'))
        banking_checkbox.setStyleSheet(get_theme('text_color'))
        todo_checkbox.setStyleSheet(get_theme('text_color'))
        reading_checkbox.setStyleSheet(get_theme('text_color'))
        wardrobe_checkbox.setStyleSheet(get_theme('text_color'))
        theme_label.setStyleSheet(get_theme('text_color'))
        theme.setStyleSheet(get_theme('open_item_color'))
        mintP_label.setStyleSheet(get_theme('text_color'))
        mint_pass.setStyleSheet(get_theme('open_item_color'))
        notif_label.setStyleSheet(get_theme('text_color'))
        notification_delay.setStyleSheet(get_theme('open_item_color'))

        get_Everything(weather_checkbox, banking_checkbox, todo_checkbox, reading_checkbox, wardrobe_checkbox, theme, mint_pass, notification_delay)

        # create layout and add widgets
        generalLayout = QVBoxLayout()
        generalLayout.addWidget(displayed_label)
        generalLayout.addWidget(weather_checkbox)
        generalLayout.addWidget(weather_zip_label)
        generalLayout.addWidget(weather_zip)
        generalLayout.addWidget(weather_zip_submit)
        generalLayout.addWidget(banking_checkbox)
        generalLayout.addWidget(todo_checkbox)
        generalLayout.addWidget(reading_checkbox)
        generalLayout.addWidget(wardrobe_checkbox)
        generalLayout.addWidget(theme_label)
        generalLayout.addWidget(theme)
        generalLayout.addWidget(mintP_label)
        generalLayout.addWidget(mint_pass)
        generalLayout.addWidget(notif_label)
        generalLayout.addWidget(notification_delay)

        # set on-click actions
        weather_checkbox.stateChanged.connect(set_weatherW)
        # weather_zip_submit.clicked.connect(self.weather_on_click(66209))
        # weather_zip.textEdited.connect(set_weatherZip)
        banking_checkbox.stateChanged.connect(set_bankingW)
        todo_checkbox.stateChanged.connect(set_todoW)
        reading_checkbox.stateChanged.connect(set_readingW)
        wardrobe_checkbox.stateChanged.connect(set_wardrobeW)
        theme.currentTextChanged.connect(self.set_Theme)
        mint_pass.textEdited.connect(set_MintP)
        notification_delay.currentTextChanged.connect(set_notifications)

        # add everything into the window
        widget = QWidget()
        widget.setLayout(generalLayout)
        self.setCentralWidget(widget)

    def weather_on_click(self, zipCode):
        print(int(zipCode))
        # set_weatherZip(int(zipCode))

    def location_on_the_screen(self):
        self.move(600, 400)

    def set_Theme(self, s):
        if s == "Light Mode":
            xml_handler.setXML('theme', 'light')
        elif s == "Dark Mode":
            xml_handler.setXML('theme', 'dark')
        elif s == "Hawkeye":
            xml_handler.setXML('theme', 'hawkeye')
        elif s == "Daredevil":
            xml_handler.setXML('theme', 'daredevil')
        elif s == "Cottage Life":
            xml_handler.setXML('theme', 'cottage')
        elif s == "Teal":
            xml_handler.setXML('theme', 'teal')
        elif s == "Pastel":
            xml_handler.setXML('theme', 'pastel')
        else:
            print("invalid theme")
        self.theme_changed.emit()

    def closeEvent(self, event):
        self.window_closed.emit()
        event.accept()
        # event.ignore() # if you want the window to never be closed

