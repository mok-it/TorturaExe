from functools import partial
from PyQt5 import QtCore
from View.QtFunctions import *
from Model.Logic import *


class TorturaEnd(QWidget):
    def __init__(self):
        super(TorturaEnd, self).__init__()
        self.setGeometry(300, 140, 300, 340)
        self.setStyleSheet("background-color: lightblue")
        tabor, csoport = logic.Infos.camp, logic.Infos.camp
        self.setWindowTitle(tabor + " - " + csoport + " csoport")
        self.initUI(tabor, csoport)

    def initUI(self, tabor, csoport):

        self.dontAllow = createLabel(40, 40, 220, 40, "A Tortúrának vége\nCsak a tabella elérhető", self)
        self.dontAllow.setAlignment(QtCore.Qt.AlignCenter)

        self.tabella = createPushButton(40, 120, 220, 40, "Tabella", self.tabella, self)

        self.saveFile = createPushButton(40, 180, 220, 40, "Eredmény mentése fájlba",
                                         partial(self.savefile, tabor, csoport), self)

        self.back = createPushButton(40, 260, 220, 40, "Visszavonas", partial(self.visszavonas, tabor, csoport), self)

    def visszavonas(self, tabor, csoport):
        self.mb = QtWidgets.QMessageBox(self)
        self.mb = createMessageBox(200, 380, 100, 60, "Figyelmeztetés", "Biztosan visszavonja a Tortúra lezárását?",
                                   (QMessageBox.Yes | QMessageBox.No), self)
        returnValue = self.mb.exec()

        if returnValue == QMessageBox.No:
            self.mb.close()
        else:
            vegso = ""
            for i in logic.Groups:
                if vegso < i.getFinish():
                    vegso = i.getFinish()
            for i in logic.Groups:
                if vegso == i.getFinish():
                    i.ends = ""
            self.close()
            logic.Infos.reOpenTortura()
        logic.writeGroupDataToFile()
        logic.Infos.writeTorturaDatasToFile()

    def savefile(self, tabor, csoport):
        logic.writeResultsToFile()

        self.mb = createMessageBox(200, 380, 100, 60, "Kész", "A fájl kimentve", QMessageBox.Ok, self)

    def tabella(self):
        tab = logic.sortResults()
        self.listwidget = createListWidget(200, 400, 550, 300, "Csapatok tabellája", self.getTabItem)
        for i in range(0, len(tab)):
            self.listwidget.insertItem(i, str(i + 1) + ".\t" + str(tab[i].numOfGroup) + ". csapat\t\tpontszám: " + str(
                tab[i].points) + "\tbefejezve: " + str(tab[i].ends))
        self.listwidget.setStyleSheet("background-color: lightpink")

    def getTabItem(self, lstItem):
        seged = self.listwidget.currentItem().text().split(".")
        csapseged = seged[1].replace('\t', '')
        csapat = logic.findTheGroupFromList(int(csapseged))

        self.rp = QtWidgets.QTextBrowser()
        self.rp.setStyleSheet("background-color: lightpink")
        self.rp.setGeometry(750, 100, 550, 700)
        self.rp.setWindowTitle(str(csapat + 1) + ". csapat")
        self.rp.insertPlainText("\nPontszám:\t" + str(logic.Groups[csapat].getPoint()))
        self.rp.insertPlainText("\n\nBefejezve:\t" + str(logic.Groups[csapat].getFinish()))
        self.rp.insertPlainText("\n\nCsapat tagjai:\t")
        s = 0
        for i in logic.Groups[csapat].members:
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
            for iii in str(logic.Groups[csapat].getNthExercise(i).getConcatenatedForm()):
                if (iii == '1'):
                    self.rp.insertPlainText("JÓ\t")
                else:
                    self.rp.insertPlainText("ROSSZ\t")
            self.rp.insertPlainText("\n\n")
        self.rp.show()
