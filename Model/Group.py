import datetime
from typing import Sequence

from Model.Block import *
from Model.Exercise import *


def createDefaultBlocks() -> Sequence[Block]:
    return [Block(i, 6 - i, (1 + (5 + 7 - i) * (i - 1) // 2), (1 + (5 + 7 - i) * (i - 1) // 2) + 6 - i) for i in
            range(1, 6)]

Blokk: Sequence[Block] = createDefaultBlocks()  # blokkok

class Group:
    def __init__(self, numOfGroup):
        self.numOfGroup: int = numOfGroup
        self.members: Sequence[str] = []
        self.numOfExercise: int = 1
        self.resultOfExercises: Sequence[str] = []
        self.ends: str = ""
        self.points: int = 0
        self.endOfBlock: int = 0
        self.exercises: Sequence[Exercise] = [Exercise(i) for i in range(1, 16)]

    def getSumOfExercises(self) -> int:
        return self.numOfExercise

    def getFinish(self) -> str:
        return self.ends

    def getPoint(self) -> int:
        return self.points

    def getNthExercise(self, nth) -> Exercise:
        return self.exercises[nth]

    def getNumOfGroup(self) -> int:
        return self.numOfGroup

    def getActualExercise(self) -> Exercise:
        return self.exercises[self.numOfExercise - 1]

    def getBlockFromExerciseNumber(self) -> Block:
        if self.endOfBlock == "0":
            for i in Blokk:
                if i.start <= self.numOfExercise < i.ends:
                    return i
        else:
            for i in Blokk:
                if self.numOfExercise == i.ends:
                    return i

    def RightExercises(self) -> int:
        rightAnswers: int = 0
        block = self.getBlockFromExerciseNumber()
        for j in range(block.start-1, block.ends-1):
            if self.getNthExercise(j).getLastAnswer() == "1":
                rightAnswers += 1
        return rightAnswers

    def torturaEnds(self) -> None:
        date = datetime.datetime.now()
        hm = str(date.strftime("%H")) + ":" + str(date.strftime("%M")) + "." + str(date.strftime("%S"))
        self.ends = hm
        self.endOfBlock = "0"

    # kiszámolja a függvény egy adott csapat pontszámát
    def refreshPoint(self):
        alap: Sequence[int] = [32, 0, 0, 0, 0, 0]
        pontszamok: Sequence[float] = [0.0] * 16
        for ii in range(0, 5):
            jof = 0
            for i in range(Blokk[ii].start - 1, Blokk[ii].ends - 1):
                if self.getNthExercise(i).getNumOfAnswers() > 0:
                    csapat_i_feladat = self.getNthExercise(i)
                    if csapat_i_feladat.getLastAnswer() == "0" or csapat_i_feladat.getLastAnswer() == '':
                        pontszamok[i] = 0
                    else:
                        szam = 0
                        while (csapat_i_feladat.getNthAnswer(
                                csapat_i_feladat.getNumOfAnswers() - 1 - szam) == "1" and
                               csapat_i_feladat.getNumOfAnswers() - 1 - szam >= 0):
                            szam = szam + 1
                        if csapat_i_feladat.getNumOfAnswers() - szam == 0:
                            pontszamok[i] = alap[ii]
                        if csapat_i_feladat.getNumOfAnswers() - szam == 1:
                            pontszamok[i] = alap[ii] * 0.5
                        if csapat_i_feladat.getNumOfAnswers() - szam == 2:
                            pontszamok[i] = alap[ii] * 0.25
                        if csapat_i_feladat.getNumOfAnswers() - szam == 3:
                            pontszamok[i] = alap[ii] * 0.125
                        if csapat_i_feladat.getNumOfAnswers() - szam >= 4:
                            pontszamok[i] = alap[ii] * 0.0625
                        jof = jof + 1

            alap[ii + 1] = alap[ii] + jof * 8
        self.points = sum(pontszamok)
