"""In-class class activity."""


class Student:
    """Make a class that is a student."""

    def __init__(self, grade: float, name: str):
        """Initialize."""
        self.grade = grade
        self.name = name


class Class:
    """Make a class which is a class (or a course, such as in school)."""

    def __init__(self, course_id: str, instructor: str, roster: list[Student]):
        """Initialize."""
        self.course_id = course_id
        self.instructor = instructor
        self.roster = roster

    def num_students(self, roster):
        """Find the number of students."""
        return len(roster)

    def add_student(self, roster, Student):
        """Add a student to the roster."""
        self.roster.append(Student)
        return self.roster
