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
			groupButtons.append(createPushButton(40 + 88*(i - i//5*5), 40 + 60 * (i//5), 68, 40, str(i+1), partial(self.javit, i),self))


	def javit(self, i):
		self.javitas = Correction(i+1)
		self.javitas.show()
		self.close()

class Correction(QWidget):
	def __init__(self, csap):
		tabor, csoport = logic.Infos.camp, logic.Infos.age
		super(Correction, self).__init__()
		self.setGeometry(800, 100, 300, 720)
		self.setStyleSheet("background-color: lightpink")
		self.setWindowTitle("Javítás: " + str(csap) + ". csapat")
		self.initUI(csap)

	def initUI(self, csap):
		labels = []
		lineEdits = []

		for i in range(0, 15):
			labels.append(createLabel(20, 20 + 40*i , 100, 30, str(i+1) + ".", self))
			lineEdits.append(createLineEdit(140, 20 + 40*i, 140, 30, self))
			lineEdits[i].setStyleSheet("background-color: white")
			lineEdits[i].setText(str(logic.Groups[int(csap)-1].getNthExercise(i).getConcatenatedForm()))

		self.exerciseNumberL = createLabel(20, 20 + 600, 100, 30, "Feladat: ", self)
		labels.append(self.exerciseNumberL)
		self.exerciseNumberLE = createLineEdit(140, 20 + 600, 140, 30, self)
		self.exerciseNumberLE.setStyleSheet("background-color: white")
		self.exerciseNumberLE.setText(str(logic.Groups[int(csap)-1].getSumOfExercises()))
		lineEdits.append(self.exerciseNumberLE)


		self.okbutton = createPushButton(20, 670, 260, 30, "OK", partial(self.correctdone, csap, lineEdits), self)

	def correctdone(self, csap, lineEdits):
		groupNow = logic.Groups[int(csap)-1]
		for i in range(0, 15):
			groupNow.exercises[i].results = lineEdits[i].text()
		groupNow.numOfExercise = int(self.exerciseNumberLE.text())
		logic.writeGroupDataToFile()
		self.close()
		logic.refreshPoints()