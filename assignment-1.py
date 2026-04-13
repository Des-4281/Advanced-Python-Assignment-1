class Student:
    def __init__(self, name, grade, email):
        self.name = name
        self.email = email
        self.grade = grade

    def add_grade(self, grade):
        # Add a grade to the student's record
        self.grade.append(grade)

    def average_grade(self):
        # Return the average of all grades
        if len(self.grade) == 0:
            return 0
        return sum(self.grade) / len(self.grade)

    def display_info(self):
        # Display the student's information
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grade}")

    def grades_tuple(self):
        # Return the grades as a tuple
        return tuple(self.grade)
    
    

    