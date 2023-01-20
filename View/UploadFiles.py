import shutil

# import windows
from View.TorturaContinue import *
from View.TorturaEnd import *

class UploadFiles(QWidget):

    def __init__(self):
        super(UploadFiles, self).__init__()
        tabor, csoport = logic.Infos.camp, logic.Infos.age
        self.setGeometry(300, 140, 500, 360)
        self.setStyleSheet("background-color: lightblue")
        self.setWindowTitle(tabor + " - " + csoport + " csoport")
        self.initUI()

    def initUI(self):

        self.sumOfGroups = createLabel(40, 40, 140, 40, "Groupok száma:", self)
        self.writeSumOfGroups = createSpinBox(200, 40, 260, 40, 1, 30, self)

        self.fileGroups = createLabel(40, 120, 140, 40, "Groupok:", self)
        self.uploadGroup = createPushButton(180, 120, 120, 40, "Feltöltés", self.uploadGroup, self)

        self.showGroupFile = createLabel(320, 120, 140, 40, "Nincs fájl", self)
        self.showGroupFile.setStyleSheet("background-color : white")
        self.showGroupFile.setAlignment(QtCore.Qt.AlignCenter)
        self.showGroupFile.show()

        self.fileSolutions = createLabel(40, 200, 140, 40, "Megoldások:", self)
        self.uploadSolution = createPushButton(180, 200, 120, 40, "Feltöltés", self.uploadMegoldas, self)
        self.showSolutionFile = createLabel(320, 200, 140, 40, "Nincs fájl", self)
        self.showSolutionFile.setStyleSheet("background-color : white")
        self.showSolutionFile.setAlignment(QtCore.Qt.AlignCenter)
        self.showSolutionFile.show()

        self.finishUpload = createPushButton(40, 280, 420, 40, "Tovább", self.tortbem, self)

    def uploadGroup(self):
        self.options = QFileDialog(self)
        file_csapat, _ = QFileDialog.getOpenFileName(self)
        if file_csapat:
            logic.Groups.clear()
            f = open(file_csapat, "r", encoding='UTF-8')
            ii = 0
            logic.Groups.append(Group(ii + 1))
            for i in f:
                if not i in ['\n', '\r\n']:
                    logic.Groups[ii].members.append(i.replace('\n', ''))
                else:
                    ii = ii + 1
                    logic.Groups.append(Group(ii + 1))
            f.close()
            logic.Infos.numOfGroups = len(logic.Groups)
            fileNameGroup = file_csapat.split('/')
            self.showGroupFile = createLabel(320, 120, 140, 40, fileNameGroup[len(fileNameGroup) - 1], self)
            self.showGroupFile.setStyleSheet("background-color : white")
            self.showGroupFile.setAlignment(QtCore.Qt.AlignCenter)
            self.showGroupFile.show()
            logic.Infos.group_file = file_csapat
        else:
            logic.Groups.clear()

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
                    ii = ii + 1;
            f.close()
            fileNameMegoldas = file_megoldas.split('/')
            self.showSolutionFile = createLabel(320, 200, 140, 40, fileNameMegoldas[len(fileNameMegoldas) - 1], self)
            self.showSolutionFile.setStyleSheet("background-color : white")
            self.showSolutionFile.setAlignment(QtCore.Qt.AlignCenter)
            self.showSolutionFile.show()
            logic.Infos.solution_file = file_megoldas
        else:
            logic.Solution.clear()

    def tortbem(self):
        if (len(logic.Groups) == 0):
            for i in range(0, self.writeSumOfGroups.value()):
                logic.Groups.append(Group(i + 1))
        logic.Infos.numOfGroups = len(logic.Groups)
        tabor, csoport = logic.Infos.camp, logic.Infos.age

        date = datetime.datetime.now()
        hm = str(date.strftime("%y"))

        directory = (tabor + "_" + csoport + "_" + hm)
        parent_dir = "data/input/"
        path = os.path.join(parent_dir, directory)

        if (os.path.isdir(path)):
            self.mb = createMessageBox(200, 380, 100, 60, "Figyelmeztetés", "A Tortúra már létezik. Betölti?",
                                       (QMessageBox.Yes | QMessageBox.No), self)
            returnValue = self.mb.exec()
            if returnValue == QMessageBox.No:
                shutil.rmtree(path)
                os.mkdir(path)

                f = open("data/input/input.txt", "w")
                f.write(directory)
                f.close()

                self.close()
                logic.Infos.writeTorturaDatasToFile()
                logic.writeGroupDataToFile()

                self.tortbe = TorturaSolution()
                self.tortbe.show()

            else:
                f = open("data/input/input.txt", "w")
                f.write(directory)
                f.close()

                if (exists("data/input/input.txt")):
                    ff = open("data/input/input.txt", "r")
                    tortura = ff.readline().replace('\n', '')
                    ff.close()

                    if logic.Infos.readTorturaDatas(tortura):
                        logic.readGroupsFromFile()
                        logic.readSolutionsFromFile()
                        logic.readGroupDatasFromFile(tortura)
                        logic.ReadAdditionalDatas()
                        for ii in range(0, len(logic.Groups)):
                            logic.refreshPoints()

                        if (int(logic.Infos.endOfTortura) == 1):
                            self.tortveg = TorturaEnd()
                            self.tortveg.show()
                        else:
                            if (logic.Infos.solution_file == ""):
                                self.utolagosfelt = TorturaContinue()
                                self.utolagosfelt.show()
                            else:
                                self.tortbe = TorturaSolution()
                                self.tortbe.show()
                    else:
                        self.mb = createMessageBox(200, 380, 100, 60, "Figyelmeztetés",
                                                   "Nincs megnyitható régi tortúra, a fájlokat törölték!",
                                                   QMessageBox.Ok, self)

            self.mb.close()
            self.close()
        else:
            os.mkdir(path)

            f = open("data/input/input.txt", "w")
            f.write(directory)
            f.close()

            logic.Infos.writeTorturaDatasToFile()
            logic.writeGroupDataToFile()
            self.close()
            self.tortbe = TorturaSolution()
            self.tortbe.show()


