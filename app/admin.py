from django.contrib import admin
from .models import Signup
from .models import token_verify

# Register your models here.

admin.site.register(Signup)
admin.site.register(token_verify)
# @admin.register(token_verify)
# class profile(admin.ModelAdmin):
#     list_display = ['user_id','tokken','verify']