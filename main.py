from student import Student
from subject import Subject
from type import Type, Student_Type, Subject_Type, default_student_types, default_subject_types
from default_data_creation import create_default_subjects, create_default_types
from evaluate_result import Evaluate


def main():
    pass


def test():
    no_of_students = input("Enter no of students")
    if (no_of_students.isdigit() == False):
        print("Please enter only valid integers")
        return

    total_passing_marks = int(input("Enter total passing marks"))

    create_default_types()
    default_subjects = create_default_subjects()

    students_list = []
    i = 0
    while (i < int(no_of_students)):
        student_type = input(
            "Enter student type: s for science, or h for humanities, f for fine_arts  : ")
        parsed_student_type = default_student_types[Type.HUMANITIES.name]
        if student_type == 's':
            parsed_student_type = default_student_types[Type.SCIENCE.name]
        elif student_type == 'h':
            parsed_student_type = default_student_types[Type.HUMANITIES.name]
        elif student_type == 'f':
            parsed_student_type = default_student_types[Type.FINE_ARTS.name]
        else:
            break

        new_student_obj = Student(name=i, type=parsed_student_type)
        for sub in default_subjects:
            sub_marks = input(f"Enter marks for  {sub.title}")
            new_student_obj.add_subject_marks(subject=sub, marks=sub_marks)
        students_list.append(new_student_obj)

        i += 1

    print("")
    for student in students_list:
        print(
            f"---------------- Student {student.name} results------------------------")
        print(f"Subjects: {student.get_subjects_str()}")
        if (Evaluate.evaluate_by_total_score(subjects=student.subjects, cutoff=total_passing_marks)
           and Evaluate.evaluate_by_student_type(student_type=student.type, subjects=student.subjects)):
            print(
                f"RESULT: Student  {student.name} who is a {student.type.student_type} student, has Passed")
        else:
            print(
                f"RESULT: Student  {student.name} who is a {student.type.student_type} student, has Failed")

        print("===================================\n")


if __name__ == "__main__":
    test()
