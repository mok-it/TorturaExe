# import windows
from View.BlockEnd import *


class ExerciseSolution(QWidget):
    def __init__(self, csap):
        super(ExerciseSolution, self).__init__()
        self.setGeometry(100, 100, 300, 520)
        self.setStyleSheet("background-color: lightblue")
        self.setWindowTitle(str(csap + 1) + " - " + str(logic.Groups[int(csap)].getSumOfExercises()) + ". feladat")
        self.initUI(csap)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

    def initUI(self, csap):

        self.groupNumber = createLabel(40, 40, 220, 20, str(csap + 1) + ". csapat", self)
        self.groupNumber.setAlignment(QtCore.Qt.AlignCenter)

        groupnames = []
        sz = 0
        for i in logic.Groups[csap].members:
            tag = createLabel(40, 80 + 20 * sz, 220, 20, i, self)
            tag.setAlignment(QtCore.Qt.AlignCenter)
            groupnames.append(tag)
            sz += 1

        self.exerciseNumber = createLabel(40, 180, 220, 40, str(logic.Groups[int(csap)].getSumOfExercises()) + ". feladat",
                                          self)
        self.exerciseNumber.setAlignment(QtCore.Qt.AlignCenter)

        self.solution = createLabel(40, 220, 220, 20, "", self)
        self.solution.setAlignment(QtCore.Qt.AlignCenter)

        self.solution2 = createLabel(40, 240, 220, 40, "", self)
        self.solution2.setAlignment(QtCore.Qt.AlignCenter)

        self.additinaldatal = createLabel(40, 320, 220, 40, "Bemondott válasz:", self)
        self.additinaldatale = createLineEdit(40, 360, 220, 40, self)

        if (len(logic.Solution) == 0 or logic.Solution[logic.Groups[int(csap)].numOfExercise - 1] == ""):
            self.solution.setText("Nincs megoldás feltöltve!")
            self.solution2.setText("Nézze meg a papíron!")

        else:
            self.solution.setText("Megoldás:")
            self.solution2.setText(logic.Solution[logic.Groups[int(csap)].getSumOfExercises() - 1])
            self.solution2.setStyleSheet("background-color: white")

        self.pushbutton_right = createPushButton(40, 440, 90, 40, "JÓ", partial(self.rightmegoldas, csap), self)
        self.pushbutton_right.setStyleSheet("background-color: green")
        self.pushbutton_rossz = createPushButton(170, 440, 90, 40, "ROSSZ", partial(self.rosszmegoldas, csap), self)
        self.pushbutton_rossz.setStyleSheet("background-color: red")

    def rightmegoldas(self, csap):
        self.close()
        logic.Groups[csap].exercises[logic.Groups[csap].numOfExercise - 1].newSolution(True)
        if (self.additinaldatale.text() == ""):
            logic.Groups[csap].exercises[logic.Groups[csap].numOfExercise - 1].additionalDatas += "- ; "
        else:
            logic.Groups[csap].exercises[logic.Groups[csap].numOfExercise - 1].additionalDatas += self.additinaldatale.text() + " ; "
        logic.Groups[csap].numOfExercise += 1
        logic.writeGroupDataToFile()
        logic.WriteAdditionalDatasToFile()
        logic.refreshPoints()
        feladat = logic.Groups[int(csap)].getSumOfExercises()
        if (feladat == 6 or feladat == 10 or feladat == 13 or feladat == 15 or feladat == 16):
            self.blokkv = BlockEnd(csap)
            self.blokkv.show()
        else:
            self.mb = createMessageBox(200, 380, 100, 60, str(csap + 1) + ". csapat",
                                       "A következő feladat száma: " + str(logic.Groups[int(csap)].getSumOfExercises()),
                                       QMessageBox.Ok, self)

    def rosszmegoldas(self, csap):
        logic.Groups[csap].exercises[logic.Groups[csap].numOfExercise - 1].newSolution(False)
        if (self.additinaldatale.text() == ""):
            logic.Groups[csap].exercises[logic.Groups[csap].numOfExercise - 1].additionalDatas += "- ; "
        else:
            logic.Groups[csap].exercises[logic.Groups[csap].numOfExercise - 1].additionalDatas += self.additinaldatale.text() + " ; "

        logic.Groups[csap].numOfExercise += 1
        logic.writeGroupDataToFile()
        logic.WriteAdditionalDatasToFile()
        logic.refreshPoints()
        self.close()
        feladat = logic.Groups[int(csap)].getSumOfExercises()
        if (feladat == 6 or feladat == 10 or feladat == 13 or feladat == 15 or feladat == 16):
            self.blokkv = BlockEnd(csap)
            self.blokkv.show()
        else:
            self.mb = createMessageBox(200, 380, 100, 60, str(csap + 1) + ". csapat",
                                       "A következő feladat száma: " + str(logic.Groups[int(csap)].getSumOfExercises()),
                                       QMessageBox.Ok, self)

