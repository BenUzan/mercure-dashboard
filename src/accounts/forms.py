from django import forms


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(help_text="L'adresse mail")
    pseudo = forms.CharField(max_length=50, help_text="Le pseudo")
    password = forms.CharField(min_length=6, help_text="Le mdp")