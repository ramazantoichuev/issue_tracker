from django.urls import reverse_lazy
from django.views.generic import DeleteView

from issue_tracker.models.issue import IssueModel


class IssueDeleteView(DeleteView):
    template_name = 'issue_tracker/issue_delete.html'
    model = IssueModel

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.object.project.pk})

