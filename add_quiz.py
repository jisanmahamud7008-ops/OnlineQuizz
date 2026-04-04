import oracledb

# Delete existing
conn = oracledb.connect(
    user="quiz_user", password="234208", dsn="localhost:1521/XEPDB1"
)
cursor = conn.cursor()
cursor.execute(
    "DELETE FROM quizzes_choice WHERE question_id IN (SELECT id FROM quizzes_question WHERE quiz_id IN (SELECT id FROM quizzes_quiz WHERE title IN ('Python Basics', 'JavaScript Basics')))"
)
cursor.execute(
    "DELETE FROM quizzes_student_answer WHERE attempt_id IN (SELECT id FROM quizzes_attempt WHERE quiz_id IN (SELECT id FROM quizzes_quiz WHERE title IN ('Python Basics', 'JavaScript Basics')))"
)
cursor.execute(
    "DELETE FROM quizzes_attempt WHERE quiz_id IN (SELECT id FROM quizzes_quiz WHERE title IN ('Python Basics', 'JavaScript Basics'))"
)
cursor.execute(
    "DELETE FROM quizzes_question WHERE quiz_id IN (SELECT id FROM quizzes_quiz WHERE title IN ('Python Basics', 'JavaScript Basics'))"
)
cursor.execute(
    "DELETE FROM quizzes_quiz WHERE title IN ('Python Basics', 'JavaScript Basics')"
)
conn.commit()
conn.close()
print("Deleted existing")

# Python quiz
conn = oracledb.connect(
    user="quiz_user", password="234208", dsn="localhost:1521/XEPDB1"
)
cursor = conn.cursor()
cursor.execute("SELECT quizzes_quiz_seq.NEXTVAL FROM DUAL")
cursor.fetchone()
cursor.execute(
    "INSERT INTO quizzes_quiz (title, description, created_by_id, created_at, is_active) VALUES ('Python Basics', 'Test your Python programming skills with 20 basic questions', 1, SYSDATE, 1)"
)
cursor.execute("SELECT quizzes_quiz_seq.CURRVAL FROM DUAL")
python_quiz_id = cursor.fetchone()[0]
conn.commit()
conn.close()
print(f"Python quiz: {python_quiz_id}")

# Python questions
python_questions_text = [
    "What is the correct way to create a variable in Python?",
    "Which data type is used to store text in Python?",
    "What is the output of: print(type(3.14))?",
    "Which operator is used for integer division in Python?",
    "What is the correct way to write a comment in Python?",
    "Which function is used to get input from user in Python?",
    "What is the output of: len([1, 2, 3])?",
    "Which method is used to add an element to a list?",
    "What is the output of: print(2 ** 3)?",
    "Which keyword is used to define a function in Python?",
    "What is the correct syntax for a for loop in Python?",
    "Which operator is used for string concatenation?",
    'What is the output of: print("Hello" * 2)?',
    "Which method converts a string to uppercase?",
    "What is a dictionary in Python?",
    "Which keyword is used to handle exceptions in Python?",
    'What is the output of: bool("")?',
    "How do you create a tuple in Python?",
    "What is the correct way to import a module in Python?",
    "Which function returns the absolute value of a number?",
]

