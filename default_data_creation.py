from student import Student
from subject import Subject
from categories import Category, Student_Division, Subject_Type

# This file contains methods that create the default data for the project as soon as the app runs

# As a starting point, it creates  default_student_divisions and default_subject_types for every Category(eg HUMANITIES, SCIENCE, etc).

# During the creation of subjects, each subject is assigned one of these default subject types.
# Similarly, during the creation of students, based on user input, every student is assigned one of these divisions

# This file also creates a list of default subjects that will be shared by every student object that gets created


default_student_divisions = {}
default_subject_types = {}


def create_default_categories():
    for defined_category in Category.__members__:

        passing_marks_for_division = input(
            f"Enter passing marks for {defined_category} :")
        passing_marks_for_division = int(
            passing_marks_for_division) if passing_marks_for_division.isdigit() else 200

        no_of_subjects_passing_marks = input(
            f"In how many subjects for {defined_category} category, should student have a total score more than {passing_marks_for_division} ? ")

        no_of_subjects_passing_marks = int(
            no_of_subjects_passing_marks) if no_of_subjects_passing_marks.isdigit() else 2

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
