from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = models.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','first_name','email','password1','password2']

    def save(self, commit=True):
        user = super(RegistrationForm, self.save(commit=False))
        user.first_name = cleaned_data['first_name']

        if commit:
            user.save()

        return user
