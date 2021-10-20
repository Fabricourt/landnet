from django.urls import path
from . import views
from django.urls import path
from . import views
from .views import (
	UserListingListView,
    #ListingDetailView,
    ListingCreateView,
    ListingUpdateView,
    ListingDeleteView

)


urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    #path('<slug:slug>/', ListingDetailView.as_view(), name='listing_detail')
    path('user/<str:username>', UserListingListView.as_view(), name='user-listings'),
    path('newlisting/', ListingCreateView.as_view(), name='create-new-listing'),
    path('listing/<int:pk>/update/', ListingUpdateView.as_view(), name='listing-update'),
    path('listing/<int:pk>/delete/', ListingDeleteView.as_view(), name='listing-delete'),
    path('search', views.search, name='search')
]
