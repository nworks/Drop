from django.conf.urls import url
from . import views
from blog1.views import PostList, CommentList, PostCreate
from blog1.views import PostDetail


urlpatterns = [
    
    #url(r'^postlog/', 'blog1.views.PostList'),
    #url(r'^postlog/$', PostList.as_view()),
    #url(r'^postlog/', 'blog1.views.PostCreate'),
    #url(r'^postlog/$', PostCreate.as_view(),'blog1.views.list_and_create', name = "PostCreate" ),
    url(r'postlog/$', 'blog1.views.list_and_create'),
    url(r'^postdetail/(?P<pk>\d+)/', PostDetail.as_view(template_name='blogpost.html')),
    
]