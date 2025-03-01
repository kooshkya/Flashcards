from django.contrib import admin
from .models import Flashcard, Review, Deck


@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('id', 'box', 'created_at', 'updated_at') 

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'flashcard', 'review_date', 'remembered') 
    list_filter = ('review_date', 'remembered')

@admin.register(Deck)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at') 
    list_filter = ('name',)
