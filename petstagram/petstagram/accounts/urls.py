from django.urls import path, include

from petstagram.accounts.views import LoginUserView, RegisterUserView, LogoutUserView, ProfileDeleteView, ProfileEditView, ProfileDetailsView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login user'),
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('delete/', ProfileDeleteView.as_view(), name='delete user'),
        path('edit/', ProfileEditView.as_view(), name='edit user'),
        path('', ProfileDetailsView.as_view(), name='details user'),
        ])),

)