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

    list_display = ('name',)
    search_fields = ['name']

class TweetResultDataAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Date', {'fields' : ['date'], 'classes':['collapse']}),
        (None, {'fields':['tweetcounts']}),
        (None, {'fields':['approval_rate']}),
        (None, {'fields':['cityname']}),
        (None, {'fields':['city']}),
    ]

    list_display = ('date','cityname',)
    list_filter = ['date','cityname']
    search_fields = ['category_name','cityname']


admin.site.register(TweetResultData, TweetResultDataAdmin)
admin.site.register(City, CityAdmin)