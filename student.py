class Student:
    def __init__(self, name, division):
        self.__name = name
        self.__division = division
        self.__subjects = []

    def add_subject_marks(self, subject, marks):
        self.__subjects.append(
            {'subject': subject.title, 'marks': marks, 'type': subject.type})

    def get_student_name(self):
        return self.__name

    def get_student_division(self):
        return self.__division

    def get_student_subjects(self):
        return self.__subjects

    def get_student_subjects_as_str(self):

        subjects_as_str = "["
        for subject in self.__subjects:
            subjects_as_str += f"({subject['subject']}: {subject['marks']})"
        subjects_as_str += "]"
        return subjects_as_str
