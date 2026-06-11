from django.contrib import admin
from django.urls import path

from .views import IssueListView, IssueDetailView , IssueCreateView, IssueUpdateView,IssueDeleteView

urlpatterns = [
    path('', IssueListView.as_view(), name='list'),
    path('issue/<int:pk>/', IssueDetailView.as_view(), name='detail'),
    path('issue/add/', IssueCreateView.as_view(), name='create'),
    path('issue/update/<int:pk>/', IssueUpdateView.as_view(), name='update'),
    path('issue/delete/<int:pk>/', IssueDeleteView.as_view(), name='delete'),
]