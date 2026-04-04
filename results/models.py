from django.db import models
from django.contrib.auth.models import User
from quizzes.models import Quiz, question, choice



class attempt(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='attempts')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'quizzes_attempt'

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title}" 

class student_answer(models.Model):
    attempt = models.ForeignKey(attempt, on_delete=models.CASCADE, related_name='student_answers')
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(choice, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'quizzes_student_answer'

    def __str__(self):
        return f"{self.attempt.user.username} - {self.question.text[:50]}"  # Return the username and the first 50 characters of the question text       
# Create your models here.


# Create your models here.
