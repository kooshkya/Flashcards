from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Flashcard, Review
from cards_app.utils import get_overdue_flashcards
from django.shortcuts import render


def overdue_flashcards(request):
    overdue_cards = get_overdue_flashcards()
    
    flashcard_data = []
    for card in overdue_cards:
        flashcard_data.append({
            'id': card.id,
            'front': card.front,
            'back': card.back,
        })
    return render(request, 'cards_app/overdue_flashcards.html', {
        'flashcard_data': flashcard_data
    })

def home(request):
    return render(request, 'cards_app/home.html')

@api_view(['POST'])
def record_review(request):
    flashcard_id = request.data.get('flashcard_id')
    remembered = request.data.get('remembered')

    if flashcard_id is None or remembered is None:
        return Response({'error': 'Both flashcard_id and remembered are required.'}, status=status.HTTP_400_BAD_REQUEST)

    if remembered not in [x[0] for x in Review.REMEMBER_CHOICES]:
        return Response({'error': 'remembered field invalid.'}, status = 400)
    
    try:
        flashcard = Flashcard.objects.get(id=flashcard_id)
    except Flashcard.DoesNotExist:
        return Response({'error': 'Flashcard not found.'}, status=status.HTTP_404_NOT_FOUND)

    Review.objects.create(
        flashcard=flashcard,
        remembered=remembered
    )

    if remembered == "N":
        flashcard.box = 1
    else:
        flashcard.box = min(5, flashcard.box + 1)
    flashcard.save()

    return Response({"success": "true"}, status=status.HTTP_201_CREATED)