
from django.urls import path
from .views import portfolio, portfolio2, home, portfolio_project

urlpatterns = [
    path('portfolio/', portfolio, name="portfolio"),
    path('portfolio2/', portfolio2, name="portfolio2"),
    path('', home, name="home"),
    path("portfolio_project/<int:id>", portfolio_project, name="portfolio_project"),

]