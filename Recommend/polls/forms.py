# forms.py
from django import forms
from .models import food
from django.db.models import Q

class CheckBox(forms.Form):
    food_names = forms.MultipleChoiceField(
        choices = lambda: [(Food.name, Food.name) for Food in food.objects.all()],
        widget = forms.CheckboxSelectMultiple,
        required = False
    )
    def __init__(self, user, *args, **kwargs):
        self.current_user = user
        super().__init__(*args, **kwargs)
        food.objects = food.objects.filter(Q(user_name=self.current_user)|Q(user_name=1))

class calorie_form(forms.Form):
    calorie = forms.DecimalField(label='目標摂取カロリー', max_digits=10000, decimal_places=0)

class insert_name(forms.Form):
    name = forms.CharField(label='食材名',max_length=100)

class insert_calorie(forms.Form):
    calorie = forms.IntegerField(label='カロリー')

class insert_value(forms.Form):
    value = forms.IntegerField(label='たんぱく質量')

class test_form(forms.Form):
    food_name = forms.MultipleChoiceField(
        choices = food.objects.values_list('name','name').distinct(),
        widget = forms.CheckboxSelectMultiple,
        required = False
    )