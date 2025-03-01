from django.db import models
from ckeditor.fields import RichTextField


class Flashcard(models.Model):
    front = RichTextField() 
    back = RichTextField()

    def __str__(self):
        return f"Flashcard {self.id}"