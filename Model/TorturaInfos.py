import datetime
import json
from os.path import exists


class TorturaInfos:
    def __init__(self):
        self.camp: str = ""
        self.age: str = ""
        self.numOfGroups: int = 0
        self.groupFile: str = ""
        self.solutionFile: str = ""
        self.dataFile: str = "groupdatas.json"
        self.endOfTortura: bool = False

    def setGroupFile(self, gf: str) -> None:
        self.groupFile = gf

    def setSolutionFile(self, sf: str) -> None:
        self.groupFile = sf

    def torturaEnds(self) -> None:
        self.endOfTortura = True

    def reOpenTortura(self) -> None:
        self.endOfTortura = False

    def writeTorturaDatasToFile(self):

        date = datetime.datetime.now()
        hm = str(date.strftime("%y"))
        dictionary = {
            "camp": self.camp,
            "age": self.age,
            "numOfGroups": self.numOfGroups,
            "groupFile": self.groupFile,
            "solutionFile": self.solutionFile,
            "dataFile": self.dataFile,
            "endOfTortura": self.endOfTortura
        }
        json_object = json.dumps(dictionary, indent=4)
        with open("data/input/" + self.camp + "_" + self.age + "_" + hm + "/datas.json", "w") as outfile:
            outfile.write(json_object)

    def readTorturaDatas(self, tortura: str):
        if exists("data/input/" + tortura + "/datas.json"):
            f = open("data/input/" + tortura + "/datas.json", "r")
            datas = json.load(f)
            self.camp = datas["camp"]
            self.age = datas["age"]
            self.numOfGroups = datas["numOfGroups"]
            self.groupFile = datas["groupFile"]
            self.solutionFile = datas["solutionFile"]
            self.dataFile = datas["dataFile"]
            self.endOfTortura = datas["endOfTortura"]
            f.close()
            return self
        else:
            return None
