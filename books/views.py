from django.views.generic import ListView

from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'

    # which model? ra which template



# request/ response logic for the web app, 

# view => generic View => we make the most out of it,  ListView, DetailView