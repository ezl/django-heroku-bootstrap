from django import forms
from models import UserProfile
from django.contrib.auth.forms import (
        UserCreationForm as AuthUserCreationForm,
        AuthenticationForm as AuthAuthenticationForm)


class EmailAuthenticationForm(AuthAuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(EmailAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label="Email"
        self.error_messages.update(
            {'invalid_login': ("Please enter a correct email and password. "
                                "Note that both fields are case-sensitive.")
            })

    def clean(self):
        self.cleaned_data['username'] = self.cleaned_data['username'].lower()
        return super(EmailAuthenticationForm, self).clean()

class EmailUserCreationForm(AuthUserCreationForm):
    def __init__(self, *args, **kwargs):
        super(EmailUserCreationForm, self).__init__(*args, **kwargs)
        self.error_messages.update(
            {'duplicate_username': "Looks like you've already signed up before!"})

    username = forms.EmailField(label="Email")

    def clean(self):
        self.cleaned_data['username'] = self.cleaned_data['username'].lower()
        return super(EmailUserCreationForm, self).clean()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user')