python_q_ids = []
for i in range(20):
    conn = oracledb.connect(
        user="quiz_user", password="234208", dsn="localhost:1521/XEPDB1"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT quizzes_question_seq.NEXTVAL FROM DUAL")
    qid = cursor.fetchone()[0]
    python_q_ids.append(qid)
    cursor.execute(
        "INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (:1, :2, :3, :4, :5)",
        (qid, python_quiz_id, python_questions_text[i], "MCQ", 1),
    )
    conn.commit()
    conn.close()
print(f"Python questions: {len(python_q_ids)}")

# Python choices
python_choices = [
    (0, "var x = 5", 0),
    (0, "x = 5", 1),
    (0, "int x = 5", 0),
    (0, "let x = 5", 0),
    (1, "int", 0),
    (1, "str", 1),
    (1, "char", 0),
    (1, "text", 0),
    (2, "<class 'int'>", 0),
    (2, "<class 'str'>", 0),
    (2, "<class 'float'>", 1),
    (2, "<class 'double'>", 0),
    (3, "/", 0),
    (3, "//", 1),
    (3, "%", 0),
    (3, ":", 0),
    (4, "// comment", 0),
    (4, "# comment", 1),
    (4, "/* comment */", 0),
    (4, "<!-- comment -->", 0),
    (5, "input()", 1),
    (5, "get()", 0),
    (5, "read()", 0),
    (5, "scanf()", 0),
    (6, "2", 0),
    (6, "3", 1),
    (6, "4", 0),
    (6, "[1,2,3]", 0),
    (7, "add()", 0),
    (7, "append()", 1),
    (7, "insert()", 0),
    (7, "push()", 0),
    (8, "6", 0),
    (8, "8", 1),
    (8, "9", 0),
    (8, "5", 0),
    (9, "function", 0),
    (9, "def", 1),
    (9, "func", 0),
    (9, "define", 0),
    (10, "for i in range(5):", 1),
    (10, "for (i=0;i<5;i++)", 0),
    (10, "for i=0 to 5", 0),
    (10, "foreach i in range", 0),
    (11, "+", 1),
    (11, "&", 0),
    (11, "*", 0),
    (11, "%", 0),
    (12, "HelloHello", 1),
    (12, "Hello 2", 0),
    (12, "Error", 0),
    (12, "2Hello", 0),
    (13, "uppercase()", 0),
    (13, "upper()", 1),
    (13, "to_upper()", 0),
    (13, "uppercase", 0),
    (14, "Ordered collection", 0),
    (14, "Key-value pairs", 1),
    (14, "Set of unique", 0),
    (14, "Sequence of nums", 0),
    (15, "catch", 0),
    (15, "try", 1),
    (15, "handle", 0),
    (15, "except", 0),
    (16, "True", 0),
    (16, "False", 1),
    (16, "None", 0),
    (16, "Error", 0),
    (17, "[1,2,3]", 0),
    (17, "(1,2,3)", 1),
    (17, "{1,2,3}", 0),
    (17, "<1,2,3>", 0),
    (18, "import os", 1),
    (18, "#include os", 0),
    (18, "require os", 0),
    (18, "using os", 0),
    (19, "abs()", 1),
    (19, "absolute()", 0),
    (19, "absval()", 0),
    (19, "fabs()", 0),
]
for q_idx, text, is_correct in python_choices:
    conn = oracledb.connect(
        user="quiz_user", password="234208", dsn="localhost:1521/XEPDB1"
    )
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (:1, :2, :3)",
        (python_q_ids[q_idx], text, is_correct),
    )
    conn.commit()
    conn.close()
print("Python choices done")

# JavaScript quiz
conn = oracledb.connect(
    user="quiz_user", password="234208", dsn="localhost:1521/XEPDB1"
)
cursor = conn.cursor()
cursor.execute("SELECT quizzes_quiz_seq.NEXTVAL FROM DUAL")
cursor.fetchone()
cursor.execute(
    "INSERT INTO quizzes_quiz (title, description, created_by_id, created_at, is_active) VALUES ('JavaScript Basics', 'Test your JavaScript programming skills with 20 basic questions', 1, SYSDATE, 1)"
)
cursor.execute("SELECT quizzes_quiz_seq.CURRVAL FROM DUAL")
js_quiz_id = cursor.fetchone()[0]
conn.commit()
conn.close()
print(f"JS quiz: {js_quiz_id}")

# JavaScript questions
js_questions_text = [
    "Which keyword is used to declare a variable in JavaScript?",
    "Which syntax is correct for a single-line comment in JavaScript?",
    "Which function is used to output content to the console in JavaScript?",
    "Which data type represents a collection of key-value pairs in JavaScript?",
    "Which operator performs strict equality comparison in JavaScript?",
    "Which keyword is used to declare a constant in JavaScript?",
    "Which method adds an element to the end of an array?",
    'What is the output of: console.log("2" + 2)?',
    "Which block is used to handle exceptions in JavaScript?",
    "Which is the correct syntax for a function declaration in JavaScript?",
    "Which function converts a string to a number in JavaScript?",
    "What does NaN stand for in JavaScript?",
    "Which keyword is used to create a loop in JavaScript?",
    'What is the output of: Boolean("")?',
    "How do you access the first element of an array named arr?",
    "Which method removes the last element from an array?",
    "Which syntax defines an arrow function in JavaScript?",
    "Which quotes are used for template literals in JavaScript?",
    "What is the data type of an object in JavaScript?",
    "Which method is used to merge two arrays in JavaScript?",
]

