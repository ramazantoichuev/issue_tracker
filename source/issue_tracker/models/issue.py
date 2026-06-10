from django.db import models

from issue_tracker.models import StatusModel, TypeModel, BaseModel


class IssueModel(BaseModel):
    summary = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(blank=True)
    status = models.ForeignKey(StatusModel, on_delete=models.RESTRICT)
    type = models.ForeignKey(TypeModel, on_delete=models.RESTRICT)

    def __str__(self):
        return self.summary
