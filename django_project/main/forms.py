from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo

from django.core import validators


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio', 'profile_pic')


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter Email Again")
    text = forms.CharField(widget=forms.Textarea)
    #bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_data_clean = super().clean()
        email = all_data_clean['email']
        v_email = all_data_clean['verify_email']

        if email != v_email:
            raise forms.ValidationError("Email are not match")


'''def clean_bot_catcher(self):
        bot_catcher = self.cleaned_data['bot_catcher']
        if len(bot_catcher)>0:
            raise forms.ValidationError("GotCH BOT!")
        return bot_catcher'''

