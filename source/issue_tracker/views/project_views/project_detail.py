from django.views.generic import DetailView

from issue_tracker.models import ProjectModel


class ProjectDetailView(DetailView):
    model = ProjectModel
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'
