from django import forms


class SignupForm(forms.Form):
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Prenom',
                'class': 'form-control',
                'id': 'floatingInput'}))

    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Post-nom',
                'class': 'form-control',
                'id': 'floatingInput'}))

    email = forms.EmailField(
        help_text="L'adresse mail",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'E-mail',
                'class': 'form-control',
                'id': 'floatingInput'}))

    username = forms.CharField(
        max_length=50,
        help_text="Le pseudo",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Nom d'utilisateur",
                'class': 'form-control',
                'id': 'floatingInput'}))

    password = forms.CharField(
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Mot de passe',
                'class': 'form-control',
                'id': 'floatingInput'}))

    password_repeat = forms.CharField(
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirmer mot de passe',
                'class': 'form-control',
                'id': 'floatingInput'}))


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        help_text="Nom d'utilisateur",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Exemple',
                'class': 'form-control',
                'id': 'floatingInput'}))

    password = forms.CharField(
        max_length=6,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Mot de passe',
                'class': 'form-control',
                'id': 'floatingInput'}))
