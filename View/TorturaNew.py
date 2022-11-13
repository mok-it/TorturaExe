# import windows
from View.UploadFiles import *


class NewTortura(QWidget):

    # Class constructor
    # @param self The object pointer
    def __init__(self) -> None:
        super(NewTortura, self).__init__()
        self.setGeometry(300, 100, 300, 320)
        self.setStyleSheet("background-color: lightblue")
        self.setWindowTitle("Új Tortúra")
        self.initUI()

    # create a new window where you can make a new tortura, choose from camps and groups
    # @param self The object pointer
    def initUI(self) -> None:

        self.camp = createLabel(40, 80, 60, 40, "Tábor:", self)

        self.camps_list = QtWidgets.QComboBox(self)
        self.camps_list.setGeometry(120, 80, 140, 40)
        camps = ("Sástó 1", "Sástó 2", "Pusztafalu", "Pálköve 1", "Pálköve 2")
        for x in camps:
            self.camps_list.addItem(x)

        self.group = createLabel(40, 160, 60, 40, "Csoport:", self)

        self.groups_list = QtWidgets.QComboBox(self)
        self.groups_list.setGeometry(120, 160, 140, 40)
        teams = ("AB", "KLM", "PQRST", "XYZUp")
        for x in teams:
            self.groups_list.addItem(x)

        self.camp_and_group = createPushButton(40, 240, 220, 40, "OK", self.fileUploading, self)

    # close the window and open the file uploading window, where you can upload the groups file
    # @param self The object pointer
    def fileUploading(self)-> None:
        logic.Infos.camp, logic.Infos.age, logic.Infos.group_file, logic.Infos.solution_file\
            = (self.camps_list.currentText()), (self.groups_list.currentText()), "", ""
        logic.Groups.clear()
        logic.Solution.clear()
        self.close()
        self.fileUp = UploadFiles()
        self.fileUp.show()
