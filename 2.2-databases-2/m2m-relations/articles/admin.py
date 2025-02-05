from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get("is_main"):
                count += 1
            if count > 1:
                raise ValidationError('Только один тэг может быть основным')
        if count == 0:
            raise ValidationError("Хотя бы один тэг должен быть основным")
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    fields = ["tag", "is_main"]
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    list_display = ['title', 'published_at']
    list_filter = ['published_at']
    search_fields = ['title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']



