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


def main():
    print("=== Student Grade Calculator ===")

    name = input("Enter student name: ")
    coursework = float(input("Enter coursework mark (0-100): "))
    exam = float(input("Enter exam mark (0-100): "))

    final_mark, grade = calculate_grade(coursework, exam)

    print("\n--- Results ---")
    print(f"Student: {name}")
    print(f"Final Mark: {final_mark:.2f}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()
