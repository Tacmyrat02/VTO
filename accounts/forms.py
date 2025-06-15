from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'avatar']
class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'