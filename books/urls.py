from django.urls import path

from .views import BookListView

from django.urls import path


urlpatterns = [
    path('', BookListView.as_view(), name='home'),
]