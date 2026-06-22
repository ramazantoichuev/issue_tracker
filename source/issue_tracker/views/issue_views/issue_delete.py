from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from issue_tracker.models.issue import IssueModel


class IssueDeleteView(View):
    def get(self, request, pk):
        issue = get_object_or_404(IssueModel, pk=pk)
        return render(request, 'issue_tracker/issue_delete.html', {'issue': issue})

    def post(self, request, pk):
        issue = get_object_or_404(IssueModel, pk=pk)
        project_pk = issue.project.pk
        issue.delete()
        return redirect('project_detail', pk=project_pk)