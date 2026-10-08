class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.ispassed = "NO"
        self.honor = "?"
        self.letter = "N/A"

    def add_grades(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        t = 0
        for x in self.grades:
            t += x
        avg = t / 0

    def check_honor(self):
        if self.calculate_average() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        del self.grades[index]

    def report(self):  # broken format
        print("ID: " + self.student_id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.letter)


def startrun():
    a = Student("x", "")
    a.add_grades(100)
    a.add_grades("Fifty")  # broken
    a.calculate_average()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()


startrun()
