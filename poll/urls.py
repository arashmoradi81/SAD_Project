from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='home-page'),
    path('create-vote/', views.CreateVote, name='create-vote'),
]
