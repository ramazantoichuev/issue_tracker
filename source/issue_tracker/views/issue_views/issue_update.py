from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from issue_tracker.models.issue import IssueModel
from issue_tracker.forms import IssueForm
from issue_tracker.permissions import is_manager, is_project_member, is_lead, is_developer


class IssueUpdateView(LoginRequiredMixin,UpdateView):
    model = IssueModel
    form_class = IssueForm
    template_name = 'issue_tracker/issue_update.html'

    def dispatch(self, request, *args, **kwargs):
        issue = self.get_object()
        project = issue.project
        is_allowed = is_manager(request.user) or is_lead(request.user) or is_developer(request.user)
        if not (is_allowed and is_project_member(request.user, project)):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.object.project.pk})