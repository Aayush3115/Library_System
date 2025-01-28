from django.urls import path
from .views import LoanView


urlpatterns= [
    path('', LoanView.as_view()),
]