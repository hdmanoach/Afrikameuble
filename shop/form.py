from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full border border-gray-300 rounded-lg px-3 py-2 focus:ring-2 focus:ring-orange-500 focus:outline-none'
            })

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'w-full border border-gray-300 rounded-xl px-4 py-3 focus:ring-2 focus:ring-orange-500 focus:outline-none text-lg',
            'placeholder': 'Nom d’utilisateur',
            'autocomplete': 'username',
        })

        self.fields['password'].widget.attrs.update({
            'class': 'w-full border border-gray-300 rounded-xl px-4 py-3 pr-10 focus:ring-2 focus:ring-orange-500 focus:outline-none text-lg',
            'placeholder': 'Mot de passe',
            'autocomplete': 'current-password',
            'id': 'id_password',  # requis pour l'icone 👁️
        })
