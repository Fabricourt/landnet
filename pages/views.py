from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import *

from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:24]
    footers = Listing.objects.order_by('?').filter(is_published=True)[:2]

    context = {
        'footers': footers,
        'listings': listings,
        'county_choices': county_choices,
        'plot_size_choices': plot_size_choices,
        'plot_type_choices': plot_type_choices,
        'house_type_choices': house_type_choices,
        'price_choices': price_choices,
        'town_choices': town_choices,
        'bedroom_choices': bedroom_choices,
        'for_rs_choices': for_rs_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    footers = Listing.objects.order_by('?').filter(is_published=True)[:2]

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'footers': footers,
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)


def services(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    footers = Listing.objects.order_by('?').filter(is_published=True)[:2]

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'footers': footers,
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/services.html', context)

def underconstruction(request):
    return render(request, 'pages/underconstruction.html')
