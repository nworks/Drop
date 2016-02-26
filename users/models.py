from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from PIL import Image


# Create your models here.
class Cliente(models.Model):
	username = models.CharField(unique=True,max_length=100, null=False, blank=True,)
	nombre_completo = models.CharField(max_length=100, null=False, blank=True,)
	vacio = models.CharField('Password',unique=True,max_length=15, null=False, blank=True)
	Empthy = models.EmailField('Email',unique=True)
	numero_tel = models.CharField(max_length=50, null=True, blank=False)
	numero_cel = models.CharField(max_length=50, null=True, blank=False)
	direccion = models.CharField(max_length=200, null=False, blank=False)
	fechaintro = models.DateField(auto_now=True,null=False,blank=False)
	creditcard = models.CharField(unique=True,max_length=15, null=False, blank=True)
	
	estatus = models.BooleanField(default=True,verbose_name="Cliente Activo?")
	
	def __str__(self):
		return self.username

class Usuario(models.Model):
	user_pic = models.ImageField(upload_to='userpic/', null=True)
	password = models.CharField(max_length=100, null=True, blank=True,)
	username = models.CharField(unique=True,max_length=100, null=True, blank=True,)
	email = models.EmailField('Email',unique=True)
	first_name = models.CharField(max_length=25, null=False, blank=True,)
	last_name = models.CharField(max_length=25, null=False, blank=True,)

	def __str__(self):
		return self.username

class UsuarioProfile(models.Model):
	user_pic = models.ImageField(upload_to='userpic/', null=True)
	idfield = models.CharField(max_length=25, null=False, blank=True,)
	
	
	def __str__(self):
		return self.idfield

class UserP(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='userpic/', blank=True)
	
	def __str__(self):
		return self.user.username

class FriendList(models.Model):
	user = models.ForeignKey(User)
	friend = models.ForeignKey(User, related_name="friends")
	friendship = models.BooleanField(default=True, verbose_name="Amigos!")
	create_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	  
	class Meta:
		ordering = ["friend"]
	
	def __str__(self):
		return self.user.username





