from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(WebInfo)
admin.site.register(Entry)
admin.site.register(Hover)
admin.site.register(Click)
admin.site.register(Pages)