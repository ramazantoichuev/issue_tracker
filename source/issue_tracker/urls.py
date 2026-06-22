from django.urls import path
from .views.issue_views import  IssueDetailView , IssueUpdateView,IssueDeleteView
from .views.project_views import ProjectListView , ProjectDetailView, ProjectCreateView, ProjectUpdateView , ProjectDeleteView, IssueCreateInProjectView

urlpatterns = [
path('', ProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/add/', ProjectCreateView.as_view(), name='project_create'),
    path('project/update/<int:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/delete/<int:pk>/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:pk>/issue/add/', IssueCreateInProjectView.as_view(), name='issue_create_in_project'),
    path('issue/<int:pk>/', IssueDetailView.as_view(), name='detail'),
    path('issue/update/<int:pk>/', IssueUpdateView.as_view(), name='update'),
    path('issue/delete/<int:pk>/', IssueDeleteView.as_view(), name='delete')
]