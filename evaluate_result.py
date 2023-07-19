from categories import Category
from itertools import combinations

# It contains the methods that evaluate the passing or failure of every student. The passing or failure of a student depends on multiple test conditions,
# For every test condition, there is a method that evaluates to true or false.
# As per the specified test conditions, the methods evaluate_by_total_score() and evaluate_by_student_division() check each test condition


class Evaluate_Student_Result:
    total_passing_marks = 50

#  evaluate_student_result() method checks whether a student has failed or not by running it through all the test conditions.
#  This also means that additional test conditions can be added, and can simply be chained to the contents of evaluate_student_result(),
#  without having to affect any other classes or files

    def evaluate_student_result(student, total_passing_marks):
        has_passed_by_total_score = Evaluate_Student_Result.evaluate_by_total_score(
            subjects_list=student.get_student_subjects(),
            total_passing_marks=total_passing_marks)

        has_passed_by_division_score = Evaluate_Student_Result.evaluate_by_student_division(
            student_division=student.get_student_division(),
            subjects_list=student.get_student_subjects())

        return has_passed_by_total_score and has_passed_by_division_score

    def evaluate_by_total_score(subjects_list, total_passing_marks):

        total_marks = 0
        Evaluate_Student_Result.total_passing_marks = total_passing_marks

        for subject in subjects_list:
            total_marks += int(subject['marks'])

        print(
            f"Condition1: Passing mark:  {Evaluate_Student_Result.total_passing_marks}, Total Marks obtained:  {total_marks}")

        if (total_marks >= Evaluate_Student_Result.total_passing_marks):

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

        are_marks_greater_than_passing_marks = Evaluate_Student_Result.are_marks_above_passing_marks(marks_list=marks_list,
                                                                                                     no_of_subjects=no_of_subjects_above_cutoff_to_pass,
                                                                                                     passing_marks=division_passing_marks)
        if (are_marks_greater_than_passing_marks):
            print(
                f"Condition2: A combination of {no_of_subjects_above_cutoff_to_pass} subjects from {marks_list},  have crossed {division_passing_marks} ")
        else:
            print(
                f"Condition2 : Any {no_of_subjects_above_cutoff_to_pass} subjects from {marks_list} have not crossed {division_passing_marks}")

        return are_marks_greater_than_passing_marks

    def are_marks_above_passing_marks(marks_list, no_of_subjects, passing_marks):
        for comb in combinations(marks_list, no_of_subjects):
            if (sum(comb) > passing_marks):
                return True
        return False
