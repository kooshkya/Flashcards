from django.db import models
from ckeditor.fields import RichTextField

from datetime import timedelta

unit_of_cycle = timedelta(hours=24)

LEITNER_REVIEW_PERIODS = {
    1: unit_of_cycle,
    2: unit_of_cycle * 2,  
    3: unit_of_cycle * 5,  
    4: unit_of_cycle * 10,  
    5: unit_of_cycle * 30,
}

class Deck(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Deck {self.name}"

class Flashcard(models.Model):
    BOX_CHOICES = [(i, str(i)) for i in range(1, 6)]

    front = RichTextField() 
    back = RichTextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    box = models.IntegerField(choices=BOX_CHOICES, default=1)
    deck = models.ForeignKey(Deck, on_delete=models.RESTRICT, related_name="flashcards")

    def __str__(self):
        return f"Flashcard {self.id} (Box {self.box})"
    

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