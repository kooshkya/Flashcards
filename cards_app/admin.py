from django.contrib import admin
from .models import Flashcard, Review


@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('id', 'box', 'created_at', 'updated_at') 

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'flashcard', 'review_date', 'remembered') 
    list_filter = ('review_date', 'remembered')
