from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from accounts.forms import RegisterForm
from issue_tracker.models import ProjectModel



class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

class ProjectUsersView(LoginRequiredMixin, View):
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