from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views, get_user_model, login
from django.contrib.auth import forms

from petstagram.accounts.forms import RegisterUserForm

UserModel = get_user_model()


class LoginUserView(views.LoginView):
    template_name = 'account/login-page.html'
    success_url = ''
    # return render(request, 'account/login-page.html')


class RegisterUserView(generic.CreateView):
    template_name = 'account/register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')
        return context

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)


class LogoutUserView(LoginRequiredMixin, views.LogoutView):
    ...


def delete_user(request, pk):
    return render(request, 'account/profile-delete-page.html')


class ProfileDetailsView(generic.DetailView):
    template_name = 'account/profile-details-page.html'
    model = UserModel
    profile_image = static('images/person.png')

    def get_profile_image(self):
        if self.object.profile_picture is not None:
            return self.object.profile_picture
        return self.profile_image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['profile_image'] = self.get_profile_image()
        context['pets'] = self.request.user.pet_set.all()

        return context


class ProfileEditView(generic.UpdateView):
    template_name = 'account/profile-edit-page.html'


class ProfileDeleteView(generic.DeleteView):
    template_name = 'account/profile-delete-page.html'
