from categories import Category
from itertools import combinations


class Evaluate:
    total_passing_marks = 50

    def evaluate_by_total_score(subjects_list, total_passing_marks):

        total_marks = 0
        Evaluate.total_passing_marks = total_passing_marks

        for subject in subjects_list:
            total_marks += int(subject['marks'])

        print(
            f"Passing mark:  {Evaluate.total_passing_marks}, Total Marks obtained:  {total_marks}")

        if (total_marks >= Evaluate.total_passing_marks):

            return True
        else:

            return False

    def evaluate_by_student_division(student_division, subjects_list):
        division_passing_marks = int(
            student_division.division_passing_marks)

        marks_list = []
        no_of_subjects_above_cutoff_to_pass = int(
            student_division.no_of_subjects_above_cutoff_to_pass)
        for subject in subjects_list:

            if (student_division.division_name == subject['type'].subject_type):
                marks_list.append(int(subject['marks']))

        return Evaluate.are_marks_above_passing_marks(marks_list=marks_list,
                                                      no_of_subjects=no_of_subjects_above_cutoff_to_pass,
                                                      passing_marks=division_passing_marks)

    def are_marks_above_passing_marks(marks_list, no_of_subjects, passing_marks):
        for comb in combinations(marks_list, no_of_subjects):
            if (sum(comb) > passing_marks):
                print(
                    f"A combination of {no_of_subjects} subjects from {marks_list}, which are {comb} , have crossed {passing_marks} ")
                return True
        print(
            f"Any {no_of_subjects} subjects from {marks_list} have not crossed {passing_marks}")
        return False
