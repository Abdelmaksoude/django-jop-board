from django.contrib import admin
from .models import Jop , Category , Apply , Comment
# Register your models here.
admin.site.register(Jop)   
admin.site.register(Category)   
admin.site.register(Apply)
admin.site.register(Comment)