from django.contrib import admin
from .models import Defect , UserProfile , modelGlass , modelGlassWithDefect 


# Register your models here.
admin.site.register(modelGlass)
admin.site.register(Defect)
admin.site.register(UserProfile)
admin.site.register(modelGlassWithDefect)
# admin.site.register(modelGlassWithDefect_for_export)


