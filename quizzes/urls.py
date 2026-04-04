from django.urls import path
from . import views

urlpatterns = [
    path("quiz/<int:quiz_id>/", views.quiz_view, name="quiz_start"),
    path("quiz/<int:quiz_id>/submit/", views.quiz_submit, name="quiz_submit"),
    path("quiz/<int:quiz_id>/result/", views.quiz_result, name="quiz_result"),
]
