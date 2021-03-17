from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),   #convention is url kaha ko,  App name_ books url
    path('api/', include('api.urls')), 
]


