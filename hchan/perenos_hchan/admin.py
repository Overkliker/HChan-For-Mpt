from django.contrib import admin
from .models import Card, Person, Collection, Manga
# Register your models here.
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('name', 'lastname')

# class RootAdmin(admin.ModelAdmin):
#     list_display = ('identificator', 'passw')

# class MangaAdmin(admin.ModelAdmin):
#     list_display = ('discr', 'name', "date")

# class OcenkaAdmin(admin.ModelAdmin):
#     list_display = ('ocenka', 'prepodavatel')

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('name', 'user_id', 'age')

# admin.site.register(Person, PersonAdmin)
# admin.site.register(Root, RootAdmin)
# admin.site.register(Manga, MangaAdmin)
# admin.site.register(Postavte5, OcenkaAdmin)
# admin.site.register(Profile, ProfileAdmin)

class CardDisplay(admin.ModelAdmin):
    list_display = ('id', 'title', 'text' , 'img')

class PersonDisplay(admin.ModelAdmin):
    list_display = ('id', 'name', 'password', 'avatar')

class CollectionDisplay(admin.ModelAdmin):
    list_display = ('id', 'person_id', 'card_id')

class MangaDisplay(admin.ModelAdmin):
    list_display = ('id', 'manga_id', 'file_name')

admin.site.register(Card, CardDisplay)
admin.site.register(Person, PersonDisplay)
admin.site.register(Collection, CollectionDisplay)
admin.site.register(Manga, MangaDisplay)