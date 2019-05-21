from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Usuario


class UserCreationForm(forms.ModelForm):
    nome = forms.CharField(
        label="Nome", widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    email = forms.EmailField(
        label="E-mail", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(
        label="Usuário", widget=forms.TextInput(attrs={'placeholder': 'Usuário'}))
    password = forms.CharField(
        label="Senha", widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))

    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'username', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'username',
                  'password', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('nome', 'email', 'username', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('nome', 'email',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nome', 'email', 'username', 'password')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(Usuario, UserAdmin)
admin.site.unregister(Group)
