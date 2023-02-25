# import windows
from View.BlockRepeat import *
from View.ExerciseSolution import *
from View.FixSolutions import *


class TorturaSolution(QWidget):
    def __init__(self):
        camp : str =  logic.Infos.camp
        age: str = logic.Infos.age
        num_of_groups : int = len(logic.Groups)

        super(TorturaSolution, self).__init__()
        self.setGeometry(300, 100, 500, 500 + ((num_of_groups - 1) // 5) * 60)
        self.setWindowTitle(camp + " - " + age + " csoport")
        self.setStyleSheet("background-color : lightblue")
        self.initUI()

    def initUI(self):
        num_of_groups : int = len(logic.Groups)
        buttons_of_groups : List = []   # The buttons of the groups
        for i in range(0, len(logic.Groups)):
            buttons_of_groups.append(createPushButton(40 + 88 * (i - i // 5 * 5), 40 + 60 * (i // 5)
                                                      , 68, 40, str(i + 1),
                                                 partial(self.announceSolution, i), self))

        self.search_students_label = createLabel(40, 140 + ((num_of_groups // 5) * 60), 120, 40, "Keresés névre:", self)
        self.search_student_lineedit = createLineEdit(200, 140 + ((num_of_groups // 5) * 60), 260, 40, self)
        self.search_student_button = createPushButton(40, 200 + ((num_of_groups // 5) * 60), 420, 40, "OK", self.searchForStudent, self)
        self.show_ranking_button = createPushButton(40, 300 + ((num_of_groups // 5) * 60), 420, 40, "Tabella", self.showRanking, self)
        self.solution_correction_button = createPushButton(40, 360 + ((num_of_groups // 5) * 60), 420, 40, "Javítás", self.correctSolutions, self)
        self.finish_tortura_button = createPushButton(40, 420 + ((num_of_groups // 5) * 60), 420, 40, "Tortúra befejezése", self.finishTortura,
                                              self)

    # Called by finish_tortura_button
    # Ask if you really want to finish the tortura
    # Set the current time to every group as finish time
    # Write datas to files
    def finishTortura(self) -> None:
        self.finish_tortura_msgbox = createMessageBox(200, 380, 100, 60,
                                                 "Figyelmeztetés", "Biztosan befejezed a Tortúrát?",
                                                 (QMessageBox.Yes | QMessageBox.No), self)

        if self.finish_tortura_msgbox.exec() == QMessageBox.No:
            self.finishTheTortura.close()
        else:
            logic.finishTheTorturaAtThisTime()
            logic.writeGroupDataToFile()
            logic.writeResultsToFile()
            self.finishTheTortura.close()
            self.close()
        logic.Infos.writeTorturaDatasToFile()

    # Called by show_ranking_button
    # Shows the sorted result of the Tortura
    def showRanking(self) -> None:
        sorted_result : List = logic.sortResults()
        self.ranking_list = createListWidget(200, 400, 550, 300, "Csapatok tabellája", self.getRankingListItem)
        self.ranking_list.setStyleSheet("background-color: lightpink")
        for i in range(0, len(sorted_result)):
            self.ranking_list.insertItem(i, str(i + 1) + ".\t" + str(
                sorted_result[i].numOfGroup) + ". csapat\t\tpontszám: " +
                str(sorted_result[i].points) + "\tends: " + str(sorted_result[i].ends))

    # Called by clicking on an element of ranking_list
    # Shows the infos of the group: points, solutions (every exercise), names
    def getRankingListItem(self) -> None:
        num_of_group = int(self.ranking_list.currentItem().text().split(".")[1]) - 1 # Get the number of the group

        self.infos_of_group = QtWidgets.QTextBrowser()
        self.infos_of_group.setStyleSheet("background-color: lightpink")
        self.infos_of_group.setGeometry(750, 100, 550, 700)
        self.infos_of_group.setWindowTitle(str(num_of_group + 1) + ". csapat")
        self.infos_of_group.insertPlainText("\nPontszám:\t" + str(logic.Groups[num_of_group].getPoint()))
        self.infos_of_group.insertPlainText("\n\nBefejezve:\t" + str(logic.Groups[num_of_group].getFinish()))
        self.infos_of_group.insertPlainText("\n\nCsapat tagjai:\t")
        s = 0
        for i in logic.Groups[num_of_group].members:
            if s == 2:
                self.infos_of_group.insertPlainText("\n\t\t")
            if s % 2 == 0:
                self.infos_of_group.insertPlainText(str(i) + "\t\t")
            else:
                self.infos_of_group.insertPlainText(str(i))
            s = s + 1

        self.infos_of_group.insertPlainText("\n\nFeladat\t1. próba\t2. próba\t3. próba\t4. próba\t5. próba\n\n")
        for i in range(0, 15):
            self.infos_of_group.insertPlainText(str(i + 1) + ".\t")
            for iii in str(logic.Groups[num_of_group].getNthExercise(i).getConcatenatedForm()):
                if (iii == '1'):
                    self.infos_of_group.insertPlainText("JÓ\t")
                else:
                    self.infos_of_group.insertPlainText("ROSSZ\t")
            self.infos_of_group.insertPlainText("\n\n")
        self.infos_of_group.show()

    # Called by search_student_button
    # Get the name from the search_student_lineedit and try to find her/him
    # If there is no file with names it is not available
    # Shows all of the results
    def searchForStudent(self) -> None:
        if logic.Infos.groupFile == "":
            self.no_file_msgbox = createMessageBox(200, 380, 100, 60, "Figyelmeztetés",
                                                  "Nem lehet névre keresni, nincs fájl!", (QMessageBox.Ok), self)
        else:
            occurences = logic.findByNames(self.search_student_lineedit.text())

            self.found_students = createListWidget(200, 400, 300, 200, "Csapatok - emberek", self.selectStudent)
            for i in range(0, len(occurences)):
                self.found_students.insertItem(i, str(occurences[i][0].getNumOfGroup()) + ". csapat\t" + str(occurences[i][1]))
            self.found_students.setStyleSheet("background-color: lightpink")

    # Called by clicking a line of found_students
    # Call the announceSolution function with the num of the group we clicked on
    def selectStudent(self) -> None:
        self.found_students.close()
        num_of_group = int(self.found_students.currentItem().text().split(".")[0]) - 1 # Get the number of the group
        self.announceSolution(num_of_group)

    # Called by selectStudent fuction and buttons_of_groups
    # Check the group has finished
    # Check if a group repeat a block
    # Check if a group at the end of a block
    # Show the right window
    def announceSolution(self, num_of_group: int) -> None:
        if logic.Groups[int(num_of_group)].getFinish() != "":
            self.the_group_has_finished = createMessageBox(200, 380, 100, 60,
                                                      "Figyelmeztetés",
                                                      "Az adott csapat végzett a tortúrával!",
                                                      (QMessageBox.Ok), self)
        else:
            if logic.Groups[num_of_group].getActualExercise().getNumOfAnswers() > 0:
                self.found_students.close()
                self.repeat_the_block_window = BlockRepeat(num_of_group)
                self.repeat_the_block_window.show()
            else:
                if logic.Groups[num_of_group].endOfBlock == 1:
                    self.end_of_the_block_window = BlockEnd(num_of_group)
                    self.end_of_the_block_window.show()
                else:
                    self.solution_announce_window = ExerciseSolution(num_of_group)
                    self.solution_announce_window.show()

    # Called by solution_correction_button
    # Open FixSolutions window
    def correctSolutions(self) -> None:
        self.correct_solutions_window = FixSolutions()
        self.correct_solutions_window.show()
