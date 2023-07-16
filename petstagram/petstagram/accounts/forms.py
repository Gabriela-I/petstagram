from django.contrib.auth import forms, get_user_model

UserModel = get_user_model()


class RegisterUserForm(forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2',)
