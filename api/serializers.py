from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'author', 'isbn')

# if the app will be not have its own  database model , there is no need to create own file. 

# Serilizers, translate data into a format that is easy to consume over the internet, typically JSON

# From which model ,what things?? 