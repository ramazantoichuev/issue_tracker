from django.urls import reverse_lazy
from django.views.generic import CreateView

from issue_tracker.forms import  ProjectForm
from issue_tracker.models import ProjectModel


class ProjectCreateView(CreateView):
    template_name = 'projects/project_create.html'
    model = ProjectModel
    form_class = ProjectForm
    success_url = reverse_lazy('project_detail')

