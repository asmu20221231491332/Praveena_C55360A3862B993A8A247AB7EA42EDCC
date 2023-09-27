def sort_students(student_list):
    # Sort the student list in descending order of CGPA
    sorted_students = sorted(student_list, key=lambda student: student['cgpa'], reverse=True)
    return sorted_students

# Define a list of student objects for testing
students = [
    {'name': 'Alice', 'roll_number': 'A123', 'cgpa': 3.8},
    {'name': 'Bob', 'roll_number': 'B456', 'cgpa': 3.5},
    {'name': 'Charlie', 'roll_number': 'C789', 'cgpa': 3.9},
    # Add more students as needed
]

# Test the function
sorted_students = sort_students(students)

# Print the sorted list
for student in sorted_students:
    print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, CGPA: {student['cgpa']}")