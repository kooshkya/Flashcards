from django.contrib import admin
from .models import Flashcard, Review


@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at')  # Show timestamps in the list view

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'flashcard', 'review_date', 'remembered')  # Ensure review_date is visible
    ordering = ('-review_date',)  # Show latest reviews first
    list_filter = ('review_date', 'remembered')  # Add filtering options
