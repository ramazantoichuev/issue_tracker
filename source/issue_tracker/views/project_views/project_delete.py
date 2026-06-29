from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from issue_tracker.models import ProjectModel
from issue_tracker.permissions import is_manager, is_project_member


class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'projects/project_delete.html'
    model = ProjectModel
    success_url = reverse_lazy('project_list')

    def dispatch(self, request, *args, **kwargs):
        project = self.get_object()
        if not (is_manager(request.user) and is_project_member(request.user, project)):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)