from django import forms
from models import Post
from django.contrib.auth.models import User

#class PostForm(forms.Form):
#	class Meta:
#		model = Post
#		fields = ["title","body","author","categories","tags"]

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ["title","picturep","body"]


		
		
#class PostForm(forms.Form):
#	
#	title = forms.CharField(max_length=200)
#	body = forms.CharField(widget=forms.Textarea)
#	author = forms.CharField(max_length=200)
#	categories = forms.CharField(max_length=200)
#	tags = forms.CharField(max_length=200)