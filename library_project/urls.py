from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),   #later is the file name, books vitra ko url
    path('api/', include('api.urls')), 
]


