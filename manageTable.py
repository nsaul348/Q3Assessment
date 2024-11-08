import sqlite3

# Database file
DB_FILE = 'questions.db'

# Function to connect to the database
def connect():
    return sqlite3.connect(DB_FILE)

# Function to add a question to a specified table
def add_question(table_name, question, option_a, option_b, option_c, option_d, correct_answer):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f'''
        INSERT INTO {table_name} (question, option_a, option_b, option_c, option_d, correct_answer)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, option_a, option_b, option_c, option_d, correct_answer))
    conn.commit()
    print(f"Question added to {table_name}.")
    conn.close()

# Function to remove a question by ID from a specified table
def remove_question(table_name, question_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f'''
        DELETE FROM {table_name} WHERE id = ?
    ''', (question_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"Question with ID {question_id} removed from {table_name}.")
    else:
        print(f"No question found with ID {question_id} in {table_name}.")
    conn.close()

# Function to read and print all questions from a specified table
def read_questions(table_name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    if rows:
        print(f"\nQuestions in table '{table_name}':")
        for row in rows:
            print(f"ID: {row[0]}, Question: {row[1]}")
            print(f" A: {row[2]}")
            print(f" B: {row[3]}")
            print(f" C: {row[4]}")
            print(f" D: {row[5]}")
            print(f" Correct Answer: {row[6]}\n")
    else:
        print(f"No questions found in table '{table_name}'.")
    conn.close()

# Main function to interact with the user
def main():
    while True:
        print("\nChoose an operation:")
        print("1. Add a question")
        print("2. Remove a question")
        print("3. Read questions from a table")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            table_name = input("Enter the table name (e.g., DS3850, ExcelAnalytics, Marketing, etc.): ")
            question = input("Enter the question text: ")
            option_a = input("Enter option A: ")
            option_b = input("Enter option B: ")
            option_c = input("Enter option C: ")
            option_d = input("Enter option D: ")
            correct_answer = input("Enter the correct answer (A, B, C, or D): ")
            add_question(table_name, question, option_a, option_b, option_c, option_d, correct_answer)

        elif choice == '2':
            table_name = input("Enter the table name (e.g., DS3850, ExcelAnalytics, Marketing, etc.): ")
            question_id = int(input("Enter the ID of the question to remove: "))
            remove_question(table_name, question_id)

        elif choice == '3':
            table_name = input("Enter the table name (e.g., DS3850, ExcelAnalytics, Marketing, etc.): ")
            read_questions(table_name)

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
