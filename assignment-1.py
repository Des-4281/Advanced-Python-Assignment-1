class Student:
    def __init__(self, name, email, grade):
        # Initialize the Student object with name, email, and grade
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
    
# Create three Student objects with different names, emails, and grades
student1 = Student("Alice McNeely",  "alice@hotmail.com", [85, 90, 78])
student2 = Student("Bob James", "bob@yahoo.com", [92, 88, 95])
student3 = Student("Charlie Brown", "charlie@gmail.com", [56, 72, 91])

# Add additional grades to each student
student1.add_grade(82)
student1.add_grade(95)

student2.add_grade(89)
student2.add_grade(94)

student3.add_grade(31)
student3.add_grade(79)

# Display each student’s info and average
    
students = [student1, student2, student3]

for student in students:
    student.display_info()
    print(f"Average Grade: {student.average_grade():.2f}")
    print("-" * 30)

    

