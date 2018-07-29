from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.Course)
admin.site.register(models.Section)
admin.site.register(models.CourseItem)
