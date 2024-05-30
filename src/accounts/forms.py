from django import forms


class SignupForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(), max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(), max_length=50)
    email = forms.EmailField(help_text="L'adresse mail")
    username = forms.CharField(widget=forms.TextInput(), max_length=50, help_text="Le pseudo")
    password = forms.CharField(widget=forms.PasswordInput(), min_length=6)
    password_repeat = forms.CharField(widget=forms.PasswordInput(), min_length=6)
    
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), max_length=50, help_text="Le pseudo")
    password = forms.CharField( widget=forms.PasswordInput(), min_length=6)