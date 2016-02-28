from django.shortcuts import render
from blog1.models import Post, Comment
from django.views.generic.detail import DetailView
from django.views import generic
from django.views.generic import ListView
from django.views.generic import ListView
from blog1.models import Post
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.shortcuts import render
from blog1.forms import PostForm
from django.contrib.auth.models import User


# Create your views here.


#class PostList(ListView):
#	model = Post
#	template_name = 'index.html'

def PostList(request):
	post = Post.objects.all()
	context = { "post":post, "posts":post.all() }
	return render(request, 'index.html', context)


class PostDetail(generic.DetailView):
	model = Post
	template_name = 'blogpost.html'

class CommentList(ListView):
	model = Comment
	template_name = 'blogpost.html'

class PostCreate(generic.edit.CreateView):
	model = Post
	fields = ["title","body","author","categories","tags"]
	template_name = 'index.html'

#def PostCreate(request):
#    # if this is a POST request we need to process the form data
#    if request.method == 'POST':
#        # create a form instance and populate it with data from the request:
#        form = PostForm(request.POST)
#        # check whether it's valid:
#        if form.is_valid():
#            # process the data in form.cleaned_data as required
#            title = form.cleaned_data['title']
#            body = form.cleaned_data['body']
#            author = form.cleaned_data['author']
 #           categories  = form.cleaned_data['categories']
#            categories  = form.cleaned_data['tags']
#            # redirect to a new URL:
#            return HttpResponseRedirect('blogpost.html')
#
#    # if a GET (or any other method) we'll create a blank form
#    else:
 #       form = PostForm()
#
#   return render(request, 'blogpost.html', {'form': form})


def list_and_create(request):
	form = PostForm(data=request.POST)
	if request.method == 'POST':
		
		if form.is_valid():
			hold = form.save(commit=False)
			hold.autor = request.user
			hold.save()

			if 'picturep' in request.FILES:
				hold.picturep  = request.FILES['picturep']
				
				hold.save()
				form.save()
					

	# notice this comes after saving the form to pick up new objects
	post = Post.objects.all()
	return render(request, 'index.html',
		{'post': post,'form': form,  "posts":post.all()})

	#'form': form,

