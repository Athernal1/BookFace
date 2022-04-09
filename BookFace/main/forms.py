from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile, CommentBlog


class LoginForm(AuthenticationForm):

    class Meta:
        model = User


class AddUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "username", "first_name", "last_name", "email", "password1", "password2"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in ("username", "password1", "password2"):
            self.fields[field_name].help_text = None

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get("username")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        user = User.objects.filter(username=username).first()
        if user:
            self.add_error("username", "User already exists.")

        if password1 != password2:
            self.add_error("password2", "Passwords do not match.")

        return cleaned_data


class UpdateUserForm(UserChangeForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    birthday = forms.DateField()
    city = forms.CharField(max_length=32)

    class Meta:
        model = Profile
        fields = ['birthday', 'city']


class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentBlog
        fields = ['content']
