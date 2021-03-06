from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User

        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
            )

        def save(self, commit=True):
            user = super(RegistrationForm,self).save(commit=False)
            user.first_name=self.cleaned_data
            user.last_name=self.cleaned_data
            user.email=self.cleaned_data

            if commit:
                user.save()

            return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User

        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
                )
