from django.contrib import admin
from .models import Quiz, question, choice

admin.site.register(Quiz)
admin.site.register(question)
admin.site.register(choice)


# Register your models here.
