
from django.urls import path
from .views import portfolio, portfolio2, home

urlpatterns = [
    path('portfolio/', portfolio, name="portfolio"),
    path('portfolio2/', portfolio2, name="portfolio2"),
    path('', home, name="home")
]