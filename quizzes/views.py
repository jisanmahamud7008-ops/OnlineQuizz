from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from quizzes.models import Quiz
from results.models import attempt, student_answer


@login_required
def quiz_view(request, quiz_id, level=None):
    quiz = get_object_or_404(Quiz, id=quiz_id, is_active=True)

    if level and level in ["Beginner", "Intermediate", "Advanced"]:
        questions = quiz.questions.filter(level=level)
    else:
        questions = quiz.questions.all()

    question_count = questions.count()
    progress_percentage = 100 // question_count if question_count > 0 else 25

    current_attempt = attempt.objects.create(quiz=quiz, user=request.user)
    request.session["attempt_id"] = current_attempt.id
    if level:
        request.session["quiz_level"] = level

    return render(
        request,
        "exam.html",
        {
            "quiz": quiz,
            "questions": questions,
            "progress_percentage": progress_percentage,
            "attempt_id": current_attempt.id,
            "quiz_level": level,
            "timeLimit": 10,
        },
    )


@login_required
def quiz_submit(request, quiz_id, level=None):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    attempt_id = request.session.get("attempt_id")
    quiz_level = (
        level or request.POST.get("quiz_level") or request.session.get("quiz_level")
    )

    if not attempt_id:
        return redirect("home")

    current_attempt = get_object_or_404(attempt, id=attempt_id, user=request.user)

    if quiz_level and quiz_level in ["Beginner", "Intermediate", "Advanced"]:
        questions = list(quiz.questions.filter(level=quiz_level))
    else:
        questions = list(quiz.questions.all())

    score = 0
    total_marks = 0
    incorrect_answers = []

    for question in questions:
        total_marks += question.marks
        selected_choice_id = request.POST.get(f"question_{question.id}")

        if selected_choice_id:
            choice_id = int(selected_choice_id)
            from quizzes.models import choice

            selected_choice = get_object_or_404(choice, id=choice_id, question=question)

            student_answer.objects.create(
                attempt=current_attempt,
                question=question,
                selected_choice=selected_choice,
            )

            if selected_choice.is_correct:
                score += question.marks
            else:
                if quiz.is_special:
                    correct_choice = question.choices.filter(is_correct=True).first()
                    incorrect_answers.append(
                        {
                            "question_text": question.text,
                            "correct_answer": correct_choice.text
                            if correct_choice
                            else "",
                            "level": question.level,
                        }
                    )

    current_attempt.completed = True
    current_attempt.save()

    percentage = (score / total_marks * 100) if total_marks > 0 else 0

    if "attempt_id" in request.session:
        del request.session["attempt_id"]
    if "quiz_level" in request.session:
        del request.session["quiz_level"]

    context = {
        "quiz": quiz,
        "score": score,
        "total": total_marks,
        "total_questions": len(questions),
        "percentage": round(percentage, 2),
        "attempt": current_attempt,
        "quiz_level": quiz_level,
    }

    if quiz.is_special:
        request.session["incorrect_answers"] = incorrect_answers
        context["show_incorrect_btn"] = True

    return render(request, "result.html", context)


@login_required
def get_incorrect_answers(request):
    incorrect_answers = request.session.get("incorrect_answers", [])
    return JsonResponse({"incorrect_answers": incorrect_answers})


@login_required
def quiz_result(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    attempt_id = request.session.get("attempt_id")

    if attempt_id:
        current_attempt = get_object_or_404(attempt, id=attempt_id, user=request.user)
        student_answers = current_attempt.student_answers.all()

        score = 0
        total_marks = 0

        for answer in student_answers:
            total_marks += answer.question.marks
            if answer.selected_choice and answer.selected_choice.is_correct:
                score += answer.question.marks

        percentage = (score / total_marks * 100) if total_marks > 0 else 0

        if percentage >= 90:
            comment = "Outstanding! You're a star!"
        elif percentage >= 80:
            comment = "Excellent work! Keep it up!"
        elif percentage >= 70:
            comment = "Great job! You're doing well!"
        elif percentage >= 60:
            comment = "Good effort! Keep practicing!"
        elif percentage >= 50:
            comment = "Not bad! A little more practice will help."
        elif percentage >= 40:
            comment = "Keep trying! You'll improve with practice."
        else:
            comment = "Don't give up! Try again and you'll do better!"

        return render(
            request,
            "result.html",
            {
                "quiz": quiz,
                "score": score,
                "total": total_marks,
                "percentage": round(percentage, 2),
                "attempt": current_attempt,
                "comment": comment,
            },
        )

    return redirect("home")
