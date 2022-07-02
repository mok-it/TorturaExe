# import windows
from View.BlockEnd import *
from View.BlockSolution import *


class BlockRepeat(QWidget):
    def __init__(self, csap):
        super(BlockRepeat, self).__init__()
        blockLength = logic.getBlockLength(csap)

        self.setGeometry(100, 100, 560, (200 + (blockLength) * 80))
        self.setStyleSheet("background-color: lightblue")
        minlength = 100
        for i in range(logic.Groups[csap].getSumOfExercises(), logic.Groups[csap].getSumOfExercises() + blockLength + 1):
            if (minlength > logic.Groups[csap].getNthExercise(i - 1).getNumOfAnswers()):
                minlength = logic.Groups[csap].getNthExercise(i - 1).getNumOfAnswers()
        self.setWindowTitle(str(csap + 1) + ". csapat - " + str(minlength + 1) + ". próbálkozás")
        self.initUI(csap, blockLength)

    def initUI(self, csap, blockLength):

        conc = ["", "", "", "", ""]
        adddatas = ["", "", "", "", ""]

        maxlength = 0
        for i in range(logic.Groups[csap].numOfExercise, logic.Groups[csap].numOfExercise + blockLength + 1):
            if (maxlength < len(logic.Groups[csap].exercises[i - 1].results)):
                maxlength = len(logic.Groups[csap].exercises[i - 1].results)
        tr = True
        for i in range(logic.Groups[csap].numOfExercise, logic.Groups[csap].numOfExercise + blockLength + 1):
            if (maxlength > len(logic.Groups[csap].exercises[i - 1].results)):
                tr = False

        self.label11 = createLabel(40, 40, 220, 40, "", self)
        if (maxlength > logic.Groups[csap].getActualExercise().getNumOfAnswers() or tr):

            if (logic.Groups[csap].getActualExercise().getLastAnswer() == "1"):
                self.label11.setText(str(logic.Groups[csap].getSumOfExercises()) + ". feladat \tJÓ")
            else:
                self.label11.setText(str(logic.Groups[csap].getSumOfExercises()) + ". feladat \tROSSZ")

            self.button11 = createPushButton(280, 40, 120, 40, "MARAD",
                                             partial(self.buttonfunc11, csap, conc, adddatas), self)
            self.button12 = createPushButton(420, 40, 120, 40, "ÚJ VÁLASZ",
                                             partial(self.buttonfunc12, csap, conc, adddatas), self)

        else:
            if (logic.Groups[csap].getActualExercise().getLLastAnswer() == "1"):
                self.label11.setText(str(logic.Groups[csap].getSumOfExercises()) + ". feladat \tJÓ")
            else:
                self.label11.setText(str(logic.Groups[csap].getSumOfExercises()) + ". feladat \tROSSZ")

            self.label12 = createLabel(280, 40, 260, 40, "", self)
            self.label12.setAlignment(QtCore.Qt.AlignCenter)

            if (logic.Groups[csap].getActualExercise().getLastAnswer() == "1"):
                self.label12.setText("JÓ")
                self.label12.setStyleSheet("background-color: green")
            else:
                self.label12.setText("ROSSZ")
                self.label12.setStyleSheet("background-color: red")

        self.okbutton = createPushButton(20, 120 + (blockLength) * 80, 520, 40, "OK",
                                         partial(self.blokkok, csap, blockLength, conc, adddatas), self)

        if (logic.Groups[csap].numOfExercise <= 13):

            self.label21 = createLabel(40, 120, 220, 40, "", self)

            if (maxlength > logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises()).getNumOfAnswers() or tr):

                if (logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises()).getLastAnswer() == "1"):
                    self.label21.setText(str(logic.Groups[csap].getSumOfExercises() + 1) + ". feladat \tJÓ")
                else:
                    self.label21.setText(str(logic.Groups[csap].getSumOfExercises() + 1) + ". feladat \tROSSZ")

                self.button21 = createPushButton(280, 120, 120, 40, "MARAD",
                                                 partial(self.buttonfunc21, csap, conc, adddatas), self)
                self.button22 = createPushButton(420, 120, 120, 40, "ÚJ VÁLASZ",
                                                 partial(self.buttonfunc22, csap, conc, adddatas), self)

            else:
                if (logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises()).getLLastAnswer() == "1"):
                    self.label21.setText(str(logic.Groups[csap].getSumOfExercises() + 1) + ". feladat \tJÓ")
                else:
                    self.label21.setText(str(logic.Groups[csap].getSumOfExercises() + 1) + ". feladat \tROSSZ")

                self.label22 = createLabel(280, 120, 260, 40, "", self)
                self.label22.setAlignment(QtCore.Qt.AlignCenter)

                if (logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises()).getLastAnswer() == "1"):
                    self.label22.setText("JÓ")
                    self.label22.setStyleSheet("background-color: green")
                else:
                    self.label22.setText("ROSSZ")
                    self.label22.setStyleSheet("background-color: red")

        if (logic.Groups[csap].numOfExercise <= 10):

            self.label31 = createLabel(40, 200, 220, 40, "", self)

            if (maxlength > logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises() + 1).getNumOfAnswers() or tr):

                if (logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises() + 1).getLastAnswer() == "1"):
                    self.label31.setText(str(logic.Groups[csap].getSumOfExercises() + 2) + ". feladat \tJÓ")
                else:
                    self.label31.setText(str(logic.Groups[csap].getSumOfExercises() + 2) + ". feladat \tROSSZ")

                self.button31 = createPushButton(280, 200, 120, 40, "MARAD",
                                                 partial(self.buttonfunc31, csap, conc, adddatas), self)
                self.button32 = createPushButton(420, 200, 120, 40, "ÚJ VÁLASZ",
                                                 partial(self.buttonfunc32, csap, conc, adddatas), self)

            else:
                if (logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises() + 1).getLLastAnswer() == "1"):
                    self.label31.setText(str(logic.Groups[csap].getSumOfExercises() + 2) + ". feladat \tJÓ")
                else:
                    self.label31.setText(str(logic.Groups[csap].getSumOfExercises() + 2) + ". feladat \tROSSZ")

                self.label32 = createLabel(280, 200, 260, 40, "", self)
                self.label32.setAlignment(QtCore.Qt.AlignCenter)

                if (logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises() + 1).getLastAnswer() == "1"):
                    self.label32.setText("JÓ")
                    self.label32.setStyleSheet("background-color: green")
                else:
                    self.label32.setText("ROSSZ")
                    self.label32.setStyleSheet("background-color: red")

        if (logic.Groups[csap].numOfExercise <= 6):

            self.label41 = createLabel(40, 280, 220, 40, "", self)

            if (maxlength > logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises() + 2).getNumOfAnswers() or tr):

                if (logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises() + 2).getLastAnswer() == "1"):
                    self.label41.setText(str(logic.Groups[csap].getSumOfExercises() + 3) + ". feladat \tJÓ")
                else:
                    self.label41.setText(str(logic.Groups[csap].getSumOfExercises() + 3) + ". feladat \tROSSZ")

                self.button41 = createPushButton(280, 280, 120, 40, "MARAD",
                                                 partial(self.buttonfunc41, csap, conc, adddatas), self)
                self.button42 = createPushButton(420, 280, 120, 40, "ÚJ VÁLASZ",
                                                 partial(self.buttonfunc42, csap, conc, adddatas), self)

            else:
                if (logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises() + 2).getLLastAnswer() == "1"):
                    self.label41.setText(str(logic.Groups[csap].getSumOfExercises() + 3) + ". feladat \tJÓ")
                else:
                    self.label41.setText(str(logic.Groups[csap].getSumOfExercises() + 3) + ". feladat \tROSSZ")

                self.label42 = createLabel(280, 280, 260, 40, "", self)
                self.label42.setAlignment(QtCore.Qt.AlignCenter)

                if (logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises() + 2).getLastAnswer() == "1"):
                    self.label42.setText("JÓ")
                    self.label42.setStyleSheet("background-color: green")
                else:
                    self.label42.setText("ROSSZ")
                    self.label42.setStyleSheet("background-color: red")

        if (logic.Groups[csap].numOfExercise == 1):

            self.label51 = createLabel(40, 360, 220, 40, "", self)

            if (maxlength > logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises() + 3).getNumOfAnswers() or tr):

                if (logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises() + 3).getLastAnswer() == "1"):
                    self.label51.setText(str(logic.Groups[csap].getSumOfExercises() + 4) + ". feladat \tJÓ")
                else:
                    self.label51.setText(str(logic.Groups[csap].getSumOfExercises() + 4) + ". feladat \tROSSZ")

                self.button51 = createPushButton(280, 360, 120, 40, "MARAD",
                                                 partial(self.buttonfunc51, csap, conc, adddatas), self)
                self.button52 = createPushButton(420, 360, 120, 40, "ÚJ VÁLASZ",
                                                 partial(self.buttonfunc52, csap, conc, adddatas), self)

            else:
                if (logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises() + 3).getLLastAnswer() == "1"):
                    self.label51.setText(str(logic.Groups[csap].getSumOfExercises() + 4) + ". feladat \tJÓ")
                else:
                    self.label51.setText(str(logic.Groups[csap].getSumOfExercises() + 4) + ". feladat \tROSSZ")

                self.label52 = createLabel(280, 360, 260, 40, "", self)
                self.label52.setAlignment(QtCore.Qt.AlignCenter)

                if (logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises() + 3).getLastAnswer() == "1"):
                    self.label52.setText("JÓ")
                    self.label52.setStyleSheet("background-color: green")
                else:
                    self.label52.setText("ROSSZ")
                    self.label2.setStyleSheet("background-color: red")

    def buttonfunc11(self, csap, conc, adddatas):
        if (logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises() - 1).getLastAnswer() == "1"):
            conc[0] = "1"
        else:
            conc[0] = "0"
        answer = logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises() - 1).additionalDatas.split(" ; ")
        lastans = answer[len(answer) - 2]
        adddatas[0] = lastans

        self.button11 = createPushButton(280, 40, 120, 40, "MARAD", partial(self.buttonfunc11, csap, conc, adddatas),
                                         self)
        self.button11.setStyleSheet("QPushButton { background-color: green }")
        self.button11.show()

        self.button12 = createPushButton(420, 40, 120, 40, "ÚJ VÁLASZ",
                                         partial(self.buttonfunc12, csap, conc, adddatas), self)
        self.button12.setStyleSheet("QPushButton { background-color: lightgray }")
        self.button12.show()

    def buttonfunc12(self, csap, conc, adddatas):

        self.button11 = createPushButton(280, 40, 120, 40, "MARAD", partial(self.buttonfunc11, csap, conc, adddatas),
                                         self)
        self.button11.setStyleSheet("QPushButton { background-color: lightgray }")
        self.button11.show()

        self.button12 = createPushButton(420, 40, 120, 40, "ÚJ VÁLASZ",
                                         partial(self.buttonfunc12, csap, conc, adddatas), self)
        self.button12.setStyleSheet("QPushButton { background-color: green }")
        self.button12.show()

        self.buttonf = Blokkbemond(csap, 0, conc, adddatas)
        self.buttonf.show()

    def buttonfunc21(self, csap, conc, adddatas):
        if (logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises()).getLastAnswer() == "1"):
            conc[1] = "1"
        else:
            conc[1] = "0"
        answer = logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises()).additionalDatas.split(" ; ")
        lastans = answer[len(answer) - 2]
        adddatas[1] = lastans

        self.button21 = createPushButton(280, 120, 120, 40, "MARAD", partial(self.buttonfunc21, csap, conc, adddatas),
                                         self)
        self.button21.setStyleSheet("QPushButton { background-color: green }")
        self.button21.show()

        self.button22 = createPushButton(420, 120, 120, 40, "ÚJ VÁLASZ",
                                         partial(self.buttonfunc22, csap, conc, adddatas), self)
        self.button22.setStyleSheet("QPushButton { background-color: lightgray }")
        self.button22.show()

    def buttonfunc22(self, csap, conc, adddatas):

        self.button21 = createPushButton(280, 120, 120, 40, "MARAD", partial(self.buttonfunc21, csap, conc, adddatas),
                                         self)
        self.button21.setStyleSheet("QPushButton { background-color: lightgray }")
        self.button21.show()

        self.button22 = createPushButton(420, 120, 120, 40, "ÚJ VÁLASZ",
                                         partial(self.buttonfunc22, csap, conc, adddatas), self)
        self.button22.setStyleSheet("QPushButton { background-color: green }")
        self.button22.show()

        self.buttonf = Blokkbemond(csap, 1, conc, adddatas)
        self.buttonf.show()

    def buttonfunc31(self, csap, conc, adddatas):
        if (logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises() + 1).getLastAnswer() == "1"):
            conc[2] = "1"
        else:
            conc[2] = "0"
        answer = logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises() + 1).additionalDatas.split(" ; ")
        lastans = answer[len(answer) - 2]
        adddatas[2] = lastans

        self.button31 = createPushButton(280, 200, 120, 40, "MARAD", partial(self.buttonfunc31, csap, conc, adddatas),
                                         self)
        self.button31.setStyleSheet("QPushButton { background-color: green }")
        self.button31.show()

        self.button32 = createPushButton(420, 200, 120, 40, "ÚJ VÁLASZ",
                                         partial(self.buttonfunc32, csap, conc, adddatas), self)
        self.button32.setStyleSheet("QPushButton { background-color: lightgray }")
        self.button32.show()

    def buttonfunc32(self, csap, conc, adddatas):

        self.button31 = createPushButton(280, 200, 120, 40, "MARAD", partial(self.buttonfunc31, csap, conc, adddatas),
                                         self)
        self.button31.setStyleSheet("QPushButton { background-color: lightgray }")
        self.button31.show()

        self.button32 = createPushButton(420, 200, 120, 40, "ÚJ VÁLASZ",
                                         partial(self.buttonfunc32, csap, conc, adddatas), self)
        self.button32.setStyleSheet("QPushButton { background-color: green }")
        self.button32.show()

        self.buttonf = Blokkbemond(csap, 2, conc, adddatas)
        self.buttonf.show()

    def buttonfunc41(self, csap, conc, adddatas):
        if (logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises() + 2).getLastAnswer() == "1"):
            conc[3] = "1"
        else:
            conc[3] = "0"
        answer = logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises() + 2).additionalDatas.split(" ; ")
        lastans = answer[len(answer) - 2]
        adddatas[3] = lastans

        self.button41 = createPushButton(280, 280, 120, 40, "MARAD", partial(self.buttonfunc41, csap, conc, adddatas),
                                         self)
        self.button41.setStyleSheet("QPushButton { background-color: green }")
        self.button41.show()

        self.button42 = createPushButton(420, 280, 120, 40, "ÚJ VÁLASZ",
                                         partial(self.buttonfunc42, csap, conc, adddatas), self)
        self.button42.setStyleSheet("QPushButton { background-color: lightgray }")
        self.button42.show()

    def buttonfunc42(self, csap, conc, adddatas):

        self.button41 = createPushButton(280, 280, 120, 40, "MARAD", partial(self.buttonfunc41, csap, conc, adddatas),
                                         self)
        self.button41.setStyleSheet("QPushButton { background-color: lightgray }")
        self.button41.show()

        self.button42 = createPushButton(420, 280, 120, 40, "ÚJ VÁLASZ",
                                         partial(self.buttonfunc42, csap, conc, adddatas), self)
        self.button42.setStyleSheet("QPushButton { background-color: green }")
        self.button42.show()

        self.buttonf = Blokkbemond(csap, 3, conc, adddatas)
        self.buttonf.show()

    def buttonfunc51(self, csap, conc, adddatas):
        if (logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises() + 3).getLastAnswer() == "1"):
            conc[4] = "1"
        else:
            conc[4] = "0"
        answer = logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises() + 3).additionalDatas.split(" ; ")
        lastans = answer[len(answer) - 2]
        adddatas[4] = lastans

        self.button51 = createPushButton(280, 360, 120, 40, "MARAD", partial(self.buttonfunc51, csap, conc, adddatas),
                                         self)
        self.button51.setStyleSheet("QPushButton { background-color: green }")
        self.button51.show()

        self.button52 = createPushButton(420, 360, 120, 40, "ÚJ VÁLASZ",
                                         partial(self.buttonfunc52, csap, conc, adddatas), self)
        self.button52.setStyleSheet("QPushButton { background-color: lightgray }")
        self.button52.show()

    def buttonfunc52(self, csap, conc, adddatas):

        self.button51 = createPushButton(280, 360, 120, 40, "MARAD", partial(self.buttonfunc51, csap, conc, adddatas),
                                         self)
        self.button51.setStyleSheet("QPushButton { background-color: lightgray }")
        self.button51.show()

        self.button52 = createPushButton(420, 360, 120, 40, "ÚJ VÁLASZ",
                                         partial(self.buttonfunc52, csap, conc, adddatas), self)
        self.button52.setStyleSheet("QPushButton { background-color: green }")
        self.button52.show()

        self.buttonf = Blokkbemond(csap, 4, conc, adddatas)
        self.buttonf.show()

    def blokkok(self, csap, blockLength, conc, adddatas):
        self.close()
        for i in range(0, blockLength + 1):
            if conc[i] != "":
                if conc[i] == "1":
                    logic.Groups[csap].exercises[logic.Groups[csap].numOfExercise + i - 1].newSolution(True)
                else:
                    logic.Groups[csap].exercises[logic.Groups[csap].numOfExercise + i - 1].newSolution(False)
            if (adddatas[i] != ""):
                logic.Groups[csap].exercises[logic.Groups[csap].numOfExercise + i - 1].additionalDatas += adddatas[i] + " ; "

        logic.writeGroupDataToFile()
        logic.WriteAdditionalDatasToFile()

        logic.refreshPoints()
        maxlength = 0
        for i in range(logic.Groups[csap].numOfExercise, logic.Groups[csap].numOfExercise + blockLength + 1):
            if (maxlength < len(logic.Groups[csap].exercises[i - 1].results)):
                maxlength = len(logic.Groups[csap].exercises[i - 1].results)
        tr = True
        for i in range(logic.Groups[csap].numOfExercise, logic.Groups[csap].numOfExercise + blockLength + 1):
            if (maxlength > len(logic.Groups[csap].exercises[i - 1].results)):
                tr = False
        trr = False
        for i in conc:
            if i == "1" or i == "0":
                trr = True
        if (trr and tr):
            logic.Groups[csap].numOfExercise = logic.Groups[csap].numOfExercise + blockLength + 1
            self.blokkv = BlockEnd(csap)
            self.blokkv.show()

