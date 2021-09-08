from django import forms
from django.forms import ModelForm
from .models import Todolist


class TodolistForm(forms.ModelForm):
    task = forms.CharField(max_length=100)

    class Meta:
        model = Todolist
        fields = '__all__'
