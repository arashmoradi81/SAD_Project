from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='home-page'),
    path('create-vote/', views.CreateVote, name='create-vote'),
    path('open-end/<str:pk>/', views.AddOpenEnd, name='open-end'),
    path('add-question/<str:pk>/', views.AddQuestion, name='add-question'),
    path('close-test/<str:pk>/', views.AddCloseTest, name='close-test'),
    path('fill-poll/<str:pk>/', views.FillPoll, name='fill-poll'),
]
