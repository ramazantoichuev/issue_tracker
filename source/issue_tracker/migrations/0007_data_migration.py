from django.db import migrations


def add_project(apps, schema_editor):
    ProjectModel = apps.get_model('issue_tracker', 'ProjectModel')
    IssueModel = apps.get_model('issue_tracker', 'IssueModel')
    project = ProjectModel.objects.create(
        name='Test Project',
        description='Тестовый проект',
        start_date='2026-01-01'
    )
    IssueModel.objects.all().update(project=project)


def rollback(apps, schema_editor):
    ProjectModel = apps.get_model('issue_tracker', 'ProjectModel')
    IssueModel = apps.get_model('issue_tracker', 'IssueModel')
    IssueModel.objects.all().update(project=None)
    ProjectModel.objects.filter(name='Test Project').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0006_projectmodel_add_nullable_project'),
    ]

    operations = [
        migrations.RunPython(add_project, rollback)
    ]