from django import forms

from .models import Person


class Triangle(forms.Form):
    cath_x = forms.IntegerField(label="Cath X", help_text='cm', required=True, min_value=1)
    cath_y = forms.IntegerField(label="Cath Y", help_text='cm', required=True, min_value=1)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
