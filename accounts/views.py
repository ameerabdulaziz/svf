from django.contrib.auth import login
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import UserRegistrationForm, UserLoginForm, EmailValidationOnForgotPassword


class UserRegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.request.GET.get('next', '/'))
        else:
            return super(UserRegisterView, self).get(request)

    def get_success_url(self):
        login(self.request, self.object)
        return self.request.GET.get('next', '/')


class UserLoginView(LoginView):
    form_class = UserLoginForm
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'



class PasswordReset(PasswordResetView):
    form_class = EmailValidationOnForgotPassword
    template_name = 'accounts/password_reset_form.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')


class PasswordResetDone(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'
    success_url = reverse_lazy('accounts:password_reset_confirm')


class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
