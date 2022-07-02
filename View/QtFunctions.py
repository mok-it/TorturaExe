from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


def createLabel(ww, wh, w, h, text, self):
    self.newlabel = QtWidgets.QLabel(self)
    self.newlabel.setGeometry(ww, wh, w, h)
    self.newlabel.setText(text)
    self.newlabel.setFont(QFont('Times', 10, QFont.Bold))
    return self.newlabel


def createPushButton(ww, wh, w, h, text, function, self):
    self.newpushbutton = QtWidgets.QPushButton(self)
    self.newpushbutton.setGeometry(ww, wh, w, h)
    self.newpushbutton.setText(text)
    self.newpushbutton.clicked.connect(function)
    self.newpushbutton.setFont(QFont('Times', 12, QFont.Bold))
    self.newpushbutton.setStyleSheet("border: 2px solid black; background-color: lightgray")
    return self.newpushbutton


def createLineEdit(ww, wh, w, h, self):
    self.newlineedit = QtWidgets.QLineEdit(self)
    self.newlineedit.setGeometry(ww, wh, w, h)
    return self.newlineedit


def createMessageBox(ww, wh, w, h, title, text, buttons, self):
    self.newmessagebox = QtWidgets.QMessageBox(self)
    self.newmessagebox.setGeometry(ww, wh, w, h)
    self.newmessagebox.setWindowTitle(title)
    self.newmessagebox.setText(text)
    self.newmessagebox.setStandardButtons(buttons)
    self.newmessagebox.setStyleSheet("background-color: white")
    # self.newmessagebox.setWindowModality(QtCore.Qt.ApplicationModal)
    self.newmessagebox.show()
    return self.newmessagebox


def createListWidget(ww, wh, w, h, title, function):
    newlistwidget = QListWidget()
    newlistwidget.setGeometry(ww, wh, w, h)
    newlistwidget.setWindowTitle(title)
    newlistwidget.itemDoubleClicked.connect(function)
    newlistwidget.show()
    return newlistwidget


def createSpinBox(ww, wh, w, h, minv, maxv, self):
    self.newspinbox = QtWidgets.QSpinBox(self)
    self.newspinbox.setMinimum(minv)
    self.newspinbox.setMaximum(maxv)
    self.newspinbox.setGeometry(ww, wh, w, h)
    return self.newspinbox
