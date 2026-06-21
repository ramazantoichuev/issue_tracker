import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0007_data_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuemodel',
            name='project',
            field=models.ForeignKey(null=False, on_delete=django.db.models.deletion.RESTRICT, to='issue_tracker.projectmodel'),
        ),
    ]