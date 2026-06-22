from django.urls import reverse_lazy
from django.views.generic import UpdateView

from issue_tracker.forms import ProjectForm
from issue_tracker.models import ProjectModel


class ProjectUpdateView(UpdateView):
    template_name = 'projects/project_update.html'
    model = ProjectModel
    form_class = ProjectForm
