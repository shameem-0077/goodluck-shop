from django.http import HttpResponse
from django.shortcuts import render
from .models import LandingPage, WhatWeDealWith, FeaturedBrand

# Create your views here.

def index(request):
    landing_page_datas = LandingPage.objects.all()
    what_we_deal_datas = WhatWeDealWith.objects.all()
    brands = FeaturedBrand.objects.all()

    context = {
        "title": "Good Luck",
        "landing_page_datas": landing_page_datas,
        "what_we_deal_datas": what_we_deal_datas,
        "brands": brands
    }
    
    return render(request, "web/index.html", context=context)