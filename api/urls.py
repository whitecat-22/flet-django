from django.urls import path
from .views import SnippetList

urlpatterns = [
    path('', SnippetList.as_view()),
]
