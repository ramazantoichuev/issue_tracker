from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from accounts.forms import RegisterForm
from issue_tracker.models import ProjectModel
from issue_tracker.permissions import is_manager, is_lead, is_project_member


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

class ProjectUsersView(LoginRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        project = get_object_or_404(ProjectModel, pk=kwargs['pk'])
        is_allowed = is_manager(request.user) or is_lead(request.user)
        if not (is_allowed and is_project_member(request.user, project)):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        project = get_object_or_404(ProjectModel, pk=pk)
        users = User.objects.all()
        return render(request, 'projects/project_users.html', {
            'project': project,
            'users': users
        })

    def post(self, request, pk):
        project = get_object_or_404(ProjectModel, pk=pk)
        user_id = request.POST.get('user_id')
        action = request.POST.get('action')
        user = get_object_or_404(User, pk=user_id)
        if action == 'add':
            project.users.add(user)
        elif action == 'remove':
            project.users.remove(user)
        return redirect('project_users', pk=pk)