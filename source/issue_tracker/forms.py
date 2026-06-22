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

    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        if len(summary) < 5:
            raise forms.ValidationError('Краткое описание должно быть не менее 5 символов')
        return summary

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description and len(description) > 500:
            raise forms.ValidationError('Описание не должно превышать 500 символов')
        return description


    class Meta:
        model = IssueModel
        fields = ('summary', 'description','status','type')



class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        self.fields['name'].widget.attrs['placeholder'] = 'Краткое описание'
        self.fields['description'].widget.attrs['placeholder'] = 'Полное описание'

    class Meta:
        model = ProjectModel
        fields = ('name', 'description', 'start_date', 'end_date')
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
