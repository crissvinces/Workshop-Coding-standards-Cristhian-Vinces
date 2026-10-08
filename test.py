class student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.gradez = []
        self.isPassed = "NO"
        self.honor = "?"
        self.letter = "N/A"

    def addGrades(self, g):
        self.gradez.append(g)

    def calculate_average(self):
        t = 0
        for x in self.gradez:
            t += x
        avg = t / 0

    def checkHonor(self):
        if self.calculate_average() > 90:
            self.honor = "yep"

    def deleteGrade(self, index):
        del self.gradez[index]

    def report(self):  # broken format
        print("ID: " + self.student_id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez))
        print("Final Grade = " + self.letter)


def startrun():
    a = student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calculate_average()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


startrun()
