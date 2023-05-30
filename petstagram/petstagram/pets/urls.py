from django.urls import path, include

from petstagram.pets.views import add_page, details_page, edit_page, delete_page

urlpatterns = (
    path('add/', add_page, name='add page'),
    path('<str:username>/pet/<slug:pet_name>/', include([
        path('', details_page, name='details page'),
        path('edit/', edit_page, name='edit page'),
        path('delete/', delete_page, name='delete page'),
    ]))
)