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

    def remove_grade_by_index(self, index):
        """Remove the grade at the given index (starting at 0)."""
        if not 0 <= index < len(self.grades):
            raise IndexError(f"Index {index} is out of range.")
        del self.grades[index]

    def remove_grade_by_value(self, value):
        """Remove the first grade equal to the given value."""
        if value not in self.grades:
            raise ValueError(f"Grade {value} was not found.")
        self.grades.remove(value)

    def report(self):
        """Print the formatted summary report of the student."""
        print("=" * 30)
        print(f"Student ID:   {self.student_id}")
        print(f"Student Name: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Average:      {self.calculate_average():.2f}")
        print(f"Letter Grade: {self.get_letter_grade()}")
        print(f"Status:       {self.get_status()}")
        print(f"Honor Roll:   {self.is_honor_roll()}")
        print("=" * 30)

def main():
    """Run a demonstration of the Student class."""
    try:
        Student("S000", "")
    except ValueError as error:
        print(f"Error: {error}")

    ana = Student("S001", "Ana Perez")
    for grade in (100, "Fifty", 150, 95.5, 72.5):
        try:
            ana.add_grades(grade)
        except (TypeError, ValueError) as error:
            print(f"Error: {error}")

    try:
        ana.remove_grade_by_index(9)
    except IndexError as error:
        print(f"Error: {error}")

    try:
        ana.remove_grade_by_value(50)
    except ValueError as error:
        print(f"Error: {error}")

    ana.remove_grade_by_value(72.5)
    ana.report()

    luis = Student("S002", "Luis Mora")
    luis.add_grades(55)
    luis.add_grades(40.5)
    luis.report()


if __name__ == "__main__":
    main()