js_q_ids = []
for i in range(20):
    conn = oracledb.connect(
        user="quiz_user", password="234208", dsn="localhost:1521/XEPDB1"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT quizzes_question_seq.NEXTVAL FROM DUAL")
    qid = cursor.fetchone()[0]
    js_q_ids.append(qid)
    cursor.execute(
        "INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (:1, :2, :3, :4, :5)",
        (qid, js_quiz_id, js_questions_text[i], "MCQ", 1),
    )
    conn.commit()
    conn.close()
print(f"JS questions: {len(js_q_ids)}")

# JavaScript choices
js_choices = [
    (0, "var x = 5", 0),
    (0, "let x = 5", 1),
    (0, "int x = 5", 0),
    (0, "const x = 5", 0),
    (1, "// comment", 1),
    (1, "# comment", 0),
    (1, "/* comment */", 0),
    (1, "<!-- comment -->", 0),
    (2, "print()", 0),
    (2, "console.log()", 1),
    (2, "System.out.println()", 0),
    (2, "echo()", 0),
    (3, "null", 0),
    (3, "undefined", 0),
    (3, "object", 1),
    (3, "number", 0),
    (4, "==", 0),
    (4, "===", 1),
    (4, "!=", 0),
    (4, "!==", 0),
    (5, "var", 0),
    (5, "let", 0),
    (5, "const", 1),
    (5, "constant", 0),
    (6, "push()", 1),
    (6, "pop()", 0),
    (6, "shift()", 0),
    (6, "unshift()", 0),
    (7, "4", 0),
    (7, "22", 1),
    (7, "NaN", 0),
    (7, "Error", 0),
    (8, "try", 0),
    (8, "catch", 1),
    (8, "handle", 0),
    (8, "except", 0),
    (9, "function myFunc()", 1),
    (9, "def myFunc()", 0),
    (9, "func myFunc()", 0),
    (9, "void myFunc()", 0),
    (10, "Number()", 1),
    (10, "parseInt()", 0),
    (10, "toInteger()", 0),
    (10, "Math.toNumber()", 0),
    (11, "Not a Number", 1),
    (11, "Not a Null", 0),
    (11, "Null and Number", 0),
    (11, "No Answer", 0),
    (12, "for", 1),
    (12, "while", 0),
    (12, "do-while", 0),
    (12, "for...of", 0),
    (13, "True", 0),
    (13, "False", 1),
    (13, "null", 0),
    (13, "undefined", 0),
    (14, "arr[0]", 1),
    (14, "arr.first()", 0),
    (14, "arr[1]", 0),
    (14, "arr.begin()", 0),
    (15, "pop()", 1),
    (15, "push()", 0),
    (15, "shift()", 0),
    (15, "splice()", 0),
    (16, "const f = () => {}", 1),
    (16, "const f = function()", 0),
    (16, "function f()", 0),
    (16, "def f()", 0),
    (17, "'", 0),
    (17, '"', 0),
    (17, "`", 1),
    (17, "/", 0),
    (18, "object", 1),
    (18, "array", 0),
    (18, "string", 0),
    (18, "undefined", 0),
    (19, "merge()", 0),
    (19, "concat()", 1),
    (19, "combine()", 0),
    (19, "join()", 0),
]
for q_idx, text, is_correct in js_choices:
    conn = oracledb.connect(
        user="quiz_user", password="234208", dsn="localhost:1521/XEPDB1"
    )
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (:1, :2, :3)",
        (js_q_ids[q_idx], text, is_correct),
    )
    conn.commit()
    conn.close()
print("Done!")
