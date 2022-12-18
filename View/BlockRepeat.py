# import windows
from View.BlockEnd import *
from View.BlockSolution import *


class BlockRepeat(QWidget):
    def __init__(self, csap):
        super(BlockRepeat, self).__init__()
        blockLength = logic.getBlockLength(csap)

        self.setGeometry(100, 100, 560, (200 + (blockLength) * 80))
        self.setStyleSheet("background-color: lightblue")
        min_length = 100
        for i in range(logic.Groups[csap].getSumOfExercises(), logic.Groups[csap].getSumOfExercises() + blockLength + 1):
            if (min_length > logic.Groups[csap].getNthExercise(i - 1).getNumOfAnswers()):
                min_length = logic.Groups[csap].getNthExercise(i - 1).getNumOfAnswers()
        self.setWindowTitle(str(csap + 1) + ". csapat - " + str(min_length + 1) + ". próbálkozás")
        self.initUI(csap, blockLength)

    def initUI(self, team, block_length):

        conc = ["", "", "", "", ""]
        add_datas = ["", "", "", "", ""]

        max_length = 0
        for i in range(logic.Groups[team].numOfExercise, logic.Groups[team].numOfExercise + block_length + 1):
            if (max_length < len(logic.Groups[team].exercises[i - 1].results)):
                max_length = len(logic.Groups[team].exercises[i - 1].results)
        tr = True
        for i in range(logic.Groups[team].numOfExercise, logic.Groups[team].numOfExercise + block_length + 1):
            if (max_length > len(logic.Groups[team].exercises[i - 1].results)):
                tr = False

        self.label11 = createLabel(40, 40, 220, 40, "", self)
        if (max_length > logic.Groups[team].getActualExercise().getNumOfAnswers() or tr):

            if (logic.Groups[team].getActualExercise().getLastAnswer() == "1"):
                self.label11.setText(str(logic.Groups[team].getSumOfExercises()) + ". feladat \tJÓ")
            else:
                self.label11.setText(str(logic.Groups[team].getSumOfExercises()) + ". feladat \tROSSZ")

            self.button11 = createPushButton(280, 40, 120, 40, "MARAD",
                                             partial(self.buttonFunc11, team, conc, add_datas), self)
            self.button12 = createPushButton(420, 40, 120, 40, "ÚJ VÁLASZ",
                                             partial(self.buttonFunc12, team, conc, add_datas), self)

        else:
            if (logic.Groups[team].getActualExercise().getLLastAnswer() == "1"):
                self.label11.setText(str(logic.Groups[team].getSumOfExercises()) + ". feladat \tJÓ")
            else:
                self.label11.setText(str(logic.Groups[team].getSumOfExercises()) + ". feladat \tROSSZ")

            self.label12 = createLabel(280, 40, 260, 40, "", self)
            self.label12.setAlignment(QtCore.Qt.AlignCenter)

            if (logic.Groups[team].getActualExercise().getLastAnswer() == "1"):
                self.label12.setText("JÓ")
                self.label12.setStyleSheet("background-color: green")
            else:
                self.label12.setText("ROSSZ")
                self.label12.setStyleSheet("background-color: red")

        self.ok_button = createPushButton(20, 120 + (block_length) * 80, 520, 40, "OK",
                                          partial(self.blocks, team, block_length, conc, add_datas), self)

        if (logic.Groups[team].numOfExercise <= 13):

            self.label21 = createLabel(40, 120, 220, 40, "", self)

            if (max_length > logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises()).getNumOfAnswers() or tr):

                if (logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises()).getLastAnswer() == "1"):
                    self.label21.setText(str(logic.Groups[team].getSumOfExercises() + 1) + ". feladat \tJÓ")
                else:
                    self.label21.setText(str(logic.Groups[team].getSumOfExercises() + 1) + ". feladat \tROSSZ")

                self.button21 = createPushButton(280, 120, 120, 40, "MARAD",
                                                 partial(self.buttonFunc21, team, conc, add_datas), self)
                self.button22 = createPushButton(420, 120, 120, 40, "ÚJ VÁLASZ",
                                                 partial(self.buttonFunc22, team, conc, add_datas), self)

            else:
                if (logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises()).getLLastAnswer() == "1"):
                    self.label21.setText(str(logic.Groups[team].getSumOfExercises() + 1) + ". feladat \tJÓ")
                else:
                    self.label21.setText(str(logic.Groups[team].getSumOfExercises() + 1) + ". feladat \tROSSZ")

                self.label22 = createLabel(280, 120, 260, 40, "", self)
                self.label22.setAlignment(QtCore.Qt.AlignCenter)

                if (logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises()).getLastAnswer() == "1"):
                    self.label22.setText("JÓ")
                    self.label22.setStyleSheet("background-color: green")
                else:
                    self.label22.setText("ROSSZ")
                    self.label22.setStyleSheet("background-color: red")

        if (logic.Groups[team].numOfExercise <= 10):

            self.label31 = createLabel(40, 200, 220, 40, "", self)

            if (max_length > logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises() + 1).getNumOfAnswers() or tr):

                if (logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises() + 1).getLastAnswer() == "1"):
                    self.label31.setText(str(logic.Groups[team].getSumOfExercises() + 2) + ". feladat \tJÓ")
                else:
                    self.label31.setText(str(logic.Groups[team].getSumOfExercises() + 2) + ". feladat \tROSSZ")

                self.button31 = createPushButton(280, 200, 120, 40, "MARAD",
                                                 partial(self.buttonFunc31, team, conc, add_datas), self)
                self.button32 = createPushButton(420, 200, 120, 40, "ÚJ VÁLASZ",
                                                 partial(self.buttonFunc32, team, conc, add_datas), self)

            else:
                if (logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises() + 1).getLLastAnswer() == "1"):
                    self.label31.setText(str(logic.Groups[team].getSumOfExercises() + 2) + ". feladat \tJÓ")
                else:
                    self.label31.setText(str(logic.Groups[team].getSumOfExercises() + 2) + ". feladat \tROSSZ")

                self.label32 = createLabel(280, 200, 260, 40, "", self)
                self.label32.setAlignment(QtCore.Qt.AlignCenter)

                if (logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises() + 1).getLastAnswer() == "1"):
                    self.label32.setText("JÓ")
                    self.label32.setStyleSheet("background-color: green")
                else:
                    self.label32.setText("ROSSZ")
                    self.label32.setStyleSheet("background-color: red")

        if (logic.Groups[team].numOfExercise <= 6):

            self.label41 = createLabel(40, 280, 220, 40, "", self)

            if (max_length > logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises() + 2).getNumOfAnswers() or tr):

                if (logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises() + 2).getLastAnswer() == "1"):
                    self.label41.setText(str(logic.Groups[team].getSumOfExercises() + 3) + ". feladat \tJÓ")
                else:
                    self.label41.setText(str(logic.Groups[team].getSumOfExercises() + 3) + ". feladat \tROSSZ")

                self.button41 = createPushButton(280, 280, 120, 40, "MARAD",
                                                 partial(self.buttonfunc41, team, conc, add_datas), self)
                self.button42 = createPushButton(420, 280, 120, 40, "ÚJ VÁLASZ",
                                                 partial(self.buttonfunc42, team, conc, add_datas), self)

            else:
                if (logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises() + 2).getLLastAnswer() == "1"):
                    self.label41.setText(str(logic.Groups[team].getSumOfExercises() + 3) + ". feladat \tJÓ")
                else:
                    self.label41.setText(str(logic.Groups[team].getSumOfExercises() + 3) + ". feladat \tROSSZ")

                self.label42 = createLabel(280, 280, 260, 40, "", self)
                self.label42.setAlignment(QtCore.Qt.AlignCenter)

                if (logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises() + 2).getLastAnswer() == "1"):
                    self.label42.setText("JÓ")
                    self.label42.setStyleSheet("background-color: green")
                else:
                    self.label42.setText("ROSSZ")
                    self.label42.setStyleSheet("background-color: red")

        if (logic.Groups[team].numOfExercise == 1):

            self.label51 = createLabel(40, 360, 220, 40, "", self)

            if (max_length > logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises() + 3).getNumOfAnswers() or tr):

                if (logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises() + 3).getLastAnswer() == "1"):
                    self.label51.setText(str(logic.Groups[team].getSumOfExercises() + 4) + ". feladat \tJÓ")
                else:
                    self.label51.setText(str(logic.Groups[team].getSumOfExercises() + 4) + ". feladat \tROSSZ")

                self.button51 = createPushButton(280, 360, 120, 40, "MARAD",
                                                 partial(self.buttonfunc51, team, conc, add_datas), self)
                self.button52 = createPushButton(420, 360, 120, 40, "ÚJ VÁLASZ",
                                                 partial(self.buttonfunc52, team, conc, add_datas), self)

            else:
                if (logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises() + 3).getLLastAnswer() == "1"):
                    self.label51.setText(str(logic.Groups[team].getSumOfExercises() + 4) + ". feladat \tJÓ")
                else:
                    self.label51.setText(str(logic.Groups[team].getSumOfExercises() + 4) + ". feladat \tROSSZ")

                self.label52 = createLabel(280, 360, 260, 40, "", self)
                self.label52.setAlignment(QtCore.Qt.AlignCenter)

                if (logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises() + 3).getLastAnswer() == "1"):
                    self.label52.setText("JÓ")
                    self.label52.setStyleSheet("background-color: green")
                else:
                    self.label52.setText("ROSSZ")
                    self.label2.setStyleSheet("background-color: red")

    def buttonFunc11(self, team, conc, add_datas):
        if (logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises() - 1).getLastAnswer() == "1"):
            conc[0] = "1"
        else:
            conc[0] = "0"
        answer = logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises() - 1).additionalDatas.split(" ; ")
        last_ans = answer[len(answer) - 2]
        add_datas[0] = last_ans

        self.button11 = createPushButton(280, 40, 120, 40, "MARAD", partial(self.buttonFunc11, team, conc, add_datas),
                                         self)
        self.button11.setStyleSheet("QPushButton { background-color: green }")
        self.button11.show()

        self.button12 = createPushButton(420, 40, 120, 40, "ÚJ VÁLASZ",
                                         partial(self.buttonFunc12, team, conc, add_datas), self)
        self.button12.setStyleSheet("QPushButton { background-color: lightgray }")
        self.button12.show()

    def buttonFunc12(self, team, conc, add_datas):

        self.button11 = createPushButton(280, 40, 120, 40, "MARAD", partial(self.buttonFunc11, team, conc, add_datas),
                                         self)
        self.button11.setStyleSheet("QPushButton { background-color: lightgray }")
        self.button11.show()

        self.button12 = createPushButton(420, 40, 120, 40, "ÚJ VÁLASZ",
                                         partial(self.buttonFunc12, team, conc, add_datas), self)
        self.button12.setStyleSheet("QPushButton { background-color: green }")
        self.button12.show()

        self.buttonf = answerTheBlock(team, 0, conc, add_datas)
        self.buttonf.show()

    def buttonFunc21(self, csap, conc, add_datas):
        if (logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises()).getLastAnswer() == "1"):
            conc[1] = "1"
        else:
            conc[1] = "0"
        answer = logic.Groups[csap].getNthExercise(logic.Groups[csap].getSumOfExercises()).additionalDatas.split(" ; ")
        last_ans = answer[len(answer) - 2]
        add_datas[1] = last_ans

        self.button21 = createPushButton(280, 120, 120, 40, "MARAD", partial(self.buttonFunc21, csap, conc, add_datas),
                                         self)
        self.button21.setStyleSheet("QPushButton { background-color: green }")
        self.button21.show()

        self.button22 = createPushButton(420, 120, 120, 40, "ÚJ VÁLASZ",
                                         partial(self.buttonFunc22, csap, conc, add_datas), self)
        self.button22.setStyleSheet("QPushButton { background-color: lightgray }")
        self.button22.show()

    def buttonFunc22(self, team, conc, add_datas):

        self.button21 = createPushButton(280, 120, 120, 40, "MARAD", partial(self.buttonFunc21, team, conc, add_datas),
                                         self)
        self.button21.setStyleSheet("QPushButton { background-color: lightgray }")
        self.button21.show()

        self.button22 = createPushButton(420, 120, 120, 40, "ÚJ VÁLASZ",
                                         partial(self.buttonFunc22, team, conc, add_datas), self)
        self.button22.setStyleSheet("QPushButton { background-color: green }")
        self.button22.show()

        self.buttonf = answerTheBlock(team, 1, conc, add_datas)
        self.buttonf.show()

    def buttonFunc31(self, team, conc, add_datas):
        if (logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises() + 1).getLastAnswer() == "1"):
            conc[2] = "1"
        else:
            conc[2] = "0"
        answer = logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises() + 1).additionalDatas.split(" ; ")
        last_ans = answer[len(answer) - 2]
        add_datas[2] = last_ans

        self.button31 = createPushButton(280, 200, 120, 40, "MARAD", partial(self.buttonFunc31, team, conc, add_datas),
                                         self)
        self.button31.setStyleSheet("QPushButton { background-color: green }")
        self.button31.show()

        self.button32 = createPushButton(420, 200, 120, 40, "ÚJ VÁLASZ",
                                         partial(self.buttonFunc32, team, conc, add_datas), self)
        self.button32.setStyleSheet("QPushButton { background-color: lightgray }")
        self.button32.show()

    def buttonFunc32(self, team: int, conc, add_datas):

        self.button31 = createPushButton(280, 200, 120, 40, "MARAD", partial(self.buttonFunc31, team, conc, add_datas),
                                         self)
        self.button31.setStyleSheet("QPushButton { background-color: lightgray }")
        self.button31.show()

        self.button32 = createPushButton(420, 200, 120, 40, "ÚJ VÁLASZ",
                                         partial(self.buttonFunc32, team, conc, add_datas), self)
        self.button32.setStyleSheet("QPushButton { background-color: green }")
        self.button32.show()

        self.buttonf = answerTheBlock(team, 2, conc, add_datas)
        self.buttonf.show()

    def buttonfunc41(self, team: int, conc, add_datas):
        if (logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises() + 2).getLastAnswer() == "1"):
            conc[3] = "1"
        else:
            conc[3] = "0"
        answer = logic.Groups[team].getNthExercise(logic.Groups[team].getSumOfExercises() + 2).additionalDatas.split(" ; ")
        last_ans = answer[len(answer) - 2]
        add_datas[3] = last_ans

        self.button41 = createPushButton(280, 280, 120, 40, "MARAD", partial(self.buttonfunc41, team, conc, add_datas),
                                         self)
        self.button41.setStyleSheet("QPushButton { background-color: green }")
        self.button41.show()

        self.button42 = createPushButton(420, 280, 120, 40, "ÚJ VÁLASZ",
                                         partial(self.buttonfunc42, team, conc, add_datas), self)
        self.button42.setStyleSheet("QPushButton { background-color: lightgray }")
        self.button42.show()

    def buttonfunc42(self, teams: int, conc, add_datas):

        self.button41 = createPushButton(280, 280, 120, 40, "MARAD", partial(self.buttonfunc41, teams, conc, add_datas),
                                         self)
        self.button41.setStyleSheet("QPushButton { background-color: lightgray }")
        self.button41.show()

        self.button42 = createPushButton(420, 280, 120, 40, "ÚJ VÁLASZ",
                                         partial(self.buttonfunc42, teams, conc, add_datas), self)
        self.button42.setStyleSheet("QPushButton { background-color: green }")
        self.button42.show()

        self.buttonf = answerTheBlock(teams, 3, conc, add_datas)
        self.buttonf.show()

    def buttonfunc51(self, teams, conc, add_datas):
        if (logic.Groups[teams].getNthExercise(logic.Groups[teams].getSumOfExercises() + 3).getLastAnswer() == "1"):
            conc[4] = "1"
        else:
            conc[4] = "0"
        answer = logic.Groups[teams].getNthExercise(logic.Groups[teams].getSumOfExercises() + 3).additionalDatas.split(" ; ")
        last_ans = answer[len(answer) - 2]
        add_datas[4] = last_ans

        self.button51 = createPushButton(280, 360, 120, 40, "MARAD", partial(self.buttonfunc51, teams, conc, add_datas),
                                         self)
        self.button51.setStyleSheet("QPushButton { background-color: green }")
        self.button51.show()

        self.button52 = createPushButton(420, 360, 120, 40, "ÚJ VÁLASZ",
                                         partial(self.buttonfunc52, teams, conc, add_datas), self)
        self.button52.setStyleSheet("QPushButton { background-color: lightgray }")
        self.button52.show()

    def buttonfunc52(self, team, conc, add_datas):

        self.button51 = createPushButton(280, 360, 120, 40, "MARAD", partial(self.buttonfunc51, team, conc, add_datas),
                                         self)
        self.button51.setStyleSheet("QPushButton { background-color: lightgray }")
        self.button51.show()

        self.button52 = createPushButton(420, 360, 120, 40, "ÚJ VÁLASZ",
                                         partial(self.buttonfunc52, team, conc, add_datas), self)
        self.button52.setStyleSheet("QPushButton { background-color: green }")
        self.button52.show()

        self.buttonf = answerTheBlock(team, 4, conc, add_datas)
        self.buttonf.show()

    def blocks(self, team, block_length, conc, add_datas):
        self.close()
        for i in range(0, block_length + 1):
            if conc[i] != "":
                if conc[i] == "1":
                    logic.Groups[team].exercises[logic.Groups[team].numOfExercise + i - 1].newSolution(True)
                else:
                    logic.Groups[team].exercises[logic.Groups[team].numOfExercise + i - 1].newSolution(False)
            if (add_datas[i] != ""):
                logic.Groups[team].exercises[logic.Groups[team].numOfExercise + i - 1].additionalDatas += add_datas[i] + " ; "

        logic.writeGroupDataToFile()
        logic.WriteAdditionalDatasToFile()

        logic.refreshPoints()
        maxlength = 0
        for i in range(logic.Groups[team].numOfExercise, logic.Groups[team].numOfExercise + block_length + 1):
            if (maxlength < len(logic.Groups[team].exercises[i - 1].results)):
                maxlength = len(logic.Groups[team].exercises[i - 1].results)
        tr = True
        for i in range(logic.Groups[team].numOfExercise, logic.Groups[team].numOfExercise + block_length + 1):
            if (maxlength > len(logic.Groups[team].exercises[i - 1].results)):
                tr = False
        trr = False
        for i in conc:
            if i == "1" or i == "0":
                trr = True
        if (trr and tr):
            logic.Groups[team].numOfExercise = logic.Groups[team].numOfExercise + block_length + 1
            self.blokkv = BlockEnd(team)
            self.blokkv.show()

