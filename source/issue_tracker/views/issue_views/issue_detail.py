from django.views.generic import DetailView
from issue_tracker.models.issue import IssueModel


class IssueDetailView(DetailView):
    model = IssueModel
    template_name = 'issue_tracker/issue_detail.html'
    context_object_name = 'issue'