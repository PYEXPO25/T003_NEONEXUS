from django.urls import path
from .views import text_translation_view

urlpatterns = [
    path("", text_translation_view, name="text_translation"),
]