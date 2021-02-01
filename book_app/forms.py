from django import forms
from django.forms import ModelForm, HiddenInput
from .models import Book
from crispy_forms.layout import Field


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = "__all__"
