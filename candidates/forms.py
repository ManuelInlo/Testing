from django import forms 
from .models import Candidate

class DateInput(forms.DateInput):
    input_type = 'date'

class CandidateForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = (
            'recruiter',
            'first_name',
            'second_name',
            'last_name',
            'second_last_name',
            'birthdate',
            'email',
            'phone',
            'comments',
            'source',
        )

        widgets = {
            'birthdate': DateInput()
        }
