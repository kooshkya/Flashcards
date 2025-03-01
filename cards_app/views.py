from django.shortcuts import render
from cards_app.utils import get_overdue_flashcards


def overdue_flashcards(request):
    overdue_cards = get_overdue_flashcards()
    
    # Prepare flashcards data as a list of dictionaries with front and back HTML
    flashcard_data = []
    for card in overdue_cards:
        flashcard_data.append({
            'id': card.id,
            'front': card.front,
            'back': card.back,
        })
    
    # Pass the flashcard data to the template as a JavaScript variable
    return render(request, 'cards_app/overdue_flashcards.html', {
        'flashcard_data': flashcard_data
    })

