from django.urls import path
from .views import ItemDetailView, ItemUpdateView, ItemDeleteView, ItemLogin, ItemLogout
from .views import my_view, detail_page, listing_page, about_view, home
# from .views import search_view

urlpatterns = [
    path('', my_view, name='home'),
    path('about/', about_view, name='about'),
    path('detail-page/', detail_page, name='detail-page'),
    path('home/', home, name='home'),
    path('listing-page/', listing_page, name='listing-page'),
    path('login/', ItemLogin.as_view(), name='login'),
    path('logout/', ItemLogout.as_view(), name='logout'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('item/<int:pk>/edit/', ItemUpdateView.as_view(), name='item_edit'),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
    # path('search/', search_view, name='search'),
]