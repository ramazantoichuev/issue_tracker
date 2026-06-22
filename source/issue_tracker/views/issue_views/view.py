from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import TemplateView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from issue_tracker.models.issue import IssueModel
from issue_tracker.forms import IssueForm


class IssueListView(TemplateView):
    template_name = 'issue_tracker/issue_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = IssueModel.objects.all()
        return context

class IssueDetailView(TemplateView):
    template_name = 'issue_tracker/issue_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(IssueModel, pk=kwargs['pk'])
        return context

class IssueCreateView(View):
    def get(self, request):
        form = IssueForm()
        return render(request, 'issue_tracker/issue_create.html', {'form': form})

    def post(self, request):
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request, 'issue_tracker/issue_create.html', {'form': form})

class IssueUpdateView(View):
    def get(self, request, pk):
        issue = get_object_or_404(IssueModel, pk=pk)
        form = IssueForm(instance=issue)
        return render(request, 'issue_tracker/issue_update.html', {'form': form})

    def post(self, request, pk):
        issue = get_object_or_404(IssueModel, pk=pk)
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request, 'issue_tracker/issue_update.html', {'form': form})

class IssueDeleteView(View):
    def get(self, request, pk):
        issue = get_object_or_404(IssueModel, pk=pk)
        return render(request, 'issue_tracker/issue_delete.html',{'issue': issue})

    def post(self, request, pk):
        issue = get_object_or_404(IssueModel, pk=pk)
        issue.delete()
        return redirect('list')
