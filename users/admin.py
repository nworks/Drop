from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


from users.models import Cliente, Usuario, UserP, FriendList
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(FriendList)
#admin.site.register(UsuarioProfile)


#class UserProfileInline(admin.StackedInline):
#	model = UsuarioProfile

#class UserModelAdmin(UserAdmin):
#	inlines = [UserProfileInline,]

#admin.site.unregister(User)
#admin.site.register(User,UserModelAdmin)
admin.site.register(UserP)


