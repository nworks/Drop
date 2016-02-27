from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	bio = models.TextField()
	
	def __str__(self):
		return self.name

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

	def __str__(self):             
		return self.name

class Category(models.Model):
	cat_name = models.CharField('Category Name',max_length=50)
	cat_description = models.CharField('Category Description',max_length=255)
	
	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.cat_name

class Tag(models.Model):
	tag_name = models.CharField(max_length=50)
	tag_description = models.CharField(max_length=255)
	
	def __str__(self):
		return self.tag_name

class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	creatd_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
	autor = models.ForeignKey(User)
	author = models.CharField(max_length=50)
	categories = models.ManyToManyField(Category)
	tags = models.ManyToManyField(Tag)

	class Meta:
		ordering = ["-creatd_date"]
	
	def get_absolute_url(self):
		return("/blog1/postlog")

	def __str__(self):
		return self.title

class Comment(models.Model):
	commentauthor = models.CharField(max_length=50)
	comment_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	comment_body = models.TextField()


	def __str__(self):
		return self.commentauthor

