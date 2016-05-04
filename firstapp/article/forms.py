# -*- coding: utf-8  -*-

from django.forms import ModelForm
from models import Comments

class CommentForm(ModelFrom):
    class Meta:
        model = Comments
