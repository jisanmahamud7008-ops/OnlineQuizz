-- Python Basics Quiz - 20 Questions

-- Section 1: Insert Quiz
INSERT INTO quizzes_quiz (id, title, description, created_by_id, created_at, is_active)
VALUES (1, 'Python Basics', 'Test your Python programming skills with 20 basic questions', 1, SYSDATE, 1);

-- Question 1
INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (1, 1, 'What is the correct way to create a variable in Python?', 'MCQ', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (1, 'var x = 5', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (1, 'x = 5', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (1, 'int x = 5', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (1, 'let x = 5', 0);

-- Question 2
INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (2, 1, 'Which data type is used to store text in Python?', 'MCQ', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (2, 'int', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (2, 'str', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (2, 'char', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (2, 'text', 0);

-- Question 3
INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (3, 1, 'What is the output of: print(type(3.14))?', 'MCQ', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (3, '<class ''int''>', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (3, '<class ''str''>', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (3, '<class ''float''>', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (3, '<class ''double''>', 0);

-- Question 4
INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (4, 1, 'Which operator is used for integer division in Python?', 'MCQ', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (4, '/', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (4, '//', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (4, '%', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (4, ':', 0);

-- Question 5
INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (5, 1, 'What is the correct way to write a comment in Python?', 'MCQ', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (5, '// This is a comment', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (5, '# This is a comment', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (5, '/* This is a comment */', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (5, '<!-- This is a comment -->', 0);

-- Question 6
INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (6, 1, 'Which function is used to get input from user in Python?', 'MCQ', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (6, 'input()', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (6, 'get()', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (6, 'read()', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (6, 'scanf()', 0);

-- Question 7
INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (7, 1, 'What is the output of: len([1, 2, 3])?', 'MCQ', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (7, '2', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (7, '3', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (7, '4', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (7, '[1, 2, 3]', 0);

-- Question 8
INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (8, 1, 'Which method is used to add an element to a list?', 'MCQ', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (8, 'add()', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (8, 'append()', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (8, 'insert()', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (8, 'push()', 0);

-- Question 9
INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (9, 1, 'What is the output of: print(2 ** 3)?', 'MCQ', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (9, '6', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (9, '8', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (9, '9', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (9, '5', 0);

-- Question 10
INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (10, 1, 'Which keyword is used to define a function in Python?', 'MCQ', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (10, 'function', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (10, 'def', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (10, 'func', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (10, 'define', 0);

COMMIT;