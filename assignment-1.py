class Student:
    def __init__(self, name, age, grade):
        self.name = name 
        self.age = age
        self.grade = grade

    def add_grade(self, grade):
        # Add a grade to the student's record
        self.grade.append(grade)

    def average_grade(self):
        # Return the average of all grades
        if len(self.grade) == 0:
            return 0
        return sum(self.grade) / len(self.grade)

