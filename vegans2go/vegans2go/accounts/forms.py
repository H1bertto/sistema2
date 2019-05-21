from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Usuario


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="Nome", widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    email = forms.EmailField(
        label="E-mail", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(
        label="Usuário", widget=forms.TextInput(attrs={'placeholder': 'Usuário'}))
    password = forms.CharField(
        label="Senha", widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))

    class Meta:
        model = Usuario
        fields = ("nome", "email", "username", "password",)

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["username"]
        user.password = self.cleaned_data["password"]

        if commit:
            user.save()
        return user
