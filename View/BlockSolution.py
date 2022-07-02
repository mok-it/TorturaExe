from functools import partial
from PyQt5 import QtCore
from Model.Logic import logic
from View.QtFunctions import *


#import windows


class Blokkbemond(QWidget):
	def __init__(self, csap, feladat, conc, adddatas):
		super(Blokkbemond, self).__init__()
		self.setGeometry(100,100,300,520)
		self.setWindowModality(QtCore.Qt.ApplicationModal)
		self.setStyleSheet("background-color: lightblue")
		self.setWindowTitle(str(csap+1) + " - " + str(logic.Groups[int(csap)].getSumOfExercises()+feladat) + ". feladat")
		self.initUI(csap, feladat, conc, adddatas)

	def initUI(self, csap, feladat, conc, adddatas):
		conc[feladat] = ""

		self.groupNumber = createLabel(40, 40, 220, 20, str(csap + 1) + ". csapat", self)
		self.groupNumber.setAlignment(QtCore.Qt.AlignCenter)

		groupnames = []
		sz = 0
		for i in logic.Groups[csap].members:
			tag = createLabel(40, 80 + 20 * sz, 220, 20, i, self)
			tag.setAlignment(QtCore.Qt.AlignCenter)
			groupnames.append(tag)
			sz += 1

		self.exerciseNumber = createLabel(40, 180, 220, 40, str(logic.Groups[int(csap)].getSumOfExercises()) + ". feladat", self)
		self.exerciseNumber.setAlignment(QtCore.Qt.AlignCenter)

		self.solution = createLabel(40, 220, 220, 20, "", self)
		self.solution.setAlignment(QtCore.Qt.AlignCenter)

		self.solution2 = createLabel(40, 240, 220, 40, "", self)
		self.solution2.setAlignment(QtCore.Qt.AlignCenter)

		self.additinaldatal = createLabel(40, 320, 220, 40, "Bemondott válasz:", self)
		self.additinaldatale = createLineEdit(40, 360, 220, 40, self)

		if (len(logic.Solution) == 0 or logic.Solution[logic.Groups[int(csap)].numOfExercise-1+feladat] == "" ):
			self.solution.setText("Nincs megoldás feltöltve!")
			self.solution2.setText("Nézze meg a papíron!")

		else:
			self.solution.setText("Megoldás:")
			self.solution2.setText(logic.Solution[logic.Groups[int(csap)].getSumOfExercises()+feladat-1])
			self.solution2.setStyleSheet("background-color: white")

		self.pushbutton_jo = createPushButton(40, 440, 90, 40, "JÓ", partial(self.jomegoldas, csap, feladat, conc, adddatas), self)
		self.pushbutton_jo.setStyleSheet("background-color: green")
		self.pushbutton_rossz = createPushButton(170, 440, 90, 40, "ROSSZ", partial(self.rosszmegoldas, csap, feladat, conc, adddatas), self)
		self.pushbutton_rossz.setStyleSheet("background-color: red")

	def jomegoldas(self, csap, feladat, conc, adddatas):
		self.close()
		conc[feladat] = "1"
		if (self.additinaldatale.text() == ""):
			adddatas[feladat] = "-"
		else:
			adddatas[feladat] = self.additinaldatale.text()



	def rosszmegoldas(self, csap, feladat, conc, adddatas):
		self.close()

		conc[feladat] = "0"

		if (self.additinaldatale.text() == ""):
			adddatas[feladat] = "-"
		else:
			adddatas[feladat] = self.additinaldatale.text()
