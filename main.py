from student import Student
from subject import Subject
from categories import Category, Student_Division, Subject_Type
from default_data_creation import create_default_categories, create_default_subjects, default_student_divisions, default_subject_types
from evaluate_result import Evaluate


def main():
    pass


def test():
    no_of_students = input("Enter no of students")
    if (no_of_students.isdigit() == False):
        print("Please enter valid integers")
        return

    total_passing_marks = int(input("Enter total passing marks"))

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

        else:
            break

        new_student_obj = Student(name=i, division=parsed_student_division)
        for sub in default_subjects:
            sub_marks = input(f"Enter marks for  {sub.title}")
            new_student_obj.add_subject_marks(subject=sub, marks=sub_marks)
        students_list.append(new_student_obj)

        i += 1

    print("")
    for student in students_list:
        print(
            f"---------------- Student {student.get_student_name()} results------------------------")
        print(f"Subjects: {student.get_student_subjects_as_str()}")
        if (Evaluate.evaluate_by_total_score(subjects_list=student.get_student_subjects(), total_passing_marks=total_passing_marks)
           and Evaluate.evaluate_by_student_division(student_division=student.get_student_division(), subjects_list=student.get_student_subjects())):
            print(
                f"RESULT: Student  {student.get_student_name()} who is a {student.get_student_division().division_name} student, has Passed")
        else:
            print(
                f"RESULT: Student  {student.get_student_name()} who is a {student.get_student_division().division_name} student, has Failed")

        print("===================================\n")


if __name__ == "__main__":
    test()
