from django.contrib import admin
from home2.models import Home2

@admin.register(Home2)
class Home2(admin.ModelAdmin):
    list_display = ('image','work_image', 'title', 'sub_title', 'title_word', 'sub_title_word' )
    list_display_links = ('image', 'work_image', 'title', 'sub_title', 'title_word', 'sub_title_word')