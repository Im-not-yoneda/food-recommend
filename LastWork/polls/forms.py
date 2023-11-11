# forms.py
from django import forms

class CheckBox(forms.Form):
    chickin_reg = forms.BooleanField(label='鶏もも肉', required=False)
    chickin_chest = forms.BooleanField(label='鶏むね肉', required=False)
    brrocori = forms.BooleanField(label='ブロッコリー', required=False)
    carrot = forms.BooleanField(label='にんじん', required=False)
    onion = forms.BooleanField(label='たまねぎ', required=False)
    beef = forms.BooleanField(label='牛もも肉', required=False)
    pork = forms.BooleanField(label='豚バラ肉', required=False)
    rice = forms.BooleanField(label='ごはん', required=False)
    potato = forms.BooleanField(label='じゃがいも', required=False)


class NumberInput(forms.Form):
    number = forms.DecimalField(label='目標摂取カロリー', max_digits=10000, decimal_places=0)