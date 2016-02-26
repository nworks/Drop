from django.shortcuts import render
from users.models import Cliente
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic import ListView ,TemplateView
from django.views import generic
from django.http import HttpResponseRedirect ,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response,render
from django.template import RequestContext
from users.forms import LoginForm , UsuarioForm,UsuarioForm2, UserPr
from users.models import Usuario, UserP, FriendList
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class ClienteList(ListView):
	model = UserP
	template_name = 'base.html'

class UserProfile(DetailView):
	model = User
	template_name = 'base.html'

def UserProfile1(request):
	user = UserP.objects.filter(user=request.user)
	context = { "user":user, "users":user.all() }
	return render(request, 'Profile.html', context)




class UsuarioNuevo(generic.edit.CreateView):
	form_class = UsuarioForm
	template_name="2.html"
	success_url = '/blog1/postlog'


def register(request):
	context = RequestContext(request)
	registered = False
	if request.method == 'POST':
		user_form = UsuarioForm2(data=request.POST)
		profile_form = UserPr(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user


			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

				profile.save()
				registered = True
				username = user_form.cleaned_data['username']
				password = user_form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				login(request,usuario)
				return HttpResponseRedirect('/blog1/postlog')
			else:
				print user_form.errors, profile_form.errors

			


	else:
		user_form = UsuarioForm2()
		profile_form = UserPr()

	return render_to_response ('clientes_add.html',{'user_form':user_form, 'profile_form': profile_form}, context_instance=RequestContext(request))





def nuevo_usuario(request):
	if request.method == 'POST':
		avatar_form = UserCreationForm(request.POST)
		if avatar_form.is_valid:
			avatar_form.save()
			username = avatar_form.cleaned_data['username']
			password = avatar_form.cleaned_data['password1']
			usuario = authenticate(username=username,password=password)
			login(request,usuario)
			return HttpResponseRedirect('/users/Clientenuevo2')
	else:
		avatar_form = UserCreationForm(request.POST)
	return render_to_response('clientes_add.html',{'avatar_form': avatar_form }, context_instance=RequestContext(request))


def nuevo_usuario2(request):
	if request.method == 'POST':
		form2 = UsuarioForm(data=request.POST,instance=request.user)
		if form2.is_valid:
			form2.save()
			return HttpResponseRedirect('/blog1/postlog')
	else:
		form2 = UsuarioForm(request.POST)
	return render_to_response('2.html',{'form2': form2 }, context_instance=RequestContext(request))





def LoginRequest(request):
	# Si el usuario ya ha iniciado sesion anteriormente.
	if request.user.is_authenticated():
		return HttpResponseRedirect('/blog1/postlog')
	if request.method == 'POST':
		form = LoginForm(request.POST)
		# Si el formulario es valido, iniciar la sesion y redireccionar
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			usuario = authenticate(username=username,password=password)
			if usuario is not None:
				login(request,usuario)
				return HttpResponseRedirect('/blog1/postlog')
			# De lo contrario devolver al Login
			else:
				return render_to_response('login.html',{'form':form},context_instance=RequestContext(request))
		# Si el formulario es invalido devolver al login
		else:
			return render_to_response('login.html',{'form':form},context_instance=RequestContext(request))
	else:
		form = LoginForm()
		context = {'form':form}
		return render_to_response('login.html',context,context_instance=RequestContext(request))

def LogoutRequest(request):
	logout(request)
	return HttpResponseRedirect('/users/login')

def ProfileUser(request):
	return render(request, 'profile.html')

def Friend_List_And_searh(request):
	friend = FriendList.objects.filter(user=request.user)
	search_query = request.GET.get('search_box',None)
	result = User.objects.filter(username=search_query).order_by( 'first_name') 
	context = { "friend":friend, "friends":friend.all(),"result":result,"results":result.all()}
	return render(request, 'friendlist.html', context)

def ajax_user_search(request):
	q = request.GET.get('search_box')
	if q is not None:
		results = User.objects.filter( fist_name__contains = q).order_by( 'username') 
		return render_to_response('friendlist.html', {'results': results, } , context_instance = RequestContext(request))

def BusquedaView(request):
	search_text = request.GET.get('search_box')
	if search_text is not None:
		search_text 
		
	else:
		search_text = '*'

	result = User.objects.filter(first_name__icontains=search_text) 
	friend = FriendList.objects.filter(user=request.user).order_by( 'friend') 
	context = { "friend":friend, "friends":friend.all(),"result":result,"results":result.all()}
	return render(request, 'friendlist.html', context)

from django.core import serializers
import json
from django.http import JsonResponse

class BusquedaAjax(TemplateView):

	def get(self, request, *args, **kwargs):
		buscar = request.GET['search']
		user = User.objects.filter(first_name__icontains=buscar)
		user_all = User.objects.all()
		data = serializers.serialize('json', user,
			fields=('username','first_name','last_name'))
		decoded_data = json.loads(data) 			

		return JsonResponse({'objects': decoded_data})
        		
		
		

