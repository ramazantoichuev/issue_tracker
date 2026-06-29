from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from issue_tracker.forms import ProjectForm
from issue_tracker.models import ProjectModel
from issue_tracker.permissions import is_manager, is_project_member


class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'projects/project_update.html'
    model = ProjectModel
    form_class = ProjectForm

    def dispatch(self, request, *args, **kwargs):
        project = self.get_object()
        if not (is_manager(request.user) and is_project_member(request.user, project)):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.object.pk})