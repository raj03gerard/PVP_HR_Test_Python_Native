from student import Student
from categories import Category
from default_data_creation import create_default_categories, create_default_subjects, default_student_divisions, default_subject_types
from evaluate_result import Evaluate_Student_Result
import tkinter as tk
from gui_handler import GUI_Handler


def main():

    gui_handler = GUI_Handler()
    gui_handler.input_no_of_students()

    no_of_students = input("Enter no of students")
    if (no_of_students.isdigit() == False):
        print("Please enter a valid integer")
        return

    total_passing_marks = input(
        "Enter total passing marks- :")
    total_passing_marks = int(
        total_passing_marks) if total_passing_marks.isdigit() else 350

    create_default_categories()
    default_subjects = create_default_subjects()

    students_list = []

    i = 0
    while (i < int(no_of_students)):
        student_type = input(
            "Enter student type: s for science, or h for humanities  : ")
        parsed_student_division = default_student_divisions[Category.HUMANITIES.name]
        if student_type == 's':
            parsed_student_division = default_student_divisions[Category.SCIENCE.name]
        elif student_type == 'h':
            parsed_student_division = default_student_divisions[Category.HUMANITIES.name]

        new_student_obj = Student(name=i, division=parsed_student_division)
        for sub in default_subjects:
            sub_marks = input(f"Enter marks for  {sub.title}")
            if sub_marks.isdigit():
                sub_marks = int(sub_marks)
                sub_marks = max(min(sub_marks, 100), 0)
            else:
                sub_marks = 0
            new_student_obj.add_subject_marks(subject=sub, marks=sub_marks)
        students_list.append(new_student_obj)

        i += 1

    print("")
    display_evaluated_result(students_list, total_passing_marks)


def display_evaluated_result(students_list, total_passing_marks):
    no_of_passed_students = 0
    for student in students_list:
        print(
            f"---------------- Student {student.get_student_name()} results------------------------")
        print(f"Subjects: {student.get_student_subjects_as_str()}")

        has_student_passed = Evaluate_Student_Result.evaluate_student_result(student=student,
                                                                             total_passing_marks=total_passing_marks)

        if (has_student_passed):
            no_of_passed_students += 1
            print(
                f"RESULT: Student  {student.get_student_name()} who is a {student.get_student_division().division_name} student, has Passed")
        else:
            print(
                f"RESULT: Student  {student.get_student_name()} who is a {student.get_student_division().division_name} student, has Failed")

        print("===================================\n")

    print(f"-------No of students who passed: {no_of_passed_students}")


if __name__ == "__main__":
    main()
