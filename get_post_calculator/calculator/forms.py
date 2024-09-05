from django import forms

class CalculatorForm(forms.Form):
    number1 = forms.FloatField(label='Number 1', required=True)
    number2 = forms.FloatField(label='Number 2', required=True)
    operation = forms.ChoiceField(
        label='Operation',
        choices=[
            ('add', 'Add'),
            ('subtract', 'Subtract'),
            ('multiply', 'Multiply'),
            ('divide', 'Divide')
        ],
        required=True
    )