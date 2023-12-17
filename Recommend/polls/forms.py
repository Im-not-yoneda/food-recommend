# forms.py
from django import forms
from .models import food

class CheckBox(forms.Form):
    food_names = forms.MultipleChoiceField(
        choices = food.objects.values_list('name','name').distinct(),
        widget = forms.CheckboxSelectMultiple,
        required = False
    )

class test_form(forms.Form):
    food_name = forms.MultipleChoiceField(
        choices = food.objects.values_list('name','name').distinct(),
        widget = forms.CheckboxSelectMultiple,
        required = False
    )

class NumberInput(forms.Form):
    number = forms.DecimalField(label='目標摂取カロリー', max_digits=10000, decimal_places=0)