
from enum import Enum

# Defines what kind of categories students/ subjects can be classified into
# For every category, a default Student division of that type is created
# Similarly, for every category, a Subject type is created


class Category(Enum):
    SCIENCE = 1
    HUMANITIES = 2


class Student_Division:  # During data creation, every student's division will be created as a type of Student_Division

    def __init__(self, division, passing_marks, no_of_subjects_above_cutoff_to_pass):
        self.division_name = division
        self.division_passing_marks = passing_marks
        self.no_of_subjects_above_cutoff_to_pass = no_of_subjects_above_cutoff_to_pass


class Subject_Type:  # During data creation, every subject's type will be created as a type of Subject_Type
    def __init__(self, type):
        self.subject_type = type
