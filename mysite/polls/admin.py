# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Question, Choice

# or admin.StackedInline
# Now choices can be added when adding a question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # By default, Django displays the str() of each object. 
    # But sometimes it’d be more helpful if we could display individual fields:
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Field to filter by and an appropriate sidebar depending on the db type:
    list_filter = ['pub_date']
    # Fields to search by (pagination default 100 items per page):
    search_fields = ['question_text']

# Before 2: 
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]
    


#  Before 1: The order of Question fields in the admin form can be changed this way:
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)


#admin.site.register(Choice)
