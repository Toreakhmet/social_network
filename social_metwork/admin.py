from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Like)
admin.site.register(Posts)