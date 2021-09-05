"""book_authors_temp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addbook', views.addbook, name="addbook"),
    path('books/<book_id>', views.info_book, name="info_book"),
    path('books/<book_id>/add_author_book', views.add_author_book, name="add_author_book"),
    path('authors', views.authors, name="authors"),
    path('addauthor', views.addauthor, name="addauthor"), 
    path('authors/<author_id>', views.info_author, name="info_author"),
    path('authors/<author_id>/addbook', views.booktoauthor, name="booktoauthor"),
]
