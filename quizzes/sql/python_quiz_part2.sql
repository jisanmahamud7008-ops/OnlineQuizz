-- Python Basics Quiz - Questions 11-20

-- Question 11
INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (11, 1, 'What is the correct syntax for a for loop in Python?', 'MCQ', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (11, 'for i in range(5):', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (11, 'for (i = 0; i < 5; i++)', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (11, 'for i = 0 to 5', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (11, 'foreach i in range(5)', 0);

-- Question 12
INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (12, 1, 'Which operator is used for string concatenation?', 'MCQ', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (12, '+', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (12, '&', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (12, '*', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (12, '%', 0);

-- Question 13
INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (13, 1, 'What is the output of: print("Hello" * 2)?', 'MCQ', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (13, 'HelloHello', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (13, 'Hello 2', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (13, 'Error', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (13, '2Hello', 0);

-- Question 14
INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (14, 1, 'Which method converts a string to uppercase?', 'MCQ', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (14, 'uppercase()', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (14, 'upper()', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (14, 'to_upper()', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (14, 'uppercase', 0);

-- Question 15
INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (15, 1, 'What is a dictionary in Python?', 'MCQ', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (15, 'An ordered collection', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (15, 'A key-value pair collection', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (15, 'A set of unique elements', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (15, 'A sequence of numbers', 0);

-- Question 16
INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (16, 1, 'Which keyword is used to handle exceptions in Python?', 'MCQ', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (16, 'catch', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (16, 'try', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (16, 'handle', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (16, 'except', 0);

-- Question 17
INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (17, 1, 'What is the output of: bool("")?', 'MCQ', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (17, 'True', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (17, 'False', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (17, 'None', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (17, 'Error', 0);

-- Question 18
INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (18, 1, 'How do you create a tuple in Python?', 'MCQ', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (18, '[1, 2, 3]', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (18, '(1, 2, 3)', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (18, '{1, 2, 3}', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (18, '<1, 2, 3>', 0);

-- Question 19
INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (19, 1, 'What is the correct way to import a module in Python?', 'MCQ', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (19, 'import os', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (19, '#include os', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (19, 'require os', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (19, 'using os', 0);

-- Question 20
INSERT INTO quizzes_question (id, quiz_id, text, question_type, marks) VALUES (20, 1, 'Which function returns the absolute value of a number?', 'MCQ', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (20, 'abs()', 1);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (20, 'absolute()', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (20, 'absval()', 0);
INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (20, 'fabs()', 0);

COMMIT;