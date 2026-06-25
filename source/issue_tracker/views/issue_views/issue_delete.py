from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from issue_tracker.models.issue import IssueModel



class IssueDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'issue_tracker/issue_delete.html'
    model = IssueModel
    context_object_name = 'issue'


    def form_valid(self, form):
        self.object.is_deleted = True
        self.object.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.object.project.pk})
