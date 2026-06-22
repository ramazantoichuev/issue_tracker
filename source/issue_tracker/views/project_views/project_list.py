from django.views.generic import ListView
from issue_tracker.models.project import ProjectModel


class ProjectListView(ListView):
    model = ProjectModel
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    paginate_by = 5



