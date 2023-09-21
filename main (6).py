#unit 3 challenge 3.2 test the function with different input list of students
students = []
def add_student(name, roll_number, cgpa):
    student = {
        'name': name,
        'roll_number': roll_number,
        'cgpa': cgpa
    }
    students.append(student)
def sort_students():
    students.sort(key=lambda x: x['roll_number'])
# Example usage:
add_student('Alice', 1, 3.8)
add_student('Bob', 3, 3.5)
add_student('Charlie', 2, 3.7)
sort_students()
for student in students:
    print(student)

