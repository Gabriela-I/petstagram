import pyperclip
from django.shortcuts import render, redirect
from django.urls import reverse

from petstagram.common.common_forms import CommentForm, SearchForm
from petstagram.common.models import PhotoLike
from petstagram.common.utils import get_user_liked_photos, get_photo_url
from petstagram.core.photo_utils import apply_likes_count, apply_user_liked_photo
from petstagram.photos.models import Photo


def index(request):
    search_form = SearchForm(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['pet_name']

    photos = Photo.objects.all()
    if search_pattern:
        photos = photos.filter(tagged_pets__name__icontains=search_pattern)
    photos = [apply_likes_count(photo) for photo in photos]
    photos = [apply_user_liked_photo(photo) for photo in photos]
    
    context = {
        'photos': photos,
        'comment_form': CommentForm(),
        'search_form': search_form,
    }

    return render(request, 'common/home-page.html', context)


def like_photo(request, photo_id):
    user_liked_photos = get_user_liked_photos(photo_id)
    if user_liked_photos:
        user_liked_photos.delete()
    else:
        photo_like = PhotoLike(
            photo_id=photo_id,
        )
        photo_like.save()

    return redirect(get_photo_url(request, photo_id))


def share_photo(request, photo_id):
    photo_details_url = reverse('details photo', kwargs={'pk': photo_id})
    pyperclip.copy(photo_details_url)
    return redirect(get_photo_url(request, photo_id))


def comment_photo(request, photo_id):
    photo = Photo.objects.filter(pk=photo_id).get()
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.photo = photo
        comment.save()
    return redirect('index')
