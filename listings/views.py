from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from PIL import Image
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from hitcount.views import HitCountDetailView
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin
from django.views.generic import ListView
from.models import Listing



def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)
  footers = Listing.objects.order_by('?').filter(is_published=True)[:22]


  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings,
    'footers': footers,
    'county_choices': county_choices,
    'plot_size_choices': plot_size_choices,
    'plot_type_choices': plot_type_choices,
    'house_type_choices': house_type_choices,
    'price_choices': price_choices,
    'town_choices': town_choices,
    'bedroom_choices': bedroom_choices,
    'for_rs_choices': for_rs_choices,
  }

  return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)
  footers = Listing.objects.order_by('?').filter(is_published=True)[:2]
  single = Listing.objects.order_by('?').filter(is_published=True)[:1]
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

  context = {}

  # hitcount logic
  hit_count = get_hitcount_model().objects.get_for_object(listing)
  hits = hit_count.hits
  hitcontext = context['hitcount'] = {'pk': hit_count.pk}
  hit_count_response = HitCountMixin.hit_count(request, hit_count)
  if hit_count_response.hit_counted:
      hits = hits + 1
      hitcontext['hit_counted'] = hit_count_response.hit_counted
      hitcontext['hit_message'] = hit_count_response.hit_message
      hitcontext['total_hits'] = hits


  context = {
    'listings': listings,
    'listing': listing,
    'footers': footers,
    'single': single,
    'county_choices': county_choices,
    'plot_size_choices': plot_size_choices,
    'plot_type_choices': plot_type_choices,
    'house_type_choices': house_type_choices,
    'price_choices': price_choices,
    'town_choices': town_choices,
    'bedroom_choices': bedroom_choices,
    'for_rs_choices': for_rs_choices,
  }

  return render(request, 'listings/listing.html', context)




class UserListingListView(ListView):
    model = Listing
    template_name = 'listings/user_listings.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'listings'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Listing.objects.filter(realtor.user==user).order_by('-joined')


class ListingCreateView(LoginRequiredMixin, CreateView):
    model = Listing
    success_url = 'listing'
    success_message = "%(name)s created successfully"
    template_name = 'listings/listing_form.html'
    context_object_name = 'listing'
    fields = ['realtor', 'title', 'slug', 'neighbourhood', 'town', 'county', 'description',  'features', 'price', 'house_type', 'for_rs', 'plot_type', 'soil_type', 'plot_size', 'document_type', 'large_plot_size', 'bedrooms', 'garage', 'sqft',  'photo_main', 'photo_1','photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6', 'map_link', 'is_published', 'list-date', 'sold', 'rental', 'house', 'mvp', 'plot',  ]

    def form_valid(self, form):
        form.instance.realtor = self.request.realtor.user
        return super().form_valid(form)


class ListingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Listing
    success_url = 'listing'
    success_message = "%(name)s Updated  successfully"
    template_name = 'listings/listing_form.html'
    fields = ['realtor', 'title', 'slug', 'neighbourhood', 'town', 'county', 'description',  'features', 'price', 'house_type', 'for_rs', 'plot_type', 'soil_type', 'plot_size', 'document_type', 'large_plot_size', 'bedrooms', 'garage', 'sqft',  'photo_main', 'photo_1','photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6', 'map_link', 'is_published', 'list-date', 'sold', 'rental', 'house', 'mvp', 'plot',  ]


    def form_valid(self, form):
        form.instance.realtor.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        listing = self.get_object()
        if self.request.realtor.user == listing.realtor.user:
            return True
        return False


class ListingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Listing
    success_url = 'listings'
    success_message = "Listing Deleted successfully"
    def test_func(self):
        listing = self.get_object()
        if self.request.user == listing.realtor.user:
            return True
        return False



@login_required
def add_to_wishlist(request, Listing_id):
    listing = get_object_or_404(Listing, pk=Listing_id)
    wished_item,created = Wishlist.objects.get_or_create(wished_item=listing,
    slug = listing.slug,
    user = request.user,
    )
    messages.info(request,'The listing was added to your wishlist')
    return redirect('listings')




def search(request):
  queryset_list = Listing.objects.order_by('-list_date')
  footers = Listing.objects.order_by('?').filter(is_published=True)[:2]


  #keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)


  # town
  if 'town' in request.GET:
    town = request.GET['town']
    if town:
      queryset_list = queryset_list.filter(town__iexact=town)

  # county
  if 'county' in request.GET:
    county = request.GET['county']
    if county:
      queryset_list = queryset_list.filter(county__iexact=county)

  # for_rs
  if 'for_rs' in request.GET:
    for_rs = request.GET['for_rs']
    if for_rs:
      queryset_list = queryset_list.filter(for_rs__iexact=for_rs)

   # for_rs
  if 'plot_type' in request.GET:
    plot_type = request.GET['plot_type']
    if plot_type:
      queryset_list = queryset_list.filter(plot_type__lte=plot_type)

   # for_rs
  if 'house_type' in request.GET:
    house_type = request.GET['house_type']
    if house_type:
      queryset_list = queryset_list.filter(house_type__lte=house_type)

  # plot_size
  if 'plot_size' in request.GET:
    plot_size = request.GET['plot_size']
    if plot_size:
      queryset_list = queryset_list.filter(plot_size__lte=plot_size)

  # price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
        'county_choices': county_choices,
        'plot_size_choices': plot_size_choices,
        'plot_type_choices': plot_type_choices,
        'house_type_choices': house_type_choices,
        'for_rs_choices': for_rs_choices,
        'town_choices': town_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET,
        'footers': footers
  }

  return  render(request, 'listings/search.html', context)
