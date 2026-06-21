from django.db import models
from issue_tracker.models.base_model import BaseModel
from issue_tracker.models.status import StatusModel
from issue_tracker.models.types import TypeModel
from issue_tracker.models.project import ProjectModel

class IssueModel(BaseModel):
    summary = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(blank=True)
    status = models.ForeignKey(StatusModel, on_delete=models.RESTRICT)
    type = models.ManyToManyField(TypeModel, related_name='issues')
    project = models.ForeignKey(ProjectModel, on_delete=models.RESTRICT)


    def __str__(self):
        return self.summary
