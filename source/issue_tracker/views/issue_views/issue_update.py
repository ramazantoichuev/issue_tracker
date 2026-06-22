from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from issue_tracker.models.issue import IssueModel
from issue_tracker.forms import IssueForm



class IssueUpdateView(View):
    def get(self, request, pk):
        issue = get_object_or_404(IssueModel, pk=pk)
        form = IssueForm(instance=issue)
        return render(request, 'issue_tracker/issue_update.html', {'form': form, 'object': issue})

    def post(self, request, pk):
        issue = get_object_or_404(IssueModel, pk=pk)
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=issue.project.pk)
        return render(request, 'issue_tracker/issue_update.html', {'form': form, 'object': issue})
