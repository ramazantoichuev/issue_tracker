from django.urls import reverse_lazy
from django.views.generic import CreateView
from issue_tracker.forms import IssueForm
from issue_tracker.models.issue import IssueModel
from issue_tracker.models.project import ProjectModel
from django.shortcuts import get_object_or_404


class IssueCreateInProjectView(CreateView):
    model = IssueModel
    form_class = IssueForm
    template_name = 'issue_tracker/issue_create.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields.pop('project', None)
        return form

    def form_valid(self, form):
        project = get_object_or_404(ProjectModel, pk=self.kwargs['pk'])
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.kwargs['pk']})