from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    Question_Type_Choices = [
        ('MCQ', 'Multiple Choice'),
        ('TF', 'True/False'),
    ]
    question_type = models.CharField(max_length=10, choices=Question_Type_Choices, default='MCQ')
    marks = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.quiz.title}: {self.text[:50]}"  # Return the quiz title and the first 50 characters of the question text

class choice(models.Model):
    question = models.ForeignKey(question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.question.text[:50]} - {self.text}"  # Return the first 50 characters of the question text and the choice text
    
