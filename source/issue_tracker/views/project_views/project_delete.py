from django.urls import reverse_lazy
from django.views.generic import DeleteView
from issue_tracker.models import ProjectModel

class ProjectDeleteView(DeleteView):
    template_name = 'projects/project_delete.html'
    model = ProjectModel
    success_url = reverse_lazy('project_list')