from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


def save(self, commit=True):
    user = super(UserRegisterForm, self).save(commit=False)
    user.set_password(self.cleaned_data["password"])
    user.save()
    profile = Profile(user=user, tarif_level=0, access_level=0)
    profile.save()
    return user
