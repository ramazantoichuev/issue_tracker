from django.shortcuts import  get_object_or_404
from django.views.generic import TemplateView
from issue_tracker.models.issue import IssueModel

class IssueDetailView(TemplateView):
    template_name = 'issue_tracker/issue_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(IssueModel, pk=kwargs['pk'])
        return context