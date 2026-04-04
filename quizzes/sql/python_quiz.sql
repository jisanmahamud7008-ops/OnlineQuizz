-- Python Basics Quiz - 20 Questions

-- Insert Quiz
INSERT INTO quizzes_quiz (title, description, created_by_id, created_at, is_active)
VALUES ('Python Basics', 'Test your Python programming skills with 20 basic questions', 1, SYSDATE, 1);

DECLARE
    v_quiz_id NUMBER;
BEGIN
    SELECT MAX(id) INTO v_quiz_id FROM quizzes_quiz;
    
    -- Question 1
    INSERT INTO quizzes_question (quiz_id, text, question_type, marks)
    VALUES (v_quiz_id, 'What is the correct way to create a variable in Python?', 'MCQ', 1);
    
    DECLARE v_q_id NUMBER;
    BEGIN
        SELECT MAX(id) INTO v_q_id FROM quizzes_question;
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'var x = 5', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'x = 5', 1);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'int x = 5', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'let x = 5', 0);
    END;

    -- Question 2
    INSERT INTO quizzes_question (quiz_id, text, question_type, marks)
    VALUES (v_quiz_id, 'Which data type is used to store text in Python?', 'MCQ', 1);
    
    DECLARE v_q_id NUMBER;
    BEGIN
        SELECT MAX(id) INTO v_q_id FROM quizzes_question;
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'int', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'str', 1);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'char', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'text', 0);
    END;

    -- Question 3
    INSERT INTO quizzes_question (quiz_id, text, question_type, marks)
    VALUES (v_quiz_id, 'What is the output of: print(type(3.14))?', 'MCQ', 1);
    
    DECLARE v_q_id NUMBER;
    BEGIN
        SELECT MAX(id) INTO v_q_id FROM quizzes_question;
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '<class ''int''>', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '<class ''str''>', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '<class ''float''>', 1);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '<class ''double''>', 0);
    END;

    -- Question 4
    INSERT INTO quizzes_question (quiz_id, text, question_type, marks)
    VALUES (v_quiz_id, 'Which operator is used for integer division in Python?', 'MCQ', 1);
    
    DECLARE v_q_id NUMBER;
    BEGIN
        SELECT MAX(id) INTO v_q_id FROM quizzes_question;
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '/', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '//', 1);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '%', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, ':', 0);
    END;

    -- Question 5
    INSERT INTO quizzes_question (quiz_id, text, question_type, marks)
    VALUES (v_quiz_id, 'What is the correct way to write a comment in Python?', 'MCQ', 1);
    
    DECLARE v_q_id NUMBER;
    BEGIN
        SELECT MAX(id) INTO v_q_id FROM quizzes_question;
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '// This is a comment', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '# This is a comment', 1);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '/* This is a comment */', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '<!-- This is a comment -->', 0);
    END;

    -- Question 6
    INSERT INTO quizzes_question (quiz_id, text, question_type, marks)
    VALUES (v_quiz_id, 'Which function is used to get input from user in Python?', 'MCQ', 1);
    
    DECLARE v_q_id NUMBER;
    BEGIN
        SELECT MAX(id) INTO v_q_id FROM quizzes_question;
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'input()', 1);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'get()', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'read()', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'scanf()', 0);
    END;

    -- Question 7
    INSERT INTO quizzes_question (quiz_id, text, question_type, marks)
    VALUES (v_quiz_id, 'What is the output of: len([1, 2, 3])?', 'MCQ', 1);
    
    DECLARE v_q_id NUMBER;
    BEGIN
        SELECT MAX(id) INTO v_q_id FROM quizzes_question;
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '2', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '3', 1);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '4', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '[1, 2, 3]', 0);
    END;

    -- Question 8
    INSERT INTO quizzes_question (quiz_id, text, question_type, marks)
    VALUES (v_quiz_id, 'Which method is used to add an element to a list?', 'MCQ', 1);
    
    DECLARE v_q_id NUMBER;
    BEGIN
        SELECT MAX(id) INTO v_q_id FROM quizzes_question;
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'add()', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'append()', 1);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'insert()', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'push()', 0);
    END;

    -- Question 9
    INSERT INTO quizzes_question (quiz_id, text, question_type, marks)
    VALUES (v_quiz_id, 'What is the output of: print(2 ** 3)?', 'MCQ', 1);
    
    DECLARE v_q_id NUMBER;
    BEGIN
        SELECT MAX(id) INTO v_q_id FROM quizzes_question;
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '6', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '8', 1);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '9', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '5', 0);
    END;

    -- Question 10
    INSERT INTO quizzes_question (quiz_id, text, question_type, marks)
    VALUES (v_quiz_id, 'Which keyword is used to define a function in Python?', 'MCQ', 1);
    
    DECLARE v_q_id NUMBER;
    BEGIN
        SELECT MAX(id) INTO v_q_id FROM quizzes_question;
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'function', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'def', 1);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'func', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'define', 0);
    END;

    -- Question 11
    INSERT INTO quizzes_question (quiz_id, text, question_type, marks)
    VALUES (v_quiz_id, 'What is the correct syntax for a for loop in Python?', 'MCQ', 1);
    
    DECLARE v_q_id NUMBER;
    BEGIN
        SELECT MAX(id) INTO v_q_id FROM quizzes_question;
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'for i in range(5):', 1);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'for (i = 0; i < 5; i++)', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'for i = 0 to 5', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'foreach i in range(5)', 0);
    END;

    -- Question 12
    INSERT INTO quizzes_question (quiz_id, text, question_type, marks)
    VALUES (v_quiz_id, 'Which operator is used for string concatenation?', 'MCQ', 1);
    
    DECLARE v_q_id NUMBER;
    BEGIN
        SELECT MAX(id) INTO v_q_id FROM quizzes_question;
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '+', 1);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '&', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '*', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '%', 0);
    END;

    -- Question 13
    INSERT INTO quizzes_question (quiz_id, text, question_type, marks)
    VALUES (v_quiz_id, 'What is the output of: print("Hello" * 2)?', 'MCQ', 1);
    
    DECLARE v_q_id NUMBER;
    BEGIN
        SELECT MAX(id) INTO v_q_id FROM quizzes_question;
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'HelloHello', 1);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'Hello 2', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'Error', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '2Hello', 0);
    END;

    -- Question 14
    INSERT INTO quizzes_question (quiz_id, text, question_type, marks)
    VALUES (v_quiz_id, 'Which method converts a string to uppercase?', 'MCQ', 1);
    
    DECLARE v_q_id NUMBER;
    BEGIN
        SELECT MAX(id) INTO v_q_id FROM quizzes_question;
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'uppercase()', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'upper()', 1);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'to_upper()', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'uppercase', 0);
    END;

    -- Question 15
    INSERT INTO quizzes_question (quiz_id, text, question_type, marks)
    VALUES (v_quiz_id, 'What is a dictionary in Python?', 'MCQ', 1);
    
    DECLARE v_q_id NUMBER;
    BEGIN
        SELECT MAX(id) INTO v_q_id FROM quizzes_question;
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'An ordered collection', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'A key-value pair collection', 1);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'A set of unique elements', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'A sequence of numbers', 0);
    END;

    -- Question 16
    INSERT INTO quizzes_question (quiz_id, text, question_type, marks)
    VALUES (v_quiz_id, 'Which keyword is used to handle exceptions in Python?', 'MCQ', 1);
    
    DECLARE v_q_id NUMBER;
    BEGIN
        SELECT MAX(id) INTO v_q_id FROM quizzes_question;
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'catch', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'try', 1);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'handle', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'except', 0);
    END;

    -- Question 17
    INSERT INTO quizzes_question (quiz_id, text, question_type, marks)
    VALUES (v_quiz_id, 'What is the output of: bool("")?', 'MCQ', 1);
    
    DECLARE v_q_id NUMBER;
    BEGIN
        SELECT MAX(id) INTO v_q_id FROM quizzes_question;
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'True', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'False', 1);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'None', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'Error', 0);
    END;

    -- Question 18
    INSERT INTO quizzes_question (quiz_id, text, question_type, marks)
    VALUES (v_quiz_id, 'How do you create a tuple in Python?', 'MCQ', 1);
    
    DECLARE v_q_id NUMBER;
    BEGIN
        SELECT MAX(id) INTO v_q_id FROM quizzes_question;
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '[1, 2, 3]', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '(1, 2, 3)', 1);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '{1, 2, 3}', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '<1, 2, 3>', 0);
    END;

    -- Question 19
    INSERT INTO quizzes_question (quiz_id, text, question_type, marks)
    VALUES (v_quiz_id, 'What is the correct way to import a module in Python?', 'MCQ', 1);
    
    DECLARE v_q_id NUMBER;
    BEGIN
        SELECT MAX(id) INTO v_q_id FROM quizzes_question;
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'import os', 1);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, '#include os', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'require os', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'using os', 0);
    END;

    -- Question 20
    INSERT INTO quizzes_question (quiz_id, text, question_type, marks)
    VALUES (v_quiz_id, 'Which function returns the absolute value of a number?', 'MCQ', 1);
    
    DECLARE v_q_id NUMBER;
    BEGIN
        SELECT MAX(id) INTO v_q_id FROM quizzes_question;
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'abs()', 1);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'absolute()', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'absval()', 0);
        INSERT INTO quizzes_choice (question_id, text, is_correct) VALUES (v_q_id, 'fabs()', 0);
    END;

    DBMS_OUTPUT.PUT_LINE('Python Basics quiz with 20 questions created successfully!');
END;
/

COMMIT;