from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .forms import *
from listings.models import Listing
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from hitcount.views import HitCountDetailView
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin
from contacts.models import *


def register(request):
    footers = Listing.objects.order_by('?').filter(is_published=True)[:2]

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
        'footers': footers,
        }

    return render(request, 'accounts/register.html', context)


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      if request.user.is_staff or request.user.is_superuser: 
        return redirect('dashboard')
      else:
        return redirect('index')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')


@login_required
def profile(request):
    footers = Listing.objects.order_by('?').filter(is_published=True)[:2]
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'footers': footers,
    }

    return render(request, 'accounts/profile.html', context)


def dashboard(request):
    listing_hits = Listing.objects.order_by('-hit_count_generic__hits')
    footers = Listing.objects.order_by('?').filter(is_published=True)[:2]
    contacts = Contact.objects.order_by('-contact_date')
    contactus = Contactus.objects.order_by('-timestamp')
   

    context = {
        'listing_hits' : listing_hits,
        'footers': footers,
        'contacts': contacts,
        'contactus': contactus,
    }

    return render(request, 'accounts/dashboard.html', context)