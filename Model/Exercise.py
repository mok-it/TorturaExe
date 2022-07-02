
class Exercise:
    def __init__(self, numOfE):
        self.numOfExercise: int = numOfE
        self.results: str = ""
        self.additionalDatas: str = ""

    def getNumOfExercise(self) -> int:
        return self.numOfExercise

    def getConcatenatedForm(self) -> str:
        return self.results

    def getNumOfAnswers(self) -> int:
        return len(self.results)

    def getNthAnswer(self, num) -> str:
        return self.results[num]

    def getLastAnswer(self) -> str:
        return self.results[self.getNumOfAnswers() - 1]

    def getLLastAnswer(self) -> str:
        return self.results[self.getNumOfAnswers() - 2]

    def newSolution(self, sol: bool):
        if sol:
            self.results += "1"
        else:
            self.results += "0"
