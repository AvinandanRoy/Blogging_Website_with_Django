from django.contrib import admin

from blogs.models import Blog,Category

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    
    list_display=['title', 'author','category' ,'status', 'is_featured','created_at', 'updated_at','created_at_year']
    list_display_links = ['title']
    list_filter = ['category','created_at', 'updated_at', 'status', 'is_featured']
    search_fields = ['title', 'author__username', 'category__category_name' , 'status',]
    ordering = ('-created_at',) # created_at field er upor descending order e blog gulo dekhabe. ascending order e dekhate chaile ordering = ('created_at',) use korte hobe.
    readonly_fields = ('created_at', 'updated_at') # created_at and updated_at field gulo ke read-only kore dibe, mane admin panel e edit kora jabe na.
    list_per_page = 10 # admin panel e prottek page e 10 ta blog dekhabe. jodi beshi blog thake tahole next page e click kore baki blog gulo dekhte parbe.
    date_hierarchy = 'created_at' # admin panel e created_at field er upor date hierarchy dekhabe, mane year, month, day wise filter korte parbe.
    list_editable = ['is_featured',] # admin panel e list_display er vitor dekhano status and is_featured field gulo ke edit korte parbe, mane list_display er vitor dekhano status and is_featured field gulo ke directly edit korte parbe, without going to the change page of the blog.
        
    # Nijer banano function jeta list_display er vitor dekhano hoyeche
    def created_at_year(self, obj):
        return obj.created_at.year

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)