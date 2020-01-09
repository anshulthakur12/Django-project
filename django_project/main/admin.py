from django.contrib import admin
from .models import AccessRecord, WebPage, Topic, UserProfileInfo

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(WebPage)


