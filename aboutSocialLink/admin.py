from django.contrib import admin

from aboutSocialLink.models import About, Social_Media_Link

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, req ):
        count = About.objects.all().count()
        if count == 0:
            return True
        else:
            return False
    

# Register your models here.

admin.site.register(About, AboutAdmin)
admin.site.register(Social_Media_Link)  