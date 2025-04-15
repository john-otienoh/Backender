from django import forms
from .models import Employee

GENDER = [("M", "Male"), ("F", "Female"), ("O", "Other")]


class EmployeeForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
                "class": "form-control",
                "id": "exampleInputName",
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control",
                "id": "exampleInputEmail1",
            }
        ),
    )
    contact = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter phone number",
                "min": "100000",
                "max": "9999999999",
            }
        ),
    )
    employee_number = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter employee number",
                "min": "1",
                "max": "1000",
                "id": "exampleInputEmployeeNumber"
            }
        ),
    )
    gender = forms.ChoiceField(
        choices=GENDER,
        required=True,
        widget=forms.RadioSelect(
            attrs={
                "class": "form-check-input",
                "name": "flexRadioDefault",
                "id": "exampleInputGender",
            }
        ),
    )

    class Meta:
        model = Employee
        fields = ["name", "email", "contact", "employee_number", "gender"]
