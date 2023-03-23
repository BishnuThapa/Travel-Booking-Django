from django.contrib import admin
from .models import *
# Register your models here.


class Itinerary(admin.StackedInline):
    model = Itinerary
    extra = 1


class FooterUseFulInfo(admin.StackedInline):
    model = FooterUseFulInfo
    extra = 1


class Gallery(admin.StackedInline):
    model = Gallery
    extra = 1


class AwardImage(admin.StackedInline):
    model = AwardImages
    extra = 1


class Faq(admin.StackedInline):
    model = Faq
    extra = 1


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('heading', 'sub_heading', 'updated_at')


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('heading',)

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(WhyUs)
class WhyUsAdmin(admin.ModelAdmin):
    list_display = ('heading',)


@admin.register(OurStory)
class OurStoryAdmin(admin.ModelAdmin):
    list_display = ('heading',)
    inlines = (AwardImage,)

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['name', ]
    }
    list_display = ('name', 'ordering', 'created_at', 'updated_at')


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
    inlines = (FooterUseFulInfo,)


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
    inlines = (Itinerary, Faq, Gallery)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    prepopulated_fields = {
        'slug': ['title', ]
    }


@admin.register(TeamCategory)
class TeamCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
