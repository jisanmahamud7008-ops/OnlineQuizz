import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth.models import User
from quizzes.models import Quiz, question, choice

# Get or create a superuser for created_by
user, created = User.objects.get_or_create(
    username="admin", defaults={"is_superuser": True, "is_staff": True}
)
if created:
    user.set_password("admin123")
    user.save()

# Create the Python Job Test quiz
python_job_quiz, created = Quiz.objects.get_or_create(
    title="Python Job Test",
    defaults={
        "description": "A comprehensive Python quiz for job preparation with 60 questions across Beginner, Intermediate, and Advanced levels.",
        "created_by": user,
        "is_active": True,
        "is_special": True,
    },
)
print(f"Quiz created: {python_job_quiz.title}")

# Questions data
questions_data = [
    # Beginner (20 questions)
    (
        "Python is a:",
        "Compiled language",
        "Interpreted language",
        "Machine language",
        "Assembly language",
        2,
        "Beginner",
    ),
    ("Which is immutable?", "List", "Dictionary", "Tuple", "Set", 3, "Beginner"),
    (
        "What does == check?",
        "Memory location",
        "Value equality",
        "Object identity",
        "Type",
        2,
        "Beginner",
    ),
    (
        "Which is a mutable data type?",
        "String",
        "Tuple",
        "List",
        "Integer",
        3,
        "Beginner",
    ),
    ("Which symbol starts a comment?", "//", "#", "/*", "--", 2, "Beginner"),
    ("Output of len([1,2,3])?", "2", "3", "1", "Error", 2, "Beginner"),
    (
        "Which is used to define a function?",
        "function",
        "define",
        "def",
        "fun",
        3,
        "Beginner",
    ),
    (
        "Which data type stores key-value pairs?",
        "List",
        "Tuple",
        "Dictionary",
        "Set",
        3,
        "Beginner",
    ),
    (
        "Which is correct list syntax?",
        "(1,2,3)",
        "[1,2,3]",
        "{1,2,3}",
        "<1,2,3>",
        2,
        "Beginner",
    ),
    (
        "What does break do?",
        "Skips iteration",
        "Ends loop",
        "Ends program",
        "Pauses loop",
        2,
        "Beginner",
    ),
    ("is keyword checks:", "Value", "Type", "Identity", "Length", 3, "Beginner"),
    ("Which creates a set?", "[]", "()", "{} with values", '""', 3, "Beginner"),
    ("Output of type(5)?", "float", "int", "str", "number", 2, "Beginner"),
    (
        "Lambda function is:",
        "Named function",
        "Anonymous function",
        "Loop",
        "Class",
        2,
        "Beginner",
    ),
    (
        "List comprehension is used for:",
        "Sorting",
        "Filtering",
        "Creating lists concisely",
        "Deleting lists",
        3,
        "Beginner",
    ),
    (
        "Which is used to handle exceptions?",
        "catch",
        "try",
        "error",
        "final",
        2,
        "Beginner",
    ),
    (
        "Which loop runs at least once?",
        "for",
        "while",
        "do-while",
        "None",
        4,
        "Beginner",
    ),
    (
        "What is indentation used for?",
        "Decoration",
        "Block definition",
        "Comments",
        "Printing",
        2,
        "Beginner",
    ),
    (
        "What does pass do?",
        "Stops loop",
        "Skips iteration",
        "Does nothing",
        "Raises error",
        3,
        "Beginner",
    ),
    (
        '__name__ == "__main__" means:',
        "File imported",
        "File executed directly",
        "Error",
        "Class name",
        2,
        "Beginner",
    ),
    # Intermediate (20 questions)
    (
        "OOP stands for:",
        "Object Oriented Programming",
        "Order of Operations",
        "Output Oriented Programming",
        "None",
        1,
        "Intermediate",
    ),
    (
        "Pillars of OOP include:",
        "Looping",
        "Inheritance",
        "Compilation",
        "Parsing",
        2,
        "Intermediate",
    ),
    (
        "Inheritance allows:",
        "Code deletion",
        "Code reuse",
        "Faster execution",
        "Memory reduction",
        2,
        "Intermediate",
    ),
    (
        "Polymorphism means:",
        "Many forms",
        "Single form",
        "No form",
        "Error",
        1,
        "Intermediate",
    ),
    (
        "Encapsulation means:",
        "Hiding data",
        "Deleting data",
        "Printing data",
        "Looping data",
        1,
        "Intermediate",
    ),
    (
        "Decorators are used to:",
        "Modify function behavior",
        "Delete functions",
        "Print output",
        "Loop",
        1,
        "Intermediate",
    ),
    ("yield is used in:", "Class", "Generator", "Loop", "Condition", 2, "Intermediate"),
    ("Generator returns:", "List", "Iterator", "Tuple", "Set", 2, "Intermediate"),
    (
        "Virtual environment is used to:",
        "Increase speed",
        "Manage dependencies",
        "Delete libraries",
        "Compile code",
        2,
        "Intermediate",
    ),
    ("PEP 8 is:", "Python error", "Style guide", "Loop", "Package", 2, "Intermediate"),
    (
        "Shallow copy copies:",
        "Nested objects",
        "References",
        "Nothing",
        "Files",
        2,
        "Intermediate",
    ),
    (
        "Deep copy copies:",
        "Only reference",
        "Entire object",
        "Memory address",
        "None",
        2,
        "Intermediate",
    ),
    (
        "finally block executes:",
        "Only if error",
        "Only if no error",
        "Always",
        "Never",
        3,
        "Intermediate",
    ),
    ("Module is:", "Function", "Python file", "Class", "Loop", 2, "Intermediate"),
    (
        "Package is:",
        "Folder with modules",
        "Single file",
        "Loop",
        "Class",
        1,
        "Intermediate",
    ),
    ("@classmethod uses:", "self", "cls", "none", "super", 2, "Intermediate"),
    (
        "@staticmethod has:",
        "self",
        "cls",
        "No default parameter",
        "Loop",
        3,
        "Intermediate",
    ),
    (
        "Iterator must implement:",
        "__len__",
        "__iter__ and __next__",
        "__init__",
        "__call__",
        2,
        "Intermediate",
    ),
    (
        "Exception is:",
        "Syntax error only",
        "Runtime error",
        "Loop",
        "Function",
        2,
        "Intermediate",
    ),
    (
        "Overriding happens in:",
        "Same class",
        "Parent-child class",
        "Loop",
        "Module",
        2,
        "Intermediate",
    ),
    # Advanced (20 questions)
    (
        "GIL stands for:",
        "Global Interpreter Lock",
        "General Instruction Loop",
        "Global Internal Logic",
        "None",
        1,
        "Advanced",
    ),
    (
        "GIL affects:",
        "Multiprocessing",
        "Multithreading",
        "Compilation",
        "Memory",
        2,
        "Advanced",
    ),
    (
        "Multiprocessing uses:",
        "Single core",
        "Multiple cores",
        "No core",
        "GPU",
        2,
        "Advanced",
    ),
    (
        "Garbage collection handles:",
        "Syntax",
        "Memory cleanup",
        "Loop",
        "Error printing",
        2,
        "Advanced",
    ),
    (
        "__str__ is used for:",
        "Developer representation",
        "User-friendly string",
        "Loop",
        "Copy",
        2,
        "Advanced",
    ),
    ("__repr__ is for:", "User", "Debugging", "Loop", "Package", 2, "Advanced"),
    ("Context manager is used with:", "for", "with", "while", "try", 2, "Advanced"),
    (
        "Async programming improves:",
        "CPU speed",
        "I/O tasks handling",
        "Memory",
        "Storage",
        2,
        "Advanced",
    ),
    (
        "MRO determines:",
        "Memory",
        "Method search order",
        "Loop",
        "Compilation",
        2,
        "Advanced",
    ),
    (
        "Metaclass defines:",
        "Function",
        "Class behavior",
        "Loop",
        "Error",
        2,
        "Advanced",
    ),
    (
        "map() applies function to:",
        "One item",
        "Each item",
        "None",
        "Class",
        2,
        "Advanced",
    ),
    (
        "filter() returns:",
        "All elements",
        "Matching elements",
        "None",
        "Class",
        2,
        "Advanced",
    ),
    ("reduce() requires module:", "math", "sys", "functools", "os", 3, "Advanced"),
    (
        "Async function defined using:",
        "async def",
        "def async",
        "yield",
        "class",
        1,
        "Advanced",
    ),
    (
        "Python memory is managed by:",
        "Manual free",
        "Garbage collector",
        "Compiler",
        "User",
        2,
        "Advanced",
    ),
    (
        "Descriptor defines:",
        "Class behavior",
        "Attribute access",
        "Loop",
        "Module",
        2,
        "Advanced",
    ),
    (
        "Monkey patching means:",
        "Fix bug",
        "Modify at runtime",
        "Compile",
        "Delete class",
        2,
        "Advanced",
    ),
    (
        "Dependency injection improves:",
        "Tight coupling",
        "Loose coupling",
        "Memory",
        "Speed",
        2,
        "Advanced",
    ),
    (
        "Django request first hits:",
        "Model",
        "View",
        "URL dispatcher",
        "Template",
        3,
        "Advanced",
    ),
    (
        "Performance optimization includes:",
        "Using loops",
        "Profiling & caching",
        "More prints",
        "More classes",
        2,
        "Advanced",
    ),
]

# Clear existing questions for this quiz
python_job_quiz.questions.all().delete()

# Add questions
for q_data in questions_data:
    q = question.objects.create(quiz=python_job_quiz, text=q_data[0], level=q_data[6])

    # Create choices
    choices_data = [
        (q_data[1], 1 == q_data[5]),  # option1
        (q_data[2], 2 == q_data[5]),  # option2
        (q_data[3], 3 == q_data[5]),  # option3
        (q_data[4], 4 == q_data[5]),  # option4
    ]

    for i, (choice_text, is_correct) in enumerate(choices_data, 1):
        choice.objects.create(question=q, text=choice_text, is_correct=is_correct)

print(f"Added {len(questions_data)} questions to Python Job Test")
print(
    f"Beginner: {question.objects.filter(quiz=python_job_quiz, level='Beginner').count()}"
)
print(
    f"Intermediate: {question.objects.filter(quiz=python_job_quiz, level='Intermediate').count()}"
)
print(
    f"Advanced: {question.objects.filter(quiz=python_job_quiz, level='Advanced').count()}"
)
