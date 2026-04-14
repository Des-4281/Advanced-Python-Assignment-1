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
student4 = Student("John Barker", "john.gmail", [65, 83, 95]) # Invalid email for testing

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
    student1.name: student1,
    student2.name: student2,
    student3.name: student3,
    student4.name: student4
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
    unique_grades.update(student.grade)
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
    removed_grade = student.grade.pop()
    print(f"Removed grade {removed_grade} from {student.name}'s record.")

# Print the first and last grade for each student after removal
for student in students:
    print(f"{student.name}'s first grade: {student.grade[0]}")
    print(f"{student.name}'s last grade: {student.grade[-1]}")
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
    for grade in student.grade:
        if grade > 90:
            count_above_90 += 1

print(f"Number of grades above 90:", count_above_90)






