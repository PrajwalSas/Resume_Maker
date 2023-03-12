from django.contrib import admin

# Register your models here.
from .models import Victim, LinkedIn

admin.site.register(Victim)

admin.site.register(LinkedIn)
