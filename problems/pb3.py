def youngest_student(students):
    
    youngest_student = min(students, key=students.get)
    return(youngest_student)

students = {"Alice": 18, "Bob": 20, "Charlie": 19, "David": 22, "Jay": 20}
print(youngest_student(students))  # Expected output: "Alice"
