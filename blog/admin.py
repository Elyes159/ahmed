from django.contrib import admin
from django.contrib.admin import register
# Register your models here.
from blog.models import CompteSnapchat
@register(CompteSnapchat)
class CompteSnapAdmin(admin.ModelAdmin):
    list_display =['nom_compte','description','followers']