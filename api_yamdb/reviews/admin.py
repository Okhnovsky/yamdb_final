from django.contrib import admin


from .models import Category, Genre, Title, Review


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class TitleAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'year', 'description')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'score')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Review, ReviewAdmin)
