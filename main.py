import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class Question:
    def __init__(self, question_text, option_a, option_b, option_c, option_d, correct_answer):
        self.question_text = question_text
        self.options = {
            "A": option_a,
            "B": option_b,
            "C": option_c,
            "D": option_d,
        }
        self.correct_answer = correct_answer

    def display(self, quiz_window, answer_var):
        """
        Display the question and options in the given window.
        """
        # Display the question text with wraplength to ensure it doesn't get cut off
        question_label = tk.Label(quiz_window, text=self.question_text, font=("Arial", 14), wraplength=550)
        question_label.pack(pady=10)

        # Display answer options as labels above the dropdown
        for key, value in self.options.items():
            option_label = tk.Label(quiz_window, text=f"{key}: {value}", font=("Arial", 12))
            option_label.pack(anchor="w", padx=20)

        # Dropdown menu for answer selection
        answer_var.set("Select your answer")  # Placeholder text
        answer_menu = ttk.Combobox(quiz_window, textvariable=answer_var, values=list(self.options.keys()), font=("Arial", 12))
        answer_menu.pack(pady=10)

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

def open_category_selection():
    global main_window
    main_window = tk.Tk()
    main_window.title("Select Quiz Category")
    main_window.geometry("400x300")

    tk.Label(main_window, text="Choose a category:", font=("Arial", 14)).pack(pady=10)
    category = tk.StringVar()
    category_menu = ttk.Combobox(main_window, textvariable=category, values=["DS3850", "Marketing", "Accounting", "Finance", "ExcelAnalytics"], font=("Arial", 12))
    category_menu.pack(pady=5)

    start_button = tk.Button(main_window, text="Start Quiz Now", font=("Arial", 12), command=lambda: open_quiz_window(category.get()))
    start_button.pack(pady=20)

def open_quiz_window(category):
    main_window.destroy()
    quiz_window = tk.Tk()
    quiz_window.title("Quiz Time!")
    quiz_window.geometry("800x400")  # Adjusted width for text wrapping

    conn = sqlite3.connect("questions.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT question, option_a, option_b, option_c, option_d, correct_answer FROM {category} LIMIT 10")
    questions_data = cursor.fetchall()
    conn.close()

    questions = [Question(*q) for q in questions_data]
    current_question_index = [0]
    answer_var = tk.StringVar()

    def display_question():
        for widget in quiz_window.winfo_children():
            widget.destroy()

        answer_var.set("Select your answer")  # Reset the selection

        if current_question_index[0] < len(questions):
            current_question = questions[current_question_index[0]]
            current_question.display(quiz_window, answer_var)

            submit_button = tk.Button(quiz_window, text="Submit Answer", font=("Arial", 12), command=lambda: submit_answer(answer_var.get()))
            submit_button.pack(pady=20)
        else:
            messagebox.showinfo("Quiz Complete", "You've completed the quiz!")
            quiz_window.destroy()
            open_category_selection()

    def submit_answer(selected_answer):
        current_question = questions[current_question_index[0]]
        if current_question.check_answer(selected_answer):
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", "Incorrect. Try Again.")

        current_question_index[0] += 1
        display_question()

    display_question()

open_category_selection()
main_window.mainloop()
