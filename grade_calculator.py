import os

FILE_NAME = "students.txt"


def calculate_grade(coursework, exam):
    final_mark = (0.4 * coursework) + (0.6 * exam)

    if final_mark >= 80:
        grade = "A"
    elif final_mark >= 70:
        grade = "B"
    elif final_mark >= 60:
        grade = "C"
    elif final_mark >= 50:
        grade = "D"
    else:
        grade = "F"

    return final_mark, grade


def get_valid_mark(prompt):
    while True:
        try:
            mark = float(input(prompt))
            if 0 <= mark <= 100:
                return mark
            else:
                print("❌ Enter a value between 0 and 100.")
        except ValueError:
            print("❌ Invalid input. Enter a number.")


def add_student():
    name = input("Enter student name: ")

    coursework = get_valid_mark("Enter coursework mark: ")
    exam = get_valid_mark("Enter exam mark: ")

    final_mark, grade = calculate_grade(coursework, exam)

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{coursework},{exam},{final_mark:.2f},{grade}\n")

    print("\n✅ Student saved successfully!")
    print(f"{name} - Final: {final_mark:.2f}, Grade: {grade}")


def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return

    print("\n--- Student Records ---")
    with open(FILE_NAME, "r") as file:
        for line in file:
            name, coursework, exam, final, grade = line.strip().split(",")
            print(f"{name} | CW: {coursework} | Exam: {exam} | Final: {final} | Grade: {grade}")


def menu():
    while True:
        print("\n=== Grade Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    menu()
