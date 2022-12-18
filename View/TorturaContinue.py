# import windows
from View.TorturaSolution import *


class TorturaContinue(QWidget):
    def __init__(self):
        super(TorturaContinue, self).__init__()
        self.setGeometry(300, 140, 500, 360)
        self.setStyleSheet("background-color: lightblue")
        tabor, csoport = logic.Infos.camp, logic.Infos.age
        self.setWindowTitle(tabor + " - " + csoport + " csoport")
        self.initUI()

    def initUI(self):

        self.sum_of_groups = createLabel(40, 40, 160, 40, "Csapatok száma:", self)
        self.count_of_groups = createLabel(240, 40, 220, 40, str(len(logic.Groups)), self)
        self.count_of_groups.setAlignment(QtCore.Qt.AlignCenter)

        self.file_groups = createLabel(40, 120, 160, 40, "Csapatok:", self)
        self.dont_allow = createLabel(240, 120, 220, 40, "Nincs lehetőség!", self)
        self.dont_allow.setAlignment(QtCore.Qt.AlignCenter)

        self.file_solutions = createLabel(40, 200, 160, 40, "Megoldások:", self)
        self.upload_solution = createPushButton(200, 200, 120, 40, "Feltöltés", self.uploadSolution, self)
        self.show_solution_file = createLabel(340, 200, 120, 40, "", self)
        self.show_solution_file.setStyleSheet("background-color : white")
        self.show_solution_file.setAlignment(QtCore.Qt.AlignCenter)
        self.show_solution_file.show()

        self.finish_upload = createPushButton(40, 280, 420, 40, "Tovább", self.tortbem, self)

        if (logic.Infos.solution_file == ""):
            self.show_solution_file.setText("Nincs fájl")
            self.show_solution_file.show()
        else:
            a = logic.Infos.solution_file.split('/')
            self.show_solution_file.setText(a[len(a) - 1])
            self.show_solution_file.show()

    def tortbem(self):
        self.close()

        logic.Infos.writeTorturaDatasToFile()

        self.tortbe = TorturaSolution()
        self.tortbe.show()

    def uploadSolution(self):
        self.options = QFileDialog(self)
        file_solution, _ = QFileDialog.getOpenFileName(self)
        if file_solution:
            logic.Solution.clear()
            f = open(file_solution, "r", encoding='UTF-8')
            ii = 0
            for i in f:
                if not i in ['\n', '\r\n']:
                    logic.Solution.append(i.replace('\n', ''))
                    ii = ii + 1
            f.close()
            file_name_solution = file_solution.split('/')
            self.show_solution_file = createLabel(340, 200, 120, 40, file_name_solution[len(file_name_solution) - 1], self)
            self.show_solution_file.setStyleSheet("background-color : white")
            self.show_solution_file.setAlignment(QtCore.Qt.AlignCenter)
            self.show_solution_file.show()
            logic.Infos.solution_file = file_solution
