from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import *
from django.shortcuts import get_object_or_404
from listings.models import Listing
from realtors.models import Realtor
from  .models import *


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:24]
    footers = Listing.objects.order_by('?').filter(is_published=True)[:22]
    home_about = Page.objects.order_by('-updated').filter(published=True).filter(home=True).filter(about=True)[:1]
    service = Page.objects.order_by('updated').filter(published=True).filter(service=True)[:3]
    home_service = Page.objects.order_by('updated').filter(published=True).filter(home=True).filter(service=True)[:3]
    mvp_faq = Page.objects.order_by('created').filter(published=True).filter(mvp=True).filter(faq=True)[:5]

    context = {
        'home_about': home_about,
        'home_service': home_service,
        'service': service,
        'mvp_faq':mvp_faq,
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
    about_service = Page.objects.order_by('created').filter(published=True).filter(about=True).filter(service=True)[:4]
    about = Page.objects.order_by('?').filter(published=True).filter(about=True)[:3]
    mvp_about = Page.objects.order_by('-updated').filter(published=True).filter(about=True).filter(mvp=True)[:1]
    realtors = Realtor.objects.order_by('-hire_date')
    footers = Listing.objects.order_by('?').filter(is_published=True)[:2]

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'mvp_about': mvp_about,
        'about_service': about_service,
        'about': about,
        'footers': footers,
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)





def services(request):
    # Get all realtors
    service_mvp = Page.objects.order_by('updated').filter(published=True).filter(mvp=True).filter(service=True)[:1]
    services = Page.objects.order_by('?').filter(published=True).filter(service=True)[:8]
    servicex = Page.objects.order_by('created').filter(published=True).filter(service=True).filter(core=True)[:1]
    about_service = Page.objects.order_by('updated').filter(published=True).filter(about=True).filter(service=True)[:4]
    realtors = Realtor.objects.order_by('-hire_date')
    footers = Listing.objects.order_by('?').filter(is_published=True)[:2]
    home_service = Page.objects.order_by('updated').filter(published=True).filter(home=True).filter(service=True)[:3]

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'service_mvp': service_mvp,
        'services': services,
        'servicex': servicex,
        'about_service': about_service,
        'home_service': home_service,
        'footers': footers,
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/services.html', context)

def underconstruction(request):
    return render(request, 'pages/underconstruction.html')


def page(request, page_id):
  page = get_object_or_404(Page, pk=page_id)
  rentals = Listing.objects.order_by('?').filter(is_published=True).filter(rental=True)[:3]
  houses = Listing.objects.order_by('?').filter(is_published=True).filter(house=True)[:3]
  plots = Listing.objects.order_by('?').filter(is_published=True).filter(plot=True)[:3]
  services = Page.objects.order_by('?').filter(published=True).filter(service=True)[:4]


  context = {
    'services': services,
    'page': page,
    'rentals': rentals,
    'houses': houses,
    'plots': plots,
    'county_choices': county_choices,
    'plot_size_choices': plot_size_choices,
    'plot_type_choices': plot_type_choices,
    'house_type_choices': house_type_choices,
    'price_choices': price_choices,
    'town_choices': town_choices,
    'bedroom_choices': bedroom_choices,
    'for_rs_choices': for_rs_choices,
  }

  return render(request, 'pages/page.html', context)
