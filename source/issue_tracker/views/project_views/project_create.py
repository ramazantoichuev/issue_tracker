from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from issue_tracker.forms import  ProjectForm
from issue_tracker.models import ProjectModel


class ProjectCreateView(LoginRequiredMixin,CreateView):
    template_name = 'projects/project_create.html'
    model = ProjectModel
    form_class = ProjectForm
    success_url = reverse_lazy('project_detail')

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.object.pk})
