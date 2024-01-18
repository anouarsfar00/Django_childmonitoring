from django.contrib import admin

from toy.models import ChildPlace, Child, Parent, Place
#from .models import parent,child,place,ChildPlace
# Register your models here.
admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(ChildPlace)
admin.site.register(Place)
