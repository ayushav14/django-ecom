from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-custom',
        'placeholder': 'Enter your first name'
    }))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-custom',
        'placeholder': 'Enter your last name'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-custom',
        'placeholder': 'name@example.com'
    }))
    phone_number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-custom',
        'placeholder': '+91 9876543210'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control form-control-custom',
            'placeholder': 'Choose a unique username'
        })
        if 'password' in self.fields:
            self.fields['password'].widget.attrs.update({'class': 'form-control form-control-custom'})
        if 'password2' in self.fields:
            self.fields['password2'].widget.attrs.update({'class': 'form-control form-control-custom'})


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-custom',
        'placeholder': 'Enter username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-custom',
        'placeholder': 'Enter password'
    }))


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'phone_number',
            'profile_image', 'address_line_1', 'address_line_2',
            'city', 'state', 'postal_code', 'country'
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-custom'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-custom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-custom'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control form-control-custom'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control form-control-custom'}),
            'address_line_1': forms.TextInput(attrs={'class': 'form-control form-control-custom'}),
            'address_line_2': forms.TextInput(attrs={'class': 'form-control form-control-custom'}),
            'city': forms.TextInput(attrs={'class': 'form-control form-control-custom'}),
            'state': forms.TextInput(attrs={'class': 'form-control form-control-custom'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control form-control-custom'}),
            'country': forms.TextInput(attrs={'class': 'form-control form-control-custom'}),
        }
