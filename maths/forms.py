from django import forms
from maths.models import Evaluations


class CreateNewEvaluationsForm(forms.ModelForm):
    # eval = forms.CharField(max_length=50)
    # answer = forms.CharField(max_length=3)

    class Meta:
        model = Evaluations
        fields = ['eval', 'answer']
