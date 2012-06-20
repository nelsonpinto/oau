from bootstrap.forms import BootstrapForm, Fieldset
from django import forms

class LoginForm(BootstrapForm):
    class Meta:
        layout = (
            Fieldset("Please Login", "username", "password", ),
        )

    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=100)