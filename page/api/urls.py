from api import views
from django.urls import path

urlpatterns=[
    path("books/all",views.BookView.as_view()),
    path("book/<int:id>",views.BookList.as_view()),
]