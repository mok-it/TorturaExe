from functools import partial
from View.QtFunctions import *
from Model.Logic import *


class FixSolutions(QWidget):
	def __init__(self):
		tabor, csoport = logic.Infos.camp, logic.Infos.age
		super(FixSolutions, self).__init__()
		numGr = len(logic.Groups)-1
		self.setGeometry(800, 100, 500, 120 + 60 * (numGr//5))
		self.setStyleSheet("background-color: lightpink")
		self.setWindowTitle(tabor + " - " + csoport + " csoport")
		self.initUI()

	def initUI(self):

		numGr = len(logic.Groups)-1
		groupButtons = []
		for i in range(0, len(logic.Groups)):
			groupButtons.append(createPushButton(40 + 88 * (i - i//5*5), 40 + 60 * (i//5), 68, 40, str(i+1), partial(self.fix, i), self))


	def fix(self, i):
		self.javitas = correction(i + 1)
		self.javitas.show()
		self.close()

class correction(QWidget):
	def __init__(self, team):
		camp, group = logic.Infos.camp, logic.Infos.age
		super(correction, self).__init__()
		self.setGeometry(800, 100, 300, 720)
		self.setStyleSheet("background-color: lightpink")
		self.setWindowTitle("Javítás: " + str(team) + ". csapat")
		self.initUI(team)

	def initUI(self, team):
		labels = []
		lineEdits = []

		for i in range(0, 15):
			labels.append(createLabel(20, 20 + 40*i , 100, 30, str(i+1) + ".", self))
			lineEdits.append(createLineEdit(140, 20 + 40*i, 140, 30, self))
			lineEdits[i].setStyleSheet("background-color: white")
			lineEdits[i].setText(str(logic.Groups[int(team) - 1].getNthExercise(i).getConcatenatedForm()))

		self.exercise_numberL = createLabel(20, 20 + 600, 100, 30, "Feladat: ", self)
		labels.append(self.exercise_numberL)
		self.exerciseNumberLE = createLineEdit(140, 20 + 600, 140, 30, self)
		self.exerciseNumberLE.setStyleSheet("background-color: white")
		self.exerciseNumberLE.setText(str(logic.Groups[int(team) - 1].getSumOfExercises()))
		lineEdits.append(self.exerciseNumberLE)


		self.ok_button = createPushButton(20, 670, 260, 30, "OK", partial(self.correctDone, team, lineEdits), self)

	def correctDone(self, csap, lineEdits):
		group_now = logic.Groups[int(csap)-1]
		for i in range(0, 15):
			group_now.exercises[i].results = lineEdits[i].text()
		group_now.numOfExercise = int(self.exerciseNumberLE.text())
		logic.writeGroupDataToFile()
		self.close()
		logic.refreshPoints()