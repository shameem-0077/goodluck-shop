from django.contrib import admin
from .models import LandingPage, WhatWeDealWith, FeaturedBrand

# Register your models here.

class LandingPageAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "featured_image"]


admin.site.register(LandingPage, LandingPageAdmin)


class WhatWeDealWithAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "featured_image"]


admin.site.register(WhatWeDealWith, WhatWeDealWithAdmin)


class FeaturedBrandAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "featured_image"]


admin.site.register(FeaturedBrand, WhatWeDealWithAdmin)

