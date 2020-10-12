from django.contrib import admin

# Register your models here.
from .models import Mentor, Project, Mentorship

admin.site.register(Mentor)
admin.site.register(Project)
admin.site.register(Mentorship)
