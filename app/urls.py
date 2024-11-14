from django.urls import path
from .views import ItemDetailView, ItemUpdateView, ItemDeleteView, ItemLogin, ItemLogout
from .views import my_view, detail_page, listing_page, about_view, home, contact_view, register

urlpatterns = [
    path('index/', my_view, name='home'),
    path('about/', about_view, name='about'),
    path('home/', home, name='index'),
    path('contact/', contact_view, name='contact'),
    path('', register, name='register'),
    path('detail-page/', detail_page, name='detail-page'),
    path('listing-page/', listing_page, name='listing-page'),
    path('login/', ItemLogin.as_view(), name='login'),
    path('logout/', ItemLogout.as_view(), name='logout'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('item/<int:pk>/edit/', ItemUpdateView.as_view(), name='item-edit'),
    path('item-delete/<int:pk>/', ItemDeleteView.as_view(), name='item-delete'),
]