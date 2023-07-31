import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QListWidget, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, pyqtSignal

class SecondWindow(QMainWindow):

    window_closed = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(SecondWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("App 2")
        label = QLabel("INSERTED VALUES")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

    def closeEvent(self, event):
        self.window_closed.emit()
        event.accept()
        # event.ignore() # if you want the window to never be closed

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("App")
        self.btn = QPushButton()
        self.btn.setText("click me!")
        self.btn.clicked.connect(self.openWin)
        winWidget = QWidget()
        self.setCentralWidget(winWidget)
        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        winWidget.setLayout(layout)

    def openWin(self):
        self.win = SecondWindow()
        self.win.window_closed.connect(self.do_something)
        self.win.show()

    def do_something(self):
        print("You closed the second window!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()