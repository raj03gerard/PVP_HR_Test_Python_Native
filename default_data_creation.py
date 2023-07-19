from student import Student
from subject import Subject
from categories import Category, Student_Division, Subject_Type

default_student_divisions = {}
default_subject_types = {}


def create_default_categories():
    for defined_category in Category.__members__:

        passing_marks_for_division = input(
            f"Enter passing marks for {defined_category}")

        no_of_subjects_passing_marks = input(
            f"In how many subjects for {defined_category} category, should student have a total score more than {passing_marks_for_division} ? ")

        default_subject_types[defined_category] = Subject_Type(
            type=defined_category)
        default_student_divisions[defined_category] = Student_Division(division=defined_category,
                                                                       passing_marks=passing_marks_for_division,
                                                                       no_of_subjects_above_cutoff_to_pass=no_of_subjects_passing_marks)


def create_default_subjects():
    default_subjects = [
        Subject(title=' Maths',
                type=default_subject_types[Category.SCIENCE.name]),
        Subject(title=' General Science',
                type=default_subject_types[Category.SCIENCE.name]),
        Subject(title=' Biology',
                type=default_subject_types[Category.SCIENCE.name]),
        Subject(title=' Chemistry',
                type=default_subject_types[Category.SCIENCE.name]),
        Subject(title=' Japanese',
                type=default_subject_types[Category.HUMANITIES.name]),
        Subject(title=' History/Geography',
                type=default_subject_types[Category.HUMANITIES.name]),
        Subject(title=' English',
                type=default_subject_types[Category.HUMANITIES.name]),

    ]
    return default_subjects
