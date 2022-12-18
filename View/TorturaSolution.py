# import windows
from View.BlockRepeat import *
from View.ExerciseSolution import *
from View.FixSolutions import *


class TorturaSolution(QWidget):
    def __init__(self):
        tabor, csoport = logic.Infos.camp, logic.Infos.age
        super(TorturaSolution, self).__init__()
        numGr = len(logic.Groups) - 1
        self.setGeometry(300, 100, 500, 500 + (numGr // 5) * 60)
        self.setWindowTitle(tabor + " - " + csoport + " csoport")
        self.setStyleSheet("background-color : lightblue")
        self.initUI()

    def initUI(self):
        numGr = len(logic.Groups) - 1
        groupButtons = []
        for i in range(0, len(logic.Groups)):
            groupButtons.append(createPushButton(40 + 88 * (i - i // 5 * 5), 40 + 60 * (i // 5), 68, 40, str(i + 1),
                                                 partial(self.rightOrWrong, i), self))

        self.nameOfStudent = createLabel(40, 140 + ((numGr // 5) * 60), 120, 40, "Keresés névre:", self)
        self.readName = createLineEdit(200, 140 + ((numGr // 5) * 60), 260, 40, self)
        self.searchName = createPushButton(40, 200 + ((numGr // 5) * 60), 420, 40, "OK", self.findByName, self)

        self.tabella = createPushButton(40, 300 + ((numGr // 5) * 60), 420, 40, "Tabella", self.scoreBoard, self)

        self.correct = createPushButton(40, 360 + ((numGr // 5) * 60), 420, 40, "Javítás", self.correct, self)

        self.finishTortura = createPushButton(40, 420 + ((numGr // 5) * 60), 420, 40, "Tortúra befejezése", self.end,
                                              self)

    def end(self):

        self.finishTheTortura = createMessageBox(200, 380, 100, 60, "Figyelmeztetés", "Biztosan befejezed a Tortúrát?",
                                                 (QMessageBox.Yes | QMessageBox.No), self)
        returnValue = self.finishTheTortura.exec()

        if returnValue == QMessageBox.No:
            self.finishTheTortura.close()
        else:

            logic.finishTheTorturaAtThisTime()
            logic.writeGroupDataToFile()
            logic.writeResultsToFile()
            self.finishTheTortura.close()
            self.close()

        logic.Infos.writeTorturaDatasToFile()

    def scoreBoard(self):

        sortedlist = logic.sortResults()
        self.tabellalist = createListWidget(200, 400, 550, 300, "Csapatok tabellája", self.getTabItem)
        self.tabellalist.setStyleSheet("background-color: lightpink")
        for i in range(0, len(sortedlist)):
            self.tabellalist.insertItem(i, str(i + 1) + ".\t" + str(
                sortedlist[i].numOfGroup) + ". csapat\t\tpontszám: " + str(sortedlist[i].points) + "\tends: " + str(
                sortedlist[i].ends))

    def getTabItem(self):
        temp = self.tabellalist.currentItem().text().split(".")
        team_temp = temp[1].replace('\t', '')
        team = logic.findTheGroupFromList(int(team_temp))

        self.rp = QtWidgets.QTextBrowser()
        self.rp.setStyleSheet("background-color: lightpink")
        self.rp.setGeometry(750, 100, 550, 700)
        self.rp.setWindowTitle(str(team + 1) + ". csapat")
        self.rp.insertPlainText("\nPontszám:\t" + str(logic.Groups[team].getPoint()))
        self.rp.insertPlainText("\n\nBefejezve:\t" + str(logic.Groups[team].getFinish()))
        self.rp.insertPlainText("\n\nCsapat tagjai:\t")
        s = 0
        for i in logic.Groups[team].members:
            if (s == 2):
                self.rp.insertPlainText("\n\t\t")
            if (s % 2 == 0):
                self.rp.insertPlainText(str(i) + "\t\t")
            else:
                self.rp.insertPlainText(str(i))
            s = s + 1

        self.rp.insertPlainText("\n\nFeladat\t1. próba\t2. próba\t3. próba\t4. próba\t5. próba\n\n")
        for i in range(0, 15):
            self.rp.insertPlainText(str(i + 1) + ".\t")
            for iii in str(logic.Groups[team].getNthExercise(i).getConcatenatedForm()):
                if (iii == '1'):
                    self.rp.insertPlainText("JÓ\t")
                else:
                    self.rp.insertPlainText("ROSSZ\t")
            self.rp.insertPlainText("\n\n")
        self.rp.show()

    def findByName(self):
        if (logic.Infos.group_file == ""):
            self.ThereIsNoFile = createMessageBox(200, 380, 100, 60, "Figyelmeztetés",
                                                  "Nem lehet névre keresni, nincs fájl!", (QMessageBox.Ok), self)
        else:
            found, embernev = logic.findByNames(self.readName.text())

            self.listwidget = createListWidget(200, 400, 300, 200, "Csapatok - emberek", self.getItem)
            for i in range(0, len(found)):
                self.listwidget.insertItem(i, str(found[i].getNumOfGroup()) + ". csapat\t" + str(embernev[i]))
            self.listwidget.setStyleSheet("background-color: lightpink")

    def getItem(self):
        self.listwidget.close()
        temp = self.listwidget.currentItem().text().split(".")
        team = logic.findTheGroupFromList(temp[0])

        if (logic.Groups[int(team)].getFinish() != ""):
            self.TheGroupsFinished = createMessageBox(200, 380, 100, 60, "Figyelmeztetés",
                                                      "Az adott csapat végzett a tortúrával!", (QMessageBox.Ok), self)
        else:
            if (logic.Groups[team].getActualExercise().getNumOfAnswers() > 0):
                self.listwidget.close()
                self.do_block_again = BlockRepeat(team)
                self.do_block_again.show()
            else:
                if logic.Groups[team].endOfBlock == 1:
                    self.blokkvege = BlockEnd(team)
                    self.blokkvege.show()
                else:
                    self.tell = ExerciseSolution(team)
                    self.tell.show()

    def rightOrWrong(self, team):
        if (logic.Groups[team].getFinish() == ""):
            if (logic.Groups[team].getActualExercise().getNumOfAnswers() > 0):
                self.do_block_again = BlockRepeat(team)
                self.do_block_again.show()
            else:
                if logic.Groups[team].endOfBlock == "1":
                    self.blokkvege = BlockEnd(team)
                    self.blokkvege.show()
                else:
                    self.tell = ExerciseSolution(team)
                    self.tell.show()
        else:
            self.TheGroupsFinished = createMessageBox(200, 380, 100, 60, "Figyelmeztetés",
                                                      "Az adott csapat végzett a tortúrával!", (QMessageBox.Ok), self)

    def correct(self):
        self.jav = FixSolutions()
        self.jav.show()

