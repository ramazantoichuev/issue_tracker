from django.contrib import admin
from issue_tracker.models.issue import IssueModel
from issue_tracker.models import StatusModel, TypeModel

class IssueTrackerAdmin(admin.ModelAdmin):
    list_display = ('summary', 'description', 'status', 'created_at', 'updated_at')
    search_fields = ('summary',)
    list_filter = ('type', 'status')

admin.site.register(IssueModel, IssueTrackerAdmin)


class TypeTrackerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(TypeModel, TypeTrackerAdmin)


class StatusModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(StatusModel, StatusModelAdmin)