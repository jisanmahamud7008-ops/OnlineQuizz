from django.urls import path
from . import views

urlpatterns = [
    path("<int:quiz_id>/", views.quiz_view, name="quiz_start"),
    path("<int:quiz_id>/<str:level>/", views.quiz_view, name="quiz_start_level"),
    path("<int:quiz_id>/submit/", views.quiz_submit, name="quiz_submit"),
    path(
        "<int:quiz_id>/submit/<str:level>/", views.quiz_submit, name="quiz_submit_level"
    ),
    path("<int:quiz_id>/result/", views.quiz_result, name="quiz_result"),
    path(
        "get-incorrect-answers/",
        views.get_incorrect_answers,
        name="get_incorrect_answers",
    ),
]
