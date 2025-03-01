# In your urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('overdue_flashcards/', views.overdue_flashcards, name='overdue_flashcards'),
]
