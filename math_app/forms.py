from django import forms


class Triangle(forms.Form):
    cath_x = forms.IntegerField(label="Cath X", help_text='cm', required=True, min_value=1)
    cath_y = forms.IntegerField(label="Cath Y", help_text='cm', required=True, min_value=1)

