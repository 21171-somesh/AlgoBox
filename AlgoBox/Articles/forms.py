from django import forms
from . import models
from pagedown.widgets import PagedownWidget

class CreateArticle(forms.ModelForm):
	content = forms.CharField(widget = PagedownWidget())
	class Meta:
		model = models.Post
		fields = ['title', 'slug', 'content', 'status']
