
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', include('books.urls')),
    path('api/users/', include('users.urls')),
    path('api/loans/', include('loans.urls')),
    path('', views.home,name='home'),
    path('users/', include('users.urls')),
]
