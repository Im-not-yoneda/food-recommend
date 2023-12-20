# forms.py
from django import forms
from .models import food

class CheckBox(forms.Form):
    food_names = forms.MultipleChoiceField(
        choices = food.objects.values_list('name','name').distinct(),
        widget = forms.CheckboxSelectMultiple,
        required = False
    )

class calorie_form(forms.Form):
    calorie = forms.DecimalField(label='目標摂取カロリー', max_digits=10000, decimal_places=0)

class insert_name(forms.Form):
    name = forms.CharField(label='name',max_length=100)

class insert_calorie(forms.Form):
    calorie = forms.IntegerField(label='calorie')

class insert_value(forms.Form):
    value = forms.IntegerField(label='value')

class test_form(forms.Form):
    food_name = forms.MultipleChoiceField(
        choices = food.objects.values_list('name','name').distinct(),
        widget = forms.CheckboxSelectMultiple,
        required = False
    )