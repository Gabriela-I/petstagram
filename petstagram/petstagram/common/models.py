from django.db import models

from petstagram.photos.models import Photo


class PhotoComment(models.Model):
    MAX_TEXT_LENGTH = 300
    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,

    )

    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )


class PhotoLike(models.Model):
    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )
