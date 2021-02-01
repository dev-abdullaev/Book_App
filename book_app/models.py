from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    author = models.CharField(max_length=50)
    book_type = models.CharField(max_length=250)
    description = models.TextField(null=False)
    img = models.URLField(max_length=5000)
    upload_file = models.FileField(upload_to="upload/")

    STATUS = (
        ('Please Choose Status', ('Please Choose Status')),
        ("I haven't started yet", ("I haven't started yet")),
        ("I'm reading", ("I'm reading")),
        ('I finished', ('I finished')),
    )

    status = models.CharField(
        max_length=50, choices=STATUS, default='Please Choose Status')

    def __str__(self):
        return self.title
