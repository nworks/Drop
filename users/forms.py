from django import forms
from models import Cliente, Usuario, UserP, FriendList
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["first_name","last_name","email"]
		

class LoginForm(forms.Form):
	username = forms.CharField(label=(u'Usuario'))
	password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))


	
class UsuarioForm2(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","password","first_name","last_name","email"]

class UserForm(forms.ModelForm):
		password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
		
		class Meta:
			model = User
			fields = ["username","password","email"]

class UserPr(forms.ModelForm):
		class Meta:
			model = UserP
			fields = ["picture"]

class FriendForm(forms.ModelForm):
	class Meta:
		model = FriendList
		fields = ["user","friend","friendship"]


				


				
		

