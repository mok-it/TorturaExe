import json
import os
from typing import Sequence, List
from Model.TorturaInfos import *
from Model.Group import *


class Logic:
    def __init__(self):
        self.Solution: Sequence[str] = []            # a megoldások listája
        self.Groups: Sequence[Group] = []            # csapatok listája
        self.Infos: TorturaInfos = TorturaInfos()    #Tortura infók
        self.Solutions: Sequence[str] = []           #Feladatok megoldásai


    # a függvény visszaadja a "num"-adik csapatot
    def NthGroup(self, num) -> Group:
        return self.Groups[num]

    def finishTheTorturaAtThisTime(self):
        date = datetime.datetime.now()
        hm = str(date.strftime("%H")) + ":" + str(date.strftime("%M")) + "." + str(date.strftime("%S"))
        for i in self.Groups:
            if i.getFinish() == "":
                i.ends = hm
        self.Infos.endOfTortura = "1"


    def sortResults(self):
        tab = sorted(self.Groups, key=lambda x: x.ends, reverse=False)
        tab.sort(reverse=True, key=lambda x: x.points)
        return tab


    def findTheGroupFromList(self, member_name: str):
        group_num = 0
        for iii in self.Groups:
            if int(iii.numOfGroup) == int(member_name):
                break
            group_num += 1
        return group_num


    # Find students with the given name
    def findByNames(self, member_name: str) -> List:
        occurences : List = []  # (group number, name of student)
        for group in self.Groups:
            for member in group.members:
                if member_name.lower().replace(" ", "") in member.lower().replace(" ", ""):
                    occurences.append((group, member))
        return occurences


    def getBlockLength(self, csap):
        a = 0
        if self.Groups[csap].getSumOfExercises() == 1:
            a = 4
        elif self.Groups[csap].getSumOfExercises() == 6:
            a = 3
        elif self.Groups[csap].getSumOfExercises() == 10:
            a = 2
        elif self.Groups[csap].getSumOfExercises() == 13:
            a = 1
        return a


    def generateDirectories(self):
        maindir = "data"
        if not os.path.isdir(maindir):
            os.mkdir(maindir)

        directory = "input"
        parent_dir = "data/"
        path1 = os.path.join(parent_dir, directory)

        if not os.path.isdir(path1):
            os.mkdir(path1)

        directory = "output"
        path2 = os.path.join(parent_dir, directory)
        if not os.path.isdir(path2):
            os.mkdir(path2)

        directory = "additionaldatas"
        parent_dir = "data/output"
        path3 = os.path.join(parent_dir, directory)

        if not os.path.isdir(path3):
            os.mkdir(path3)

        directory = "results"
        path4 = os.path.join(parent_dir, directory)

        if not os.path.isdir(path4):
            os.mkdir(path4)

    def refreshPoints(self):
        for ii in self.Groups:
            ii.refreshPoint()

    def writeGroupDataToFile(self):
        date = datetime.datetime.now()
        hm = str(date.strftime("%y"))
        dictionary = {"groups": []}
        for i in range(0, self.Infos.numOfGroups):
            dictionary["groups"].append({
                "groupNum": self.Groups[i].numOfGroup,
                "solutions": [],
                "numOfEx": self.Groups[i].numOfExercise,
                "endOfBlock": self.Groups[i].endOfBlock,
                "endOfTortura": self.Groups[i].ends
            })
            for j in range(0, 15):
                dictionary["groups"][i]["solutions"].append(self.Groups[i].exercises[j].results)
        json_object = json.dumps(dictionary, indent=4)
        with open("data/input/" + self.Infos.camp + "_" + self.Infos.age + "_" + hm + "/" + self.Infos.dataFile, "w") as outfile:
            outfile.write(json_object)

    def writeResultsToFile(self):
        date = datetime.datetime.now()
        hm = str(date.strftime("%y"))
        ff = open(("data/output/results/" + self.Infos.camp + "_" + self.Infos.age + "_" + hm + ".txt"), "w")
        tab = sorted(self.Groups, reverse=False, key=lambda x: x.ends)
        tab.sort(reverse=True, key=lambda x: x.points)
        sz = 1
        for i in tab:
            ff.write(
                str(sz) + ".\t" + str(i.numOfGroup) + ". csapat\t" + str(i.points) + " pont\t" + i.getFinish() + "\n")
        ff.close()

    def WriteAdditionalDatasToFile(self):
        date = datetime.datetime.now()
        hm = str(date.strftime("%y"))
        ff = open(("data/output/additionaldatas/" + self.Infos.camp + "_" + self.Infos.age + "_" + hm + ".txt"), "w")
        for i in range(0, len(self.Groups)):
            ff.write(str(self.Groups[i].getNumOfGroup()) + ". csapat\n")
            for ii in range(0, 15):
                ff.write(str(ii + 1) + ". feladat: " + self.Groups[i].getNthExercise(ii).additionalDatas + "\n")
        ff.close()

    def ReadAdditionalDatas(self):
        date = datetime.datetime.now()
        hm = str(date.strftime("%y"))
        if exists("Tortura/output/additionaldatas/" + self.Infos.camp + "_" + self.Infos.age + "_" + hm + ".txt"):
            ff = open(("Tortura/output/additionaldatas/" + self.Infos.camp + "_" + self.Infos.age + "_" + hm + ".txt"), "r")
            sz = 0
            for i in ff:
                if sz % 16 == 0:
                    sz += 1
                else:
                    self.Groups[sz // 16].exercises[sz - sz // 16 * 16 - 1].additionalDatas = i.split(": ")[1].rstrip()
                    sz += 1
            ff.close()

        # nevek beolvasása
    def readGroupsFromFile(self) -> None:
        if self.Infos.groupFile:
            self.Groups.clear()
            ff = open(self.Infos.groupFile, "r", encoding='UTF-8')
            ii = 0
            self.Groups.append(Group(ii + 1))
            for i in ff:
                if not i in ['\n', '\r\n']:
                    self.Groups[ii].members.append(i.rstrip())
                else:
                    ii = ii + 1
                    self.Groups.append(Group(ii + 1))
            ff.close()
        else:
            self.Groups.clear()
            for i in range(0, int(self.Infos.numOfGroups)):
                self.Groups.append(Group(i + 1))

    # megoldások beolvasása
    def readSolutionsFromFile(self) -> None:
        if self.Infos.solutionFile:
            self.Solution.clear()
            ff = open(self.Infos.solutionFile, "r", encoding='UTF-8')
            ii = 0
            for i in ff:
                if not i in ['\n', '\r\n']:
                    self.Solution.append(i.rstrip())
                    ii = ii + 1
            ff.close()

    # eddigi megoldások
    def readGroupDatasFromFile(self, tortura: str) -> None:
        if self.Infos.dataFile:
            ff = open("data/input/" + tortura + "/" + self.Infos.dataFile, "r", encoding='UTF-8')
            datas = json.load(ff)
            numG = 0
            for i in datas["groups"]:
                self.Groups[numG].numOfGroup = i["groupNum"]
                self.Groups[numG].numOfExercise = i["numOfEx"]
                self.Groups[numG].ends = i["endOfTortura"]
                self.Groups[numG].endOfBlock = i["endOfBlock"]
                for j in range(0, 15):
                    self.Groups[numG].exercises[j].results = i["solutions"][j]
                numG += 1
            ff.close()
        else:
            self.writeGroupDataToFile()


logic = Logic()