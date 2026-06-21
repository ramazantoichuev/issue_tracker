import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0005_remove_issuemodel_type_old'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
            options={'abstract': False},
        ),
        migrations.AddField(
            model_name='issuemodel',
            name='project',
            field=models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.RESTRICT, to='issue_tracker.projectmodel'),
        ),
    ]