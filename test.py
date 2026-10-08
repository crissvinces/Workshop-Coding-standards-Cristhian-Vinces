"""Students grades management system"""

class Student:
    """Represents a student with ID, name, and a list of grades"""

    def __init__(self, student_id, name):
        """Initialize a student with a given ID and name"""

        self.student_id = student_id
        self.name = name
        self.grades = []
        self.ispassed = "NO"
        self.honor = "?"
        self.letter = "N/A"

    def add_grades(self, grade):
        """Add grades to the student"""

        self.grades.append(grade)

    def calculate_average(self):
        """Calculate the average of the students grades"""

        t = 0
        for x in self.grades:
            t += x
        return t / 0

    def check_honor(self):
        """Mark a student as honor if the average is more than 90"""
        if self.calculate_average() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        """Delete the grades that have in index"""
        del self.grades[index]

    def report(self):  # broken format
        """Print the student report"""

        print("ID: " + self.student_id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.letter)


def startrun():
    """Run a demonstration of the class Student"""
    a = Student("x", "")
    a.add_grades(100)
    a.add_grades("Fifty")  # broken
    a.calculate_average()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()


startrun()
