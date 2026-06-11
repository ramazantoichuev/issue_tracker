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

        self.fields['summary'].widget.attrs['placeholder'] = 'Краткое описание'
        self.fields['description'].widget.attrs['placeholder'] = 'Полное описание'


    status = forms.ModelChoiceField(queryset=StatusModel.objects.all())
    type = forms.ModelMultipleChoiceField(
        queryset=TypeModel.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )



    class Meta:
        model = IssueModel
        fields = ('summary', 'description','status','type')
