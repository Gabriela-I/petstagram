from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from petstagram.common.utils import get_user_liked_photos
from petstagram.photos.models import Photo
from petstagram.photos.photos_forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm


class PhotoAddView(CreateView):
    template_name = 'photos/photo-add-page.html'
    form_class = PhotoCreateForm
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse('details photo', kwargs={
            'pk': self.object.pk,
        })

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


# @login_required
# def add_photo(request):
#     if request.method == 'GET':
#         form = PhotoCreateForm()
#     else:
#         form = PhotoCreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             photo = form.save()
#             return redirect('details photo', pk=photo.pk)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'photos/photo-add-page.html', context)

@login_required
def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    context = {
        'photo': photo,
        'has_user_liked_photo': get_user_liked_photos(pk, request.user),
        'likes_count': photo.photolike_set.count(),
    }

    return render(request, 'photos/photo-details-page.html', context)


@login_required
def edit_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PhotoEditForm(instance=photo)
    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('details photo', pk=pk)

    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, 'photos/photo-edit-page.html', context)


@login_required
def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('index')
