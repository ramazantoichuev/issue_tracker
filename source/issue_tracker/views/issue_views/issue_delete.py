from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from issue_tracker.models.issue import IssueModel
from issue_tracker.permissions import is_manager, is_project_member, is_lead


class IssueDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'issue_tracker/issue_delete.html'
    model = IssueModel
    context_object_name = 'issue'

    def dispatch(self, request, *args, **kwargs):
        issue = self.get_object()
        project = issue.project
        is_allowed = is_manager(request.user) or is_lead(request.user)
        if not (is_allowed and is_project_member(request.user, project)):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object.is_deleted = True
        self.object.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.object.project.pk})
