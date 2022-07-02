# import windows
from View.UploadFiles import *


class NewTortura(QWidget):
    def __init__(self):
        super(NewTortura, self).__init__()
        self.setGeometry(300, 100, 300, 320)
        self.setStyleSheet("background-color: lightblue")
        self.setWindowTitle("Új Tortúra")
        self.initUI()

    def initUI(self):

        self.camp = createLabel(40, 80, 60, 40, "Tábor:", self)

        self.campsList = QtWidgets.QComboBox(self)
        self.campsList.setGeometry(120, 80, 140, 40)
        taborok = ("Sástó 1", "Sástó 2", "Pusztafalu", "Pálköve 1", "Pálköve 2")
        for x in taborok:
            self.campsList.addItem(x)

        self.group = createLabel(40, 160, 60, 40, "Csoport:", self)

        self.groupsList = QtWidgets.QComboBox(self)
        self.groupsList.setGeometry(120, 160, 140, 40)
        csoportok = ("AB", "KLM", "PQRST", "XYZUp")
        for x in csoportok:
            self.groupsList.addItem(x)

        self.campAndgroup = createPushButton(40, 240, 220, 40, "OK", self.fileuploading, self)

    def fileuploading(self):
        logic.Infos.camp, logic.Infos.age, logic.Infos.groupFile, logic.Infos.solutionFile\
            = (self.campsList.currentText()), (self.groupsList.currentText()), "", ""
        logic.Groups.clear()
        logic.Solution.clear()
        self.close()
        self.fileup = UploadFiles()
        self.fileup.show()
