# import windows
from View.TorturaSolution import *


class TorturaContinue(QWidget):
    def __init__(self):
        super(TorturaContinue, self).__init__()
        self.setGeometry(300, 140, 500, 360)
        self.setStyleSheet("background-color: lightblue")
        tabor, csoport = logic.Infos.camp, logic.Infos.age
        self.setWindowTitle(tabor + " - " + csoport + " csoport")
        self.initUI(csoport, tabor)

    def initUI(self, csoport, tabor):

        self.sumOfGroups = createLabel(40, 40, 160, 40, "Csapatok száma:", self)
        self.countOfGroups = createLabel(240, 40, 220, 40, str(len(logic.Groups)), self)
        self.countOfGroups.setAlignment(QtCore.Qt.AlignCenter)

        self.fileGroups = createLabel(40, 120, 160, 40, "Csapatok:", self)
        self.dontAllow = createLabel(240, 120, 220, 40, "Nincs lehetőség!", self)
        self.dontAllow.setAlignment(QtCore.Qt.AlignCenter)

        self.fileSolutions = createLabel(40, 200, 160, 40, "Megoldások:", self)
        self.uploadSolution = createPushButton(200, 200, 120, 40, "Feltöltés", self.uploadMegoldas, self)
        self.showSolutionFile = createLabel(340, 200, 120, 40, "", self)
        self.showSolutionFile.setStyleSheet("background-color : white")
        self.showSolutionFile.setAlignment(QtCore.Qt.AlignCenter)
        self.showSolutionFile.show()

        self.finishUpload = createPushButton(40, 280, 420, 40, "Tovább", self.tortbem, self)

        if (logic.Infos.solutionFile == ""):
            self.showSolutionFile.setText("Nincs fájl")
            self.showSolutionFile.show()
        else:
            a = logic.Infos.solutionFile.split('/')
            self.showSolutionFile.setText(a[len(a) - 1])
            self.showSolutionFile.show()

    def tortbem(self):
        self.close()

        logic.Infos.writeTorturaDatasToFile()

        self.tortbe = TorturaSolution()
        self.tortbe.show()

    def uploadMegoldas(self):
        self.options = QFileDialog(self)
        file_megoldas, _ = QFileDialog.getOpenFileName(self)
        if file_megoldas:
            logic.Solution.clear()
            f = open(file_megoldas, "r", encoding='UTF-8')
            ii = 0
            for i in f:
                if not i in ['\n', '\r\n']:
                    logic.Solution.append(i.replace('\n', ''))
                    ii = ii + 1
            f.close()
            fileNameMegoldas = file_megoldas.split('/')
            self.showSolutionFile = createLabel(340, 200, 120, 40, fileNameMegoldas[len(fileNameMegoldas) - 1], self)
            self.showSolutionFile.setStyleSheet("background-color : white")
            self.showSolutionFile.setAlignment(QtCore.Qt.AlignCenter)
            self.showSolutionFile.show()
            logic.Infos.solutionFile = file_megoldas
