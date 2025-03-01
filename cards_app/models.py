from django.db import models
from ckeditor.fields import RichTextField


class Flashcard(models.Model):
    front = RichTextField() 
    back = RichTextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Flashcard {self.id}"
    

class Review(models.Model):
    REMEMBER_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]

    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE, related_name='reviews')
    review_date = models.DateTimeField(auto_now_add=True)
    remembered = models.CharField(max_length=1, choices=REMEMBER_CHOICES)

    def __str__(self):
        return f"Review for Flashcard {self.flashcard.id} - {self.get_remembered_display()}"