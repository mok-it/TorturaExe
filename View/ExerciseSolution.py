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

        self.group_number = createLabel(40, 40, 220, 20, str(csap + 1) + ". csapat", self)
        self.group_number.setAlignment(QtCore.Qt.AlignCenter)

        group_names = []
        sz = 0
        for i in logic.Groups[csap].members:
            tag = createLabel(40, 80 + 20 * sz, 220, 20, i, self)
            tag.setAlignment(QtCore.Qt.AlignCenter)
            group_names.append(tag)
            sz += 1

        self.exercise_number = createLabel(40, 180, 220, 40, str(logic.Groups[int(csap)].getSumOfExercises()) + ". feladat",
                                           self)
        self.exercise_number.setAlignment(QtCore.Qt.AlignCenter)

        self.solution = createLabel(40, 220, 220, 20, "", self)
        self.solution.setAlignment(QtCore.Qt.AlignCenter)

        self.solution2 = createLabel(40, 240, 220, 40, "", self)
        self.solution2.setAlignment(QtCore.Qt.AlignCenter)

        self.additinal_datal = createLabel(40, 320, 220, 40, "Bemondott válasz:", self)
        self.additinal_datale = createLineEdit(40, 360, 220, 40, self)

        if (len(logic.Solution) == 0 or logic.Solution[logic.Groups[int(csap)].numOfExercise - 1] == ""):
            self.solution.setText("Nincs megoldás feltöltve!")
            self.solution2.setText("Nézze meg a papíron!")

        else:
            self.solution.setText("Megoldás:")
            self.solution2.setText(logic.Solution[logic.Groups[int(csap)].getSumOfExercises() - 1])
            self.solution2.setStyleSheet("background-color: white")

        self.pushbutton_right = createPushButton(40, 440, 90, 40, "JÓ", partial(self.rightSolution, csap), self)
        self.pushbutton_right.setStyleSheet("background-color: green")
        self.pushbutton_wrong = createPushButton(170, 440, 90, 40, "ROSSZ", partial(self.wrongSolution, csap), self)
        self.pushbutton_wrong.setStyleSheet("background-color: red")

    def rightSolution(self, team):
        self.close()
        logic.Groups[team].exercises[logic.Groups[team].numOfExercise - 1].newSolution(True)
        if (self.additinal_datale.text() == ""):
            logic.Groups[team].exercises[logic.Groups[team].numOfExercise - 1].additionalDatas += "- ; "
        else:
            logic.Groups[team].exercises[logic.Groups[team].numOfExercise - 1].additionalDatas += self.additinal_datale.text() + " ; "
        logic.Groups[team].numOfExercise += 1
        logic.writeGroupDataToFile()
        logic.WriteAdditionalDatasToFile()
        logic.refreshPoints()
        exercise = logic.Groups[int(team)].getSumOfExercises()
        if (exercise == 6 or exercise == 10 or exercise == 13 or exercise == 15 or exercise == 16):
            self.blokkv = BlockEnd(team)
            self.blokkv.show()
        else:
            self.mb = createMessageBox(200, 380, 100, 60, str(team + 1) + ". csapat",
                                       "A következő feladat száma: " + str(logic.Groups[int(team)].getSumOfExercises()),
                                       QMessageBox.Ok, self)

    def wrongSolution(self, csap):
        logic.Groups[csap].exercises[logic.Groups[csap].numOfExercise - 1].newSolution(False)
        if (self.additinal_datale.text() == ""):
            logic.Groups[csap].exercises[logic.Groups[csap].numOfExercise - 1].additionalDatas += "- ; "
        else:
            logic.Groups[csap].exercises[logic.Groups[csap].numOfExercise - 1].additionalDatas += self.additinal_datale.text() + " ; "

        logic.Groups[csap].numOfExercise += 1
        logic.writeGroupDataToFile()
        logic.WriteAdditionalDatasToFile()
        logic.refreshPoints()
        self.close()
        exercise = logic.Groups[int(csap)].getSumOfExercises()
        if (exercise == 6 or exercise == 10 or exercise == 13 or exercise == 15 or exercise == 16):
            self.blokkv = BlockEnd(csap)
            self.blokkv.show()
        else:
            self.mb = createMessageBox(200, 380, 100, 60, str(csap + 1) + ". csapat",
                                       "A következő feladat száma: " + str(logic.Groups[int(csap)].getSumOfExercises()),
                                       QMessageBox.Ok, self)

