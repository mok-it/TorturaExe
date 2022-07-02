from functools import partial
from PyQt5 import QtCore
from View.QtFunctions import *
from Model.Logic import *


class BlockEnd(QWidget):
    def __init__(self, csap):
        super(BlockEnd, self).__init__()
        self.setGeometry(100, 100, 320, 420)
        self.setStyleSheet("background-color: lightpink")
        self.setWindowTitle(str(csap + 1) + ". csapat")
        self.initUI(csap)

    def initUI(self, csap):

        self.endOfBlock = createLabel(40, 40, 220, 40, "Blokk vége", self)
        self.endOfBlock.setAlignment(QtCore.Qt.AlignCenter)

        logic.Groups[csap].endOfBlock = "1"
        logic.writeGroupDataToFile()

        self.rightAnswers = createLabel(40, 100, 220, 40, "", self)
        self.rightAnswers.setAlignment(QtCore.Qt.AlignCenter)

        numOfBlock = logic.Groups[int(csap)].getBlockFromExerciseNumber().numOfExercises
        self.rightAnswers.setText(str(numOfBlock) + " feladatból\na jó megoldások száma:")

        self.rightAnswers2 = createLabel(40, 140, 220, 40, str(logic.Groups[int(csap)].RightExercises()) + " feladat", self)
        self.rightAnswers2.setAlignment(QtCore.Qt.AlignCenter)

        self.respond = createLabel(40, 240, 220, 40, "", self)
        self.respond.setAlignment(QtCore.Qt.AlignCenter)

        if logic.Groups[int(csap)].RightExercises() == numOfBlock:

            if numOfBlock != 1:
                self.respond.setText("Tökéletes, mehetsz tovább")
                self.pushbutton_ok = createPushButton(40, 340, 220, 40, "OK", partial(self.tokeletes, csap), self)
                logic.writeGroupDataToFile()

            else:
                self.respond.setText("Befejezted a Tortúrát,\ngratulálunk!")
                logic.Groups[int(csap)].torturaEnds()
                self.pushbutton_ok = createPushButton(40, 340, 220, 40, "VÉGE", self.teljesenvege, self)
                logic.writeGroupDataToFile()

        else:
            if logic.Groups[int(csap)].RightExercises() >= (numOfBlock // 2) + 1:
                self.respond.setText("Tovább mész?")
                self.pushbutton_go = createPushButton(20, 340, 130, 40, "MEGY", partial(self.tokeletes, csap), self)
                self.pushbutton_go.setStyleSheet("background-color: green")
                self.pushbutton_stay = createPushButton(170, 340, 130, 40, "ÚJRAKEZD", partial(self.ujrakezd, numOfBlock, csap),
                                                        self)
                self.pushbutton_stay.setStyleSheet("background-color: red")

                logic.writeGroupDataToFile()

            else:
                self.respond.setText("Sajnos nem mehetsz tovább")
                self.pushbutton_stay = createPushButton(40, 340, 220, 40, "ÚJRAKEZD", partial(self.ujrakezd, numOfBlock, csap),
                                                        self)

                logic.writeGroupDataToFile()

    def ujrakezd(self, ii, csap):
        self.close()
        logic.Groups[csap].numOfExercise -= ii
        logic.Groups[csap].endOfBlock = 1
        logic.writeGroupDataToFile()
        self.mb = createMessageBox(200, 380, 100, 60, str(csap + 1) + ". csapat",
                                   "A következő feladat száma: " + str(logic.Groups[int(csap)].getSumOfExercises()),
                                   QMessageBox.Ok, self)

    def teljesenvege(self, csap):
        self.close()

    def tokeletes(self, csap):
        self.close()
        logic.Groups[csap].endOfBlock = "0"
        logic.writeGroupDataToFile()
        self.mb = createMessageBox(200, 380, 100, 60, str(csap + 1) + ". csapat",
                                   "A következő feladat száma: " + str(logic.Groups[int(csap)].getSumOfExercises()),
                                   QMessageBox.Ok, self)