from django.contrib import admin
from .models import Finch, Location, Feed
# Register your models here.
admin.site.register(Finch)
admin.site.register(Location)
admin.site.register(Feed)