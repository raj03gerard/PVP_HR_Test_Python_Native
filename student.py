from subject import Subject
from type import Type


class Student:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.subjects = []

    def add_subject_marks(self, subject, marks):
        self.subjects.append(
            {'subject': subject.title, 'marks': marks, 'type': subject.type})

    def get_all_subjects(self):
        return self.subjects

    def print_student(self):
        print(self.name, " ", self.type.student_type, " ", self.subjects)

    def get_subjects_str(self):

        subjects_as_str = "["
        for subject in self.subjects:
            subjects_as_str += f"({subject['subject']}: {subject['marks']})"
        subjects_as_str += "]"
        return subjects_as_str
