from categories import Category
from itertools import combinations


class Evaluate:
    total_passing_marks = 50

    def evaluate_by_total_score(subjects, cutoff):

        total_marks = 0
        Evaluate.total_passing_marks = cutoff

        for subject in subjects:
            if subject != None:
                total_marks += int(subject['marks'])

        print(
            f"Passing mark:  {Evaluate.total_passing_marks}, Total Marks obtained:  {total_marks}")

        if (total_marks >= Evaluate.total_passing_marks):

            return True
        else:

            return False

    def evaluate_by_student_division(student_division, subjects):
        division_passing_marks = int(
            student_division.student_division_passing_marks)

        marks_list = []
        no_of_subjects_above_cutoff_to_pass = int(
            student_division.no_of_subjects_above_cutoff_to_pass)
        for subject in subjects:

            if (student_division.student_division == subject['type'].subject_type):
                marks_list.append(int(subject['marks']))

        return Evaluate.check_subjects_greater_than_cutoff(marks_list=marks_list,
                                                           no_of_subjects=no_of_subjects_above_cutoff_to_pass,
                                                           cutoff=division_passing_marks)

    def check_subjects_greater_than_cutoff(marks_list, no_of_subjects, cutoff):
        for comb in combinations(marks_list, no_of_subjects):
            if (sum(comb) > cutoff):
                print(
                    f"A combination of {no_of_subjects} subjects from {marks_list}, which are {comb} , have crossed {cutoff} ")
                return True
        print(
            f"Any {no_of_subjects} subjects from {marks_list} have not crossed {cutoff}")
        return False
