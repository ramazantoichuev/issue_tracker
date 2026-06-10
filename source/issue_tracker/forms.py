from typing import Type
from django import forms
from issue_tracker.models.issue import *




class IssueForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

    status = forms.ModelChoiceField(queryset=StatusModel.objects.all())
    type = forms.ModelChoiceField(queryset=TypeModel.objects.all())


    class Meta:
        model = IssueModel
        fields = ('summary', 'description','status','type')
