from django.db import migrations


def transfer_types(apps, schema_editor):
    IssueModel = apps.get_model('issue_tracker', 'IssueModel')
    for issue in IssueModel.objects.all():
        if issue.type_old:
            issue.type.set([issue.type_old])


def rollback_transfer(apps, schema_editor):
    IssueModel = apps.get_model('issue_tracker', 'IssueModel')
    for issue in IssueModel.objects.all():
        types = issue.type.all()
        if types:
            issue.type_old = types.first()
            issue.save()


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0003_issuemodel_type_old_remove_issuemodel_type_and_more'),
    ]

    operations = [
        migrations.RunPython(transfer_types, rollback_transfer)
    ]