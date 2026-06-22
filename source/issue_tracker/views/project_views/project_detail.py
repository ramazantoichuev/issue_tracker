from django.views.generic import DetailView

from issue_tracker.models import ProjectModel


class ProjectDetailView(DetailView):
    model = ProjectModel
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = self.object.issuemodel_set.filter(is_deleted=False)
        return context
