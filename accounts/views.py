from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import UserRegistrationForm, UserLoginForm, EmailValidationOnForgotPassword, UserForm, \
    UserProfileForm
from accounts.models import Profile


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


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = UserProfileForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_form = UserForm(self.request.POST or None, instance=self.request.user)
        # user_profile_form = UserProfileForm(self.request.POST or None, self.request.FILES or None,
        #                                     instance=self.request.user.profile)
        context['user_form'] = user_form
        # context['profile_form'] = user_profile_form


# @login_required(login_url='/accounts/login/')
# def user_edit_view(request, slug):
#     query_set = get_object_or_404(UserProfile, slug=slug)
#     user_form = UserForm(request.POST or None, instance=query_set.user)
#     user_profile_form = UserProfileForm(request.POST or None, request.FILES or None, instance=query_set)
#
#     # Declare session['previous_url'] for once and delete it after post process
#     if 'previous_url' not in request.session:
#         request.session['previous_url'] = request.META.get('HTTP_REFERER')
#     if user_form.is_valid() and user_profile_form.is_valid():
#         user_form.save()
#         user_profile_form.save()
#         previous_url = request.session['previous_url']  # Save the session before the deletion
#         del request.session['previous_url']
#         return redirect(previous_url)
#     context = {
#         'user_form': user_form,
#         'user_profile_form': user_profile_form,
#     }
#     return render(request, 'accounts/userprofile_form.html', context)
#
