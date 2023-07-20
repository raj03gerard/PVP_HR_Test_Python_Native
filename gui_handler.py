import tkinter as tk


class GUI_Handler:
    def __init__(self):
        self.root = tk.Tk()
        self.enter_students_no_label = tk.Label(
            self.root, text="Enter no of students:")
        self.enter_no_of_students_entry = tk.Entry(self.root)
        self.save_no_of_students_button = tk.Button(
            self.root, text="Submit", command=self.submit)

        self.no_of_students = tk.IntVar()
        self.no_of_students_label = tk.Label(
            self.root, textvariable=self.no_of_students)

        self.enter_total_passing_marks_label = tk.Label(
            self.root, text="Enter total passing marks:")
        self.total_passing_marks_entry = tk.Entry(self.root)
        self.save_total_passing_marks = tk.Button(
            self.root, text="Submit", command=self.submit_total_passing_marks)
        self.total_passing_marks = tk.IntVar()

        window_width = 300
        window_height = 150
        self.root.geometry(f"{window_width}x{window_height}")

    def submit(self):
        self.no_of_students.set(self.enter_no_of_students_entry.get())
        self.input_total_passing_marks()

    def input_no_of_students(self):
        self.enter_students_no_label.pack()
        self.enter_no_of_students_entry.pack()
        self.save_no_of_students_button.pack()

        self.no_of_students_label.pack()

        self.root.mainloop()

    def input_total_passing_marks(self):
        self.enter_total_passing_marks_label.pack()
        self.total_passing_marks_entry.pack()
        self.save_total_passing_marks.pack()
        self.root.mainloop()

    def submit_total_passing_marks(self):
        self.total_passing_marks.set(self.total_passing_marks_entry.get())
        print(self.total_passing_marks)
