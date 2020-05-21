from django.contrib import admin
from .models import TweetResultData,City

# Register your models here.

class CityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['name']}),
        (None, {'fields':['average_income']}),
        (None, {'fields':['education_level']}),
        (None, {'fields':['migration_percentage']}),
    ]

    list_display = ('category_name')
    search_fields = ['category_name']

class TweetResultDataAdmin(admin.ModelAdmin):
    filter_horizontal = ('city',)
    fieldsets = [
        ('Date', {'fields' : ['date'], 'classes':['collapse']}),
        (None, {'fields':['tweetcounts']}),
        (None, {'fields':['location']}),
        (None, {'fields':['approval_rate']}),
        (None, {'fields':['cityname']}),
        (None, {'fields':['city']}),
    ]

    list_display = ('date','cityname')
    list_filter = ['date','cityname']
    search_fields = ['category_name','cityname']
