from functools import partial
from PyQt5 import QtCore
from Model.Logic import logic
from View.QtFunctions import *


#import windows


class answerTheBlock(QWidget):
	def __init__(self, team, exercise, conc, add_datas):
		super(answerTheBlock, self).__init__()
		self.setGeometry(100,100,300,520)
		self.setWindowModality(QtCore.Qt.ApplicationModal)
		self.setStyleSheet("background-color: lightblue")
		self.setWindowTitle(str(team + 1) + " - " + str(logic.Groups[int(team)].getSumOfExercises() + exercise) + ". feladat")
		self.initUI(team, exercise, conc, add_datas)

	def initUI(self, team, exercise, conc, add_datas):
		conc[exercise] = ""

		self.group_number = createLabel(40, 40, 220, 20, str(team + 1) + ". csapat", self)
		self.group_number.setAlignment(QtCore.Qt.AlignCenter)

		group_names = []
		sz = 0
		for i in logic.Groups[team].members:
			tag = createLabel(40, 80 + 20 * sz, 220, 20, i, self)
			tag.setAlignment(QtCore.Qt.AlignCenter)
			group_names.append(tag)
			sz += 1

		self.exercise_number = createLabel(40, 180, 220, 40, str(logic.Groups[int(team)].getSumOfExercises()) + ". feladat", self)
		self.exercise_number.setAlignment(QtCore.Qt.AlignCenter)

		self.solution = createLabel(40, 220, 220, 20, "", self)
		self.solution.setAlignment(QtCore.Qt.AlignCenter)

		self.solution2 = createLabel(40, 240, 220, 40, "", self)
		self.solution2.setAlignment(QtCore.Qt.AlignCenter)

		self.additinal_datal = createLabel(40, 320, 220, 40, "Bemondott válasz:", self)
		self.additinaldatale = createLineEdit(40, 360, 220, 40, self)	#ez mi?

		if (len(logic.Solution) == 0 or logic.Solution[logic.Groups[int(team)].numOfExercise - 1 + exercise] == ""):
			self.solution.setText("Nincs megoldás feltöltve!")
			self.solution2.setText("Nézze meg a papíron!")

		else:
			self.solution.setText("Megoldás:")
			self.solution2.setText(logic.Solution[logic.Groups[int(team)].getSumOfExercises() + exercise - 1])
			self.solution2.setStyleSheet("background-color: white")

		self.pushbutton_right = createPushButton(40, 440, 90, 40, "JÓ", partial(self.rightSolution, team, exercise, conc, add_datas), self)
		self.pushbutton_right.setStyleSheet("background-color: green")
		self.pushbutton_wrong = createPushButton(170, 440, 90, 40, "ROSSZ", partial(self.wrongSolution, team, exercise, conc, add_datas), self)
		self.pushbutton_wrong.setStyleSheet("background-color: red")

	def rightSolution(self, team, exercise, conc, add_datas):
		self.close()
		conc[exercise] = "1"
		if (self.additinaldatale.text() == ""):
			add_datas[exercise] = "-"
		else:
			add_datas[exercise] = self.additinaldatale.text()



	def wrongSolution(self, eercise, conc, add_datas):
		self.close()

		conc[eercise] = "0"

		if (self.additinaldatale.text() == ""):
			add_datas[eercise] = "-"
		else:
			add_datas[eercise] = self.additinaldatale.text()
