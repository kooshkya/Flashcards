from django.contrib import admin
from django.urls import path, include
from cards_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cards/', include('cards_app.urls')), 
    path('', views.home), 
]
