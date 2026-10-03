students = []

def add_student():
    name = input("Enter student name: ")
    students.append({"name": name, "attendance": "Absent"})
    print("Student added successfully!")


def mark_attendance():
    name = input("Enter student name: ")

    for student in students:
        if student["name"] == name:
            student["attendance"] = "Present"
            print("Attendance marked successfully!")
            return

    print("Student not found!")


def display_report():
    print("\n----- Attendance Report -----")

    if len(students) == 0:
        print("No students added.")
    else:
        for student in students:
            print(student["name"], "-", student["attendance"])


while True:
    print("\n===== Attendance Management System =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. Display Report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        mark_attendance()

    elif choice == "3":
        display_report()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")