from django.urls import path

from .views.issue_views.view import IssueListView, IssueDetailView , IssueCreateView, IssueUpdateView,IssueDeleteView
from issue_tracker.views.project_views.project_create import ProjectCreateView
from .views.project_views import ProjectListView , ProjectDetailView, ProjectCreateView, ProjectUpdateView , ProjectDeleteView

urlpatterns = [
    path('', IssueListView.as_view(), name='list'),
    path('issue/<int:pk>/', IssueDetailView.as_view(), name='detail'),
    path('issue/add/', IssueCreateView.as_view(), name='create'),
    path('issue/update/<int:pk>/', IssueUpdateView.as_view(), name='update'),
    path('issue/delete/<int:pk>/', IssueDeleteView.as_view(), name='delete'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/add/', ProjectCreateView.as_view(), name='project_create'),
    path('project/update/<int:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/delete/<int:pk>/', ProjectDeleteView.as_view(), name='project_delete')

]