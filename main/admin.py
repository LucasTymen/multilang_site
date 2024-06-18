from django.contrib import admin
from .models import Article, Category, Comment, Profile

# Inline for adding comments directly in the article admin page
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1  # Number of empty forms to display

# Admin for Article with CommentInline
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    list_filter = ('publication_date', 'author', 'categories')
    ordering = ('-publication_date',)
    date_hierarchy = 'publication_date'
    filter_horizontal = ('categories',)
    inlines = [CommentInline]  # Add comments inline in article admin page

    # Automatically set the author to the current user and set the publication date
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created, not updated
            obj.author = request.user
        obj.save()

# Inline for adding articles directly in the category admin page
class ArticleInline(admin.TabularInline):
    model = Article.categories.through
    extra = 1  # Number of empty forms to display

# Admin for Category with ArticleInline
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    inlines = [ArticleInline]  # Add articles inline in category admin page

# Admin for Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'email', 'article', 'publication_date')
    search_fields = ('author', 'email', 'content')
    list_filter = ('publication_date', 'article')
    ordering = ('-publication_date',)
    date_hierarchy = 'publication_date'

# Admin for Profile
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')
    search_fields = ('user__username', 'user__email')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile, ProfileAdmin)
