from django.views.generic import UpdateView
from django.urls import reverse_lazy
from issue_tracker.models.issue import IssueModel
from issue_tracker.forms import IssueForm


class IssueUpdateView(UpdateView):
    model = IssueModel
    form_class = IssueForm
    template_name = 'issue_tracker/issue_update.html'

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.object.project.pk})