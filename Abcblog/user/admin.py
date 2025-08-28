from django.contrib import admin # type: ignore
from user.models import User, Profile # type: ignore

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)