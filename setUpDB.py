import sqlite3

# Function to create the database and tables, and insert questions
def create_database(db_file='questions.db'):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Create tables for each category
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS DS3850 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_answer TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ExcelAnalytics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_answer TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Marketing (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_answer TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Accounting (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_answer TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Finance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_answer TEXT NOT NULL
    )
    ''')

    # Sample questions for each category
    python_questions = [
    ("What is the correct syntax to output 'Hello, World' in Python?", 
     "echo('Hello, World')", "print('Hello, World')", "console.log('Hello, World')", "printf('Hello, World')", "B"),
    
    ("Which of the following is a correct variable name in Python?", 
     "1variable", "variable_name", "variable-name", "var name", "B"),
    
    ("Which keyword is used to create a function in Python?", 
     "function", "def", "fun", "define", "B"),
    
    ("What will be the output of the following code? \n\nprint(type(3))",
     "<class 'float'>", "<class 'int'>", "<class 'str'>", "<class 'bool'>", "B"),
    
    ("Which of the following is not a Python data type?",
     "list", "dictionary", "tuple", "array", "D"),
    
    ("How do you insert comments in Python code?",
     "// This is a comment", "/* This is a comment */", "# This is a comment", "<!-- This is a comment -->", "C"),
    
    ("What is the output of this code? \n\nx = [1, 2, 3]\nprint(len(x))",
     "1", "2", "3", "4", "C"),
    
    ("What will be the output of this code? \n\nprint(10 // 3)",
     "3.33", "3", "3.0", "Error", "B"),
    
    ("Which method can be used to convert a string to lowercase in Python?", 
     "lower()", "tolowercase()", "strtolower()", "toLowerCase()", "A"),
    
    ("Which of the following operators is used for exponentiation in Python?", 
     "^", "**", "//", "exp()", "B"),
    
    ("What does the 'len' function do in Python?",
     "Finds the length of a string", "Calculates the sum of numbers", "Converts to lowercase", "Rounds a number", "A"),
    
    ("What is the output of this code? \n\nx = 'Hello'\nprint(x[1])",
     "H", "e", "l", "o", "B"),
    
    ("What is the result of '5 + 3 * 2' in Python?", 
     "11", "16", "13", "10", "A"),
    
    ("Which of these is the correct syntax to open a file named 'file.txt' in read mode?", 
     "open('file.txt')", "open('file.txt', 'r')", "open('file.txt', 'read')", "open('file.txt', 'w')", "B"),
    
    ("Which function is used to generate random numbers in Python?", 
     "randomize()", "rand()", "random()", "generate_random()", "C"),
    
    ("Which module provides support for regular expressions in Python?", 
     "re", "regex", "exp", "expressions", "A"),
    
    ("Which of the following statements will check if 'x' is equal to 'y'?", 
     "x = y", "x == y", "x != y", "x equal y", "B"),
    
    ("What is the default return value of a function that doesn't return anything explicitly?", 
     "0", "None", "null", "Undefined", "B"),
    
    ("Which of the following can be used to handle exceptions in Python?", 
     "try/except", "catch/try", "handle/error", "throw/catch", "A"),
    
    ("Which loop is best to use when you know the exact number of iterations needed?", 
     "while loop", "for loop", "do-while loop", "None of the above", "B"),
    ]
    
    excel_questions = [
    ("Which Excel function is used to calculate the average of a range of numbers?", 
     "AVERAGE()", "SUM()", "MEAN()", "MEDIAN()", "A"),
    
    ("What is the function to find the maximum value in a range of cells?", 
     "MAXIMUM()", "LARGEST()", "MAX()", "HIGH()", "C"),
    
    ("Which of the following functions is used to count the number of cells that contain numbers?", 
     "COUNT()", "COUNTA()", "COUNTIF()", "COUNTALL()", "A"),
    
    ("What is the shortcut to create a chart from selected data in Excel?", 
     "Alt + C", "F11", "Ctrl + C", "Shift + F3", "B"),
    
    ("Which function is used to join text from multiple cells in Excel?", 
     "JOIN()", "TEXTJOIN()", "CONCAT()", "MERGE()", "C"),
    
    ("What type of chart is best for showing trends over time?", 
     "Pie Chart", "Line Chart", "Bar Chart", "Scatter Plot", "B"),
    
    ("Which Excel feature allows you to apply a condition to format cells?", 
     "Data Validation", "Filter", "Conditional Formatting", "Sort", "C"),
    
    ("What function would you use to look up a value in the first column of a table and return a value in the same row?", 
     "MATCH()", "LOOKUP()", "VLOOKUP()", "SEARCH()", "C"),
    
    ("Which function would you use to calculate the standard deviation of a data set in Excel?", 
     "STD()", "STDEV()", "STANDARDDEV()", "SD()", "B"),
    
    ("In a Pivot Table, which field setting would you use to find the total of values in a category?", 
     "Average", "Sum", "Count", "Product", "B"),
    
    ("Which function can be used to determine if two values are exactly equal?", 
     "COMPARE()", "MATCH()", "EQUALS()", "EXACT()", "D"),
    
    ("What Excel tool allows you to filter data based on multiple criteria?", 
     "Sort", "Data Validation", "Conditional Formatting", "Advanced Filter", "D"),
    
    ("How do you calculate the percentage change between two values in Excel?", 
     "=(New Value - Old Value)", "=(New Value / Old Value)", "=(New Value - Old Value) / Old Value", "=(New Value - Old Value) * 100", "C"),
    
    ("What is the function to find the smallest value in a range of cells?", 
     "MIN()", "LOWEST()", "MINIMUM()", "LEAST()", "A"),
    
    ("Which of these functions can be used to round a number to the nearest integer?", 
     "ROUNDUP()", "ROUNDDOWN()", "ROUND()", "NEAREST()", "C"),
    
    ("What feature would you use to quickly find duplicates in a data range?", 
     "Filter", "Remove Duplicates", "Find", "Sort", "B"),
    
    ("Which function can count the number of blank cells in a range?", 
     "COUNTBLANK()", "COUNTA()", "ISBLANK()", "COUNT()", "A"),
    
    ("What is the purpose of the 'Freeze Panes' option in Excel?", 
     "To lock specific rows and columns for easy navigation", 
     "To prevent editing cells", 
     "To highlight cells", 
     "To create a table", "A"),
    
    ("In a Pivot Table, which field area would you place a field to create row labels?", 
     "Filter", "Rows", "Columns", "Values", "B"),
    
    ("Which Excel function returns the current date and time?", 
     "DATE()", "NOW()", "TODAY()", "CURRENT()", "B"),
    ]

    marketing_questions = [
    ("What are the '4 Ps' of marketing?", 
     "Product, Place, Promotion, Price", 
     "Product, Price, People, Process", 
     "Product, Positioning, Place, Promotion", 
     "Promotion, Process, Product, Price", 
     "A"),

    ("What is the primary purpose of market segmentation?", 
     "To increase production", 
     "To better understand competitors", 
     "To identify and target specific customer groups", 
     "To reduce advertising costs", 
     "C"),

    ("Which of the following best describes a target market?", 
     "A group of products in the same category", 
     "A group of customers most likely to buy a product", 
     "All people within a geographic area", 
     "A list of competitors", 
     "B"),

    ("What is a 'brand'?", 
     "A product or service offered at a low price", 
     "The name, term, design, or feature that identifies a product", 
     "A type of marketing research method", 
     "A label on a product", 
     "B"),

    ("Which type of marketing strategy involves selling existing products in new markets?", 
     "Market Penetration", 
     "Product Development", 
     "Market Development", 
     "Diversification", 
     "C"),

    ("What is the main purpose of the marketing mix?", 
     "To create and deliver value to customers", 
     "To increase product costs", 
     "To design packaging for a product", 
     "To advertise a product on social media", 
     "A"),

    ("What does 'B2B' stand for in marketing?", 
     "Business to Buyer", 
     "Business to Business", 
     "Buyer to Buyer", 
     "Brand to Brand", 
     "B"),

    ("Which of the following is a characteristic of a 'niche market'?", 
     "It is broad and includes many customer segments", 
     "It targets a small, specific group of customers", 
     "It has high competition levels", 
     "It is not suitable for specialized products", 
     "B"),

    ("What is the role of 'marketing research'?", 
     "To develop the pricing strategy", 
     "To create social media content", 
     "To gather information about customers and market conditions", 
     "To design product packaging", 
     "C"),

    ("Which of the following best describes 'customer relationship management' (CRM)?", 
     "A strategy for managing a company's relationships with potential and existing customers", 
     "A strategy to maximize production output", 
     "A method to evaluate competitors", 
     "A process of selecting suppliers", 
     "A")
    ]

    accounting_questions = [
    ("What is the accounting equation?", 
     "Assets = Liabilities + Owner's Equity", 
     "Assets = Liabilities - Owner's Equity", 
     "Assets = Revenue - Expenses", 
     "Assets = Liabilities + Revenue", 
     "A"),

    ("Which financial statement shows a company's revenues and expenses?", 
     "Balance Sheet", 
     "Income Statement", 
     "Cash Flow Statement", 
     "Statement of Owner's Equity", 
     "B"),

    ("What type of account is 'Accounts Receivable'?", 
     "Liability", 
     "Asset", 
     "Expense", 
     "Revenue", 
     "B"),

    ("What does 'GAAP' stand for in accounting?", 
     "Generally Accepted Accounting Principles", 
     "Global Accepted Accounting Practices", 
     "Generally Accepted Auditing Principles", 
     "General Accounting and Auditing Practices", 
     "A"),

    ("Which of the following best describes 'accrual accounting'?", 
     "Recording revenue when cash is received", 
     "Recording revenue when it is earned, regardless of cash receipt", 
     "Recording expenses only when paid", 
     "Recording only cash transactions", 
     "B"),

    ("In a double-entry accounting system, every transaction affects:", 
     "One account only", 
     "At least two accounts", 
     "All accounts in the ledger", 
     "Only income and expense accounts", 
     "B"),

    ("Which account is increased by credits?", 
     "Assets", 
     "Liabilities", 
     "Expenses", 
     "Withdrawals", 
     "B"),

    ("What is depreciation?", 
     "The increase in value of an asset over time", 
     "The reduction in value of an asset over time", 
     "The reduction in an asset's liability", 
     "An increase in the owner’s equity", 
     "B"),

    ("Which financial statement shows a company's financial position at a specific point in time?", 
     "Income Statement", 
     "Statement of Cash Flows", 
     "Balance Sheet", 
     "Statement of Retained Earnings", 
     "C"),

    ("What is the purpose of a 'trial balance'?", 
     "To ensure total debits equal total credits", 
     "To show the company’s net income", 
     "To determine cash flow", 
     "To assess asset values", 
     "A")
    ]


    finance_questions = [
    ("What is the primary goal of corporate finance?", 
     "Maximizing sales", 
     "Minimizing costs", 
     "Maximizing shareholder value", 
     "Reducing debt", 
     "C"),

    ("Which of the following is considered a long-term liability?", 
     "Accounts Payable", 
     "Short-term loan", 
     "Bonds Payable", 
     "Accrued expenses", 
     "C"),

    ("What does 'ROI' stand for?", 
     "Return on Investment", 
     "Rate of Interest", 
     "Return on Income", 
     "Revenue of Investment", 
     "A"),

    ("Which of the following best describes 'liquidity'?", 
     "The ability to convert assets into cash quickly", 
     "The ability to generate high profits", 
     "The measure of long-term debt", 
     "The total market value of assets", 
     "A"),

    ("What is 'capital budgeting'?", 
     "The process of tracking expenses and revenues", 
     "The process of evaluating and selecting long-term investments", 
     "The process of preparing a company's budget", 
     "The process of managing short-term cash flow", 
     "B"),

    ("Which of the following is an example of a capital asset?", 
     "Cash", 
     "Inventory", 
     "Real estate", 
     "Accounts Receivable", 
     "C"),

    ("What is a 'bond' in finance?", 
     "A long-term loan made to a company or government", 
     "A short-term investment in stock", 
     "A type of asset only available to banks", 
     "An ownership share in a company", 
     "A"),

    ("What is 'diversification' in finance?", 
     "Investing in one type of asset to maximize returns", 
     "Allocating resources in multiple assets to reduce risk", 
     "Buying only high-risk assets", 
     "Selling assets to generate cash", 
     "B"),

    ("What does 'NPV' stand for in finance?", 
     "Net Profit Value", 
     "New Product Venture", 
     "Net Present Value", 
     "Net Profit Variance", 
     "C"),

    ("Which of the following best describes 'equity'?", 
     "The amount of cash a company holds", 
     "The total debt a company owes", 
     "The value of ownership interest in the company", 
     "The company’s gross revenue", 
     "C")
    ]


    # Function to insert questions into a specified table
    def insert_questions(table_name, questions):
        for question in questions:
            cursor.execute(f'''
            INSERT INTO {table_name} (question, option_a, option_b, option_c, option_d, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', question)
        conn.commit()

    # Insert questions into the tables
    insert_questions('DS3850', python_questions)
    insert_questions('ExcelAnalytics', excel_questions)
    insert_questions('Marketing', marketing_questions)
    insert_questions('Accounting', accounting_questions)
    insert_questions('Finance', finance_questions)
    print("Questions have been inserted into the DS3850, ExcelAnalytics, Marketing, Accounting, and Finance tables.")
    
    # Close the connection
    conn.close()


# Function to read tables and data from the database
def read_database(db_file='questions.db'):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Retrieve all table names in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    # Print all tables
    print("Tables in the database:")
    for idx, table in enumerate(tables):
        print(f"{idx + 1}. {table[0]}")
    
    # Ask the user to select a table
    table_index = int(input("Enter the number of the table you want to view: ")) - 1
    selected_table = tables[table_index][0]
    
    # Retrieve and print all data from the selected table
    print(f"\nData from table '{selected_table}':")
    cursor.execute(f"SELECT * FROM {selected_table}")
    rows = cursor.fetchall()
    
    # Print column headers
    column_names = [description[0] for description in cursor.description]
    print("\t".join(column_names))
    
    # Print each row of data
    for row in rows:
        print("\t".join(str(cell) for cell in row))
    
    # Close the connection
    conn.close()


# Run the functions
create_database()
read_database()
