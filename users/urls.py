from django.conf.urls import patterns, include, url
from . import views
from users.views import UsuarioNuevo
from users.views import Usuario,UserProfile,BusquedaView,BusquedaAjax
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    #url(r'^Clientenuevo2/$', UsuarioNuevo.as_view()),
    url(r'Clientenuevo/$', 'users.views.register'),
    url(r'friends2/$', 'users.views.Friend_List_And_searh'),
    url(r'friends/$', 'users.views.BusquedaView'),
    url(r'perfil/$', 'users.views.Friend_List_And_searh'),
    # CUENTAS
    url(r'login/$', 'users.views.LoginRequest'),
    url(r'logout/$', 'users.views.LogoutRequest'),
    url(r'^perfil/(?P<pk>\d+)/', UserProfile.as_view(template_name='Profile.html')),
   url(r'buscaramigos/$', BusquedaAjax.as_view()),
     
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

