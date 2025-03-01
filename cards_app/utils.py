from django.utils import timezone
from cards_app.models import Flashcard, Review, Deck
from cards_app.models import LEITNER_REVIEW_PERIODS
import random

def get_overdue_flashcards(deck_id: int):
    overdue_flashcards = []

    for flashcard in Flashcard.objects.filter(deck_id=deck_id):
        last_review = Review.objects.filter(flashcard=flashcard).order_by('-review_date').first()

        if last_review:
            review_period = LEITNER_REVIEW_PERIODS.get(flashcard.box)
            if review_period:
                next_review_date = last_review.review_date + review_period
                if next_review_date <= timezone.now():
                    overdue_flashcards.append(flashcard)
            else:
                overdue_flashcards.append(flashcard)
        else:
            overdue_flashcards.append(flashcard)
    
    random.shuffle(overdue_flashcards)
    return overdue_flashcards