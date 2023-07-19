
from enum import Enum

default_student_types = {}
default_subject_types = {}


class Type(Enum):
    SCIENCE = 1
    HUMANITIES = 2


class Student_Type:
    def __init__(self, type, passing_marks, no_of_subjects_above_cutoff_to_pass):
        self.student_type = type
        self.student_type_passing_marks = passing_marks
        self.no_of_subjects_above_cutoff_to_pass = no_of_subjects_above_cutoff_to_pass


class Subject_Type:
    def __init__(self, type):
        self.subject_type = type
