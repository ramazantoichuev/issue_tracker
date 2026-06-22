from issue_tracker.forms import ProjectSearchForm
from django.views.generic import ListView
from issue_tracker.models.project import ProjectModel
from django.db.models import Q


class ProjectListView(ListView):
    model = ProjectModel
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | Q(description__icontains=search)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = ProjectSearchForm(self.request.GET)
        return context



