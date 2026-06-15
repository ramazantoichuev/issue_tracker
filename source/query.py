from datetime import timedelta
from django.utils import timezone
from django.db.models import Q, F, Count
from issue_tracker.models.issue import IssueModel
from issue_tracker.models.types import TypeModel


closed = IssueModel.objects.filter(
    status__name='done',
    updated_at__gte=timezone.now() - timedelta(days=30)
)


tasks = IssueModel.objects.filter(
    Q(status__name='new') | Q(status__name='in progress'),
    Q(type__name='task') | Q(type__name='bug')
)


not_closed = IssueModel.objects.filter(
    Q(summary__icontains='bug') | Q(type__name='bug')
).exclude(status__name='done')


only_fields = IssueModel.objects.values('id', 'summary', 'type__name', 'status__name')

same_summary_description = IssueModel.objects.filter(summary=F('description'))

count_by_type = TypeModel.objects.annotate(issue_count=Count('issues'))
for t in count_by_type:
    print(t.name, t.issue_count)