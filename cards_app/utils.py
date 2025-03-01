from django.utils import timezone
from datetime import timedelta
from cards_app.models import Flashcard, Review
from cards_app.models import LEITNER_REVIEW_PERIODS


def get_overdue_flashcards():
    overdue_flashcards = []

    for flashcard in Flashcard.objects.all():
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
    return overdue_flashcards