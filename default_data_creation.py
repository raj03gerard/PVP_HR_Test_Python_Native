from student import Student
from subject import Subject
from type import Type, Student_Type, Subject_Type, default_student_types, default_subject_types


def create_default_types():
    for defined_type in Type.__members__:
        passing_marks_for_type = input(
            f"Enter passing marks for {defined_type}")
        no_of_subjects_passing_marks = input(
            f"Enter no of subjects in which the passing marks need to be scored for {defined_type}")

        default_subject_types[defined_type] = Subject_Type(type=defined_type)
        default_student_types[defined_type] = Student_Type(type=defined_type,
                                                           passing_marks=passing_marks_for_type,
                                                           no_of_subjects_above_cutoff_to_pass=no_of_subjects_passing_marks)


def create_default_subjects():
    default_subjects = [
        Subject(title=' Maths', type=default_subject_types[Type.SCIENCE.name]),
        Subject(title=' General Science',
                type=default_subject_types[Type.SCIENCE.name]),
        Subject(title=' Biology',
                type=default_subject_types[Type.SCIENCE.name]),
        Subject(title=' Chemistry',
                type=default_subject_types[Type.SCIENCE.name]),
        Subject(title=' Japanese',
                type=default_subject_types[Type.HUMANITIES.name]),
        Subject(title=' History/Geography',
                type=default_subject_types[Type.HUMANITIES.name]),
        Subject(title=' English',
                type=default_subject_types[Type.HUMANITIES.name]),

    ]
    return default_subjects
