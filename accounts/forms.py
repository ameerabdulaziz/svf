from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, HTML
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter Email'}))
    password1 = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Password Confirmation', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password Confirmation'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        labels = {
            'password1': 'Password',
            'password2': 'Password Confirmation',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus', None)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('username', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('password1', css_class='form-group col-md-6 mb-0'),
                Column('password2', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Register New Account', css_class='form-group'),
            # HTML('''<span class="small"> Already have an account? <a href="{% url 'accounts:login' %}?next={{ request.path }}">Login To Your Account</a></span>'''),
        )


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus', None)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('password', css_class='form-group mb-0'),
                css_class='form-row'
            ),
            Row(
                Submit('submit', 'Login', css_class='form-group'),
                HTML('''<a class="m-2" href="{% url 'accounts:password_reset' %}?next={{ request.path }}"> Forgot password?</a>'''),
                css_class='form-row'
            ),
        )


class EmailValidationOnForgotPassword(PasswordResetForm):
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter Email'}))

    def __init__(self, *args, **kwargs):
        super(EmailValidationOnForgotPassword, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group mb-0'),
                css_class='form-row',
            ),
            Row(
                Column(
                    Submit('submit', 'Recover Your Password', css_class='btn'),
                    css_class='text-center',
                ),
            ),
        )

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError("There is no user registered with the specified email address!")
        return email
