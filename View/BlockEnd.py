from functools import partial
from PyQt5 import QtCore
from View.QtFunctions import *
from Model.Logic import *


class BlockEnd(QWidget):
    def __init__(self, team):
        super(BlockEnd, self).__init__()
        self.setGeometry(100, 100, 320, 420)
        self.setStyleSheet("background-color: lightpink")
        self.setWindowTitle(str(team + 1) + ". csapat")
        self.initUI(team)

    def initUI(self, team):

        self.endOfBlock = createLabel(40, 40, 220, 40, "Blokk vége", self)
        self.endOfBlock.setAlignment(QtCore.Qt.AlignCenter)

        logic.Groups[team].endOfBlock = "1"
        logic.writeGroupDataToFile()

        self.right_answers = createLabel(40, 100, 220, 40, "", self)
        self.right_answers.setAlignment(QtCore.Qt.AlignCenter)

        num_of_block = logic.Groups[int(team)].getBlockFromExerciseNumber().numOfExercises
        self.right_answers.setText(str(num_of_block) + " feladatból\na jó megoldások száma:")

        self.right_answers_2 = createLabel(40, 140, 220, 40, str(logic.Groups[int(team)].RightExercises()) + " feladat", self)
        self.right_answers_2.setAlignment(QtCore.Qt.AlignCenter)

        self.respond = createLabel(40, 240, 220, 40, "", self)
        self.respond.setAlignment(QtCore.Qt.AlignCenter)

        if logic.Groups[int(team)].RightExercises() == num_of_block:

            if num_of_block != 1:
                self.respond.setText("Tökéletes, mehetsz tovább")
                self.pushbutton_ok = createPushButton(40, 340, 220, 40, "OK", partial(self.perfect, team), self)
                logic.writeGroupDataToFile()

            else:
                self.respond.setText("Befejezted a Tortúrát,\ngratulálunk!")
                logic.Groups[int(team)].torturaEnds()
                self.pushbutton_ok = createPushButton(40, 340, 220, 40, "VÉGE", self.completelyOver, self)
                logic.writeGroupDataToFile()

        else:
            if logic.Groups[int(team)].RightExercises() >= (num_of_block // 2) + 1:
                self.respond.setText("Tovább mész?")
                self.pushbutton_go = createPushButton(20, 340, 130, 40, "MEGY", partial(self.perfect, team), self)
                self.pushbutton_go.setStyleSheet("background-color: green")
                self.pushbutton_stay = createPushButton(170, 340, 130, 40, "ÚJRAKEZD", partial(self.startAgain, num_of_block, team),
                                                        self)
                self.pushbutton_stay.setStyleSheet("background-color: red")

                logic.writeGroupDataToFile()

            else:
                self.respond.setText("Sajnos nem mehetsz tovább")
                self.pushbutton_stay = createPushButton(40, 340, 220, 40, "ÚJRAKEZD", partial(self.startAgain, num_of_block, team),
                                                        self)

                logic.writeGroupDataToFile()

    def startAgain(self, num_of_block: int, team: int):
        self.close()
        logic.Groups[team].numOfExercise -= num_of_block
        logic.Groups[team].endOfBlock = 1
        logic.writeGroupDataToFile()
        self.mb = createMessageBox(200, 380, 100, 60, str(team + 1) + ". csapat",
                                   "A következő feladat száma: " + str(logic.Groups[int(team)].getSumOfExercises()),
                                   QMessageBox.Ok, self)

    def completelyOver(self):
        self.close()

    def perfect(self, team):
        self.close()
        logic.Groups[team].endOfBlock = "0"
        logic.writeGroupDataToFile()
        self.mb = createMessageBox(200, 380, 100, 60, str(team + 1) + ". csapat",
                                   "A következő feladat száma: " + str(logic.Groups[int(team)].getSumOfExercises()),
                                   QMessageBox.Ok, self)