from django.contrib import admin
from .models import ImageModel, ContactModel, UserModel


class UserAdmin(admin.ModelAdmin):
    user_id = (id,)


admin.site.register(UserModel, UserAdmin)


class ImageAdmin(admin.ModelAdmin):
    image_id = (id,)


admin.site.register(ImageModel, ImageAdmin)


class ContactAdmin(admin.ModelAdmin):
    contact_id = (id,)


admin.site.register(ContactModel, ContactAdmin)
