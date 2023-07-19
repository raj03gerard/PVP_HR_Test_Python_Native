
class Student:
    def __init__(self, name, division):  # member variables are marked as private
        self.__name = name
        self.__division = division
        self.__subjects = []

    def add_subject_marks(self, subject, marks):  # Adds new subject data
        self.__subjects.append(
            {'subject': subject.title, 'marks': marks, 'type': subject.type})

    # getter for name
    def get_student_name(self):
        return self.__name

    # getter for division
    def get_student_division(self):
        return self.__division

    # getter for subjects
    def get_student_subjects(self):
        return self.__subjects

    # converts subjects into a formatted string for display purposes
    def get_student_subjects_as_str(self):

        subjects_as_str = "["
        for subject in self.__subjects:
            subjects_as_str += f"({subject['subject']}: {subject['marks']})"
        subjects_as_str += "]"
        return subjects_as_str
