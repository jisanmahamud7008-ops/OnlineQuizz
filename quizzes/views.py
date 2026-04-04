from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from quizzes.models import Quiz
from results.models import attempt, student_answer


@login_required
def quiz_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id, is_active=True)
    questions = quiz.questions.all()
    question_count = questions.count()
    progress_percentage = 100 // question_count if question_count > 0 else 25

    current_attempt = attempt.objects.create(quiz=quiz, user=request.user)
    request.session["attempt_id"] = current_attempt.id

    return render(
        request,
        "exam.html",
        {
            "quiz": quiz,
            "questions": questions,
            "progress_percentage": progress_percentage,
            "attempt_id": current_attempt.id,
        },
    )


@login_required
def quiz_submit(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    attempt_id = request.session.get("attempt_id")

    if not attempt_id:
        return redirect("home")

    current_attempt = get_object_or_404(attempt, id=attempt_id, user=request.user)

    score = 0
    total_marks = 0

    for question in quiz.questions.all():
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

    current_attempt.completed = True
    current_attempt.save()

    percentage = (score / total_marks * 100) if total_marks > 0 else 0

    if "attempt_id" in request.session:
        del request.session["attempt_id"]

    return render(
        request,
        "result.html",
        {
            "quiz": quiz,
            "score": score,
            "total": total_marks,
            "percentage": round(percentage, 2),
            "attempt": current_attempt,
        },
    )


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
