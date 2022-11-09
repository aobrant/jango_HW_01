from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError

from .models import Article, Scope,Tag


@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):
    model = Tag

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self) -> None:
        counter = 0

        for form in self.forms:
            if form.cleaned_data['is_main']:
                    counter += 1
            if counter > 1 or counter ==0 :
                    raise ValidationError('Error')




        return super().clean()

class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset

@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
