from django.shortcuts import redirect

from petstagram.common.models import PhotoLike


def get_user_liked_photos(photo_id, user):
    return PhotoLike.objects.filter(photo_id=photo_id, user=user).first()


def get_photo_url(request, photo_id):
    return request.META['HTTP_REFERER'] + f'#photo-{photo_id}'
