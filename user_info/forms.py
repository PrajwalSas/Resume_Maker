from django import forms
from user_info.fields import CommaSeparatedField



class Get_LinkedIn_form(forms.Form):
    linkedin_url = forms.CharField(max_length=120, label='Please provide url of LinkedIn profile', widget=forms.Textarea(attrs={
        'style': '''width: 50%;
        padding: 12px 20px;
        border: 2px solid #ccc;
        border-radius: 4px;
        background-color: #f8f8f8;
        resize: none;
        background-color: #dbdbdb;
        ''',
        'rows':'1',
        'cols': '100',
    }))
    github_url = forms.CharField(max_length=100, label='Please provide url of GitHub profile', widget=forms.Textarea(attrs={
        'style': '''width: 50%;
        padding: 12px 20px;
        margin: 0px 13px;
        border: 2px solid #ccc;
        border-radius: 4px;
        background-color: #f8f8f8;
        resize: none;
        background-color: #dbdbdb;
        ''',
        'rows':'1',
        'cols': '100',
    }))
        

class VictimForm_better(forms.Form):
    
    name = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '1',
        'cols' : '80',
        'style' : 'resize:none; margin: 0px 95px; background-color: #dbdbdb;'
    }))
    current_position = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '1',
        'cols' : '80',
        'style' : 'resize:none; margin: 0px 29px; background-color: #dbdbdb;'
    }))
    location = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '1',
        'cols' : '80',
        'style' : 'resize:none; margin: 0px 76px; background-color: #dbdbdb;'
    }))
    about = forms.CharField(widget=forms.Textarea(attrs={
        'style' : '''
        width: 756px;
        height: 87px;
        resize: none;
        background-color: #dbdbdb;
        '''
    }))
    positions = CommaSeparatedField(label='Positions (separate with commas) ', widget=forms.Textarea(attrs={
        'rows': '1',
        'style' : 'margin: 0px 62px; width: 900px; resize: none; background-color: #dbdbdb;'
    }))
    companies = CommaSeparatedField(label='Companies (separate with commas) ', widget=forms.Textarea(attrs={
        'rows': '1',
        'style' : 'margin: 0px 48px; width: 900px; resize: none; background-color: #dbdbdb;'
    }))
    durations = CommaSeparatedField(label='Durations (separate with commas) ', widget=forms.Textarea(attrs={
        'rows': '2',
        'style' : 'margin: 0px 57px; width: 900px; resize: none; background-color: #dbdbdb;'
    }))
    job_descriptions = CommaSeparatedField(label='Job Descriptions (separate with commas) ', widget=forms.Textarea(attrs={
        'rows': '3',
        'style' : 'margin: 0px 11px; width: 900px; resize: none; background-color: #dbdbdb;'
    }))
    institutions = CommaSeparatedField(label='Institutions (separate with commas) ', widget=forms.Textarea(attrs={
        'rows': '1',
        'style' : 'margin: 0px 45px; width: 900px; resize: none; background-color: #dbdbdb;'
    }))
    tenures = CommaSeparatedField(label='Tenures (separate with commas) ', widget=forms.Textarea(attrs={
        'rows': '1',
        'style' : 'margin: 0px 66px; width: 900px; resize: none; background-color: #dbdbdb;'
    }))
    victim_skills = CommaSeparatedField(label='Skills (separate with commas) ', widget=forms.Textarea(attrs={
        'rows': '4',
        'style' : 'margin: 0px 79px; width: 900px; resize: none; background-color: #dbdbdb;'
    }))
    github_repos = CommaSeparatedField(label='Github Repos (separate with commas) ', widget=forms.Textarea(attrs={
        'rows': '1',
        'style' : 'margin: 0px 26px; width: 900px; resize: none; background-color: #dbdbdb;'
    }))
    template_number = forms.ChoiceField(choices=[("1","1"),("2","2")], required=True, label="Choose the template you would like")
    
# positions, companies, durations, job_descriptions, institutions, tenures, victim_skills, github_repos