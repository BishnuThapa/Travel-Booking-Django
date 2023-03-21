from django.contrib import admin
from .models import *
# Register your models here.


class Itinerary(admin.StackedInline):
    model = Itinerary
    extra = 1


class Faq(admin.StackedInline):
    model = Faq
    extra = 1


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('heading', 'sub_heading', 'updated_at')


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['name', ]
    }
    list_display = ('name', 'ordering', 'created_at', 'updated_at')


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Tour_Type)
class TourTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['name', ]
    }


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    # filter_horizontal = ('included', 'excluded')
    prepopulated_fields = {
        'slug': ['name', ]
    }
    inlines = (Itinerary, Faq)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    prepopulated_fields = {
        'slug': ['title', ]
    }
