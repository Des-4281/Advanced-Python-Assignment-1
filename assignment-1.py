class Student:
    def __init__(self, name, email, grades):
        # Initialize the Student object with name, email, and grade
        self.name = name
        self.email = email
        self.grades = grades

    def add_grade(self, grades):
        # Add grades to the student's record
        self.grades.extend(grades)

    def average_grade(self):
        # Return the average of all grades
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        # Display the student's information
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")

    def grades_tuple(self):
        # Return the grades as a tuple
        return tuple(self.grades)
    
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

# Student Dictionary
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

# Get student by email function 

def get_student_by_email(email):
    return student_dict.get(email)

found_student = get_student_by_email("alice@hotmail.com")
if found_student:
    print(f"Student found: {found_student.name}")
else:   
    print("Student not found.")

# Create a set of unique grades from all students
unique_grades = set()
for student in students:
    unique_grades.update(student.grades)

print("Unique grades:", unique_grades)

# Convert grades to tuples and demonstrate immutability
grades_as_tuples = student1.grades_tuple()
print("Grades as tuple:", grades_as_tuples)

try: 
    grades_as_tuples[0] = 100
except TypeError as e:
    print("Tuples are immutable, so you cannot change their values.")

# Remove the last grade from each student 
for student in students:
    removed_grade = student.grades.pop()
    print(f"Removed grade {removed_grade} from {student.name}'s record.")

# Print the first and last grade for each student after removal
for student in students:
    print(f"{student.name}'s first grade: {student.grades[0]}")
    print(f"{student.name}'s last grade: {student.grades[-1]}")
    print(f"{student.name} has {len(student.grades)} grades.") 
    print ("-" * 30)

# Import the re module 
import re

# Function to validate email addresses using a regular expression pattern
def validate_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

# Loop through the students and validate their email addresses, printing the results
for student in students:
    if validate_email(student.email):
        print (f"{student.name}'s email is valid.")
    else:
        print (f"{student.name}'s email is invalid.")

count_above_90 = 0
for student in students:
    for grade in student.grades:
        if grade > 90:
            count_above_90 += 1

print(f"Number of grades above 90:", count_above_90)





