
from enum import Enum


class Category(Enum):
    SCIENCE = 1
    HUMANITIES = 2


class Student_Division:
    def __init__(self, division, passing_marks, no_of_subjects_above_cutoff_to_pass):
        self.division_name = division
        self.division_passing_marks = passing_marks
        self.no_of_subjects_above_cutoff_to_pass = no_of_subjects_above_cutoff_to_pass


class Subject_Type:
    def __init__(self, type):
        self.subject_type = type
