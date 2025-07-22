from django import forms

class CoverageForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    city = forms.CharField()
    income = forms.FloatField()
    dependents = forms.IntegerField()


