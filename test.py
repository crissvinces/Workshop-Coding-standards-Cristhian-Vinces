"""Students grades management system"""

class Student:
    """Represents a student with ID, name, and a list of grades"""

    MIN_GRADE = 0
    MAX_GRADE=100
    A_MIN = 90
    B_MIN = 80
    C_MIN = 70
    PASSING_GRADE = 60
    HONOR_ROLL_GRADE = 90

    def __init__(self, student_id, name):
        """Initialize a student with a given ID and name"""

        if not str(student_id).strip():
            raise ValueError("Student ID cannot be empty")
        if not str(name).strip():
            raise ValueError("Student name cannot be empty.")
        self.student_id = student_id.strip()
        self.name = name.strip()
        self.grades = []
        

    def add_grades(self, grade):
        """Add grades to the student beteeen 0 and 100"""

        if isinstance(grade, bool) or not isinstance(grade, (int, float)):
            raise TypeError(f"Grade must be a number, got {grade!r}.")
        if not self.MIN_GRADE <= grade <= self.MAX_GRADE:
            raise ValueError(
                f"Grade must be between {self.MIN_GRADE} and {self.MAX_GRADE}."
            )

        self.grades.append(grade)

    def calculate_average(self):
        """Calculate the average of the students grades, 0 if there are none"""

        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        """Return the letter grade based on the average."""
        average = self.calculate_average()
        if average >= self.A_MIN:
            return "A"
        if average >= self.B_MIN:
            return "B"
        if average >= self.C_MIN:
            return "C"
        if average >= self.PASSING_GRADE:
            return "D"
        return "F"

    def get_status(self):
        """Return 'Passed' if the average is 60 or higher, else 'Failed'."""
        if self.calculate_average() >= self.PASSING_GRADE:
            return "Passed"
        return "Failed"

    def is_honor_roll(self):
        """Return True if the average is 90 or higher, else False."""
        return self.calculate_average() >= self.HONOR_ROLL_GRADE

    def delete_grade(self, index):
        """Delete the grades that have in index"""
        del self.grades[index]

    def report(self):  # broken format
        """Print the student report"""

        print("ID: " + self.student_id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.get_letter_grade())


def startrun():
    """Run a demonstration of the class Student"""
    a = Student("x", "")
    a.add_grades(100)
    a.add_grades("Fifty")  # broken
    a.calculate_average()
    a.delete_grade(5)  # IndexError
    a.report()


startrun()
