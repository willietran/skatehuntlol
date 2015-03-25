from django.contrib.auth.forms import UserCreationForm
from django import forms
from skatehuntapp.models import User

__author__ = 'WillieTran'


class NewUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    image = forms.ImageField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['password2'].label = "Confirm Password"

    class Meta:
        model = User
        fields = ("username", "first_name", "email", "password1", "password2",
                  "image")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(u'Email Addresses Must Be Unique.')


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={'placeholder':'Title'})
    )
    url = forms.CharField(
        max_length=140,
        widget=forms.TextInput(attrs={'placeholder':'http://example.com'})
    )
    description = forms.CharField(
        max_length=140,
        widget=forms.TextInput(attrs={'placeholder':'Brief Description'})
    )