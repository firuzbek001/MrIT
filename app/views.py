from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Item
# from .models import Book

def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

def detail_page(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'detail-page.html', {'item': item})

def my_view(request):
  context = {
  #   'title': 'Salom, Dunyo!',
  #   'content': 'Bu mening birinchi Django sahifam.'
  }
  return render(request, 'index.html', context)


def about_view(request):
    context = {

    }
    return render(request, 'about.html', context)


def detail_page(request):
    context = {

    }
    return render(request, 'detail-page.html', context)

def listing_page(request):
    context = {

    }
    return render(request, 'listing-page.html', context)

class HomeView(TemplateView):
    model = Item
    template_name = 'home.html'

class ItemLogin(LoginView):
    model = Item
    template_name = 'login.html'

class ItemLogout(LogoutView):
    model = Item
    template_name = 'logout.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'

class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'item_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('item_detail')

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item_confirm_delete.html'
    success_url = reverse_lazy('login')

# class SearchForm(forms.Form):
#     query = forms.CharField(label='Search', max_length=100)


# def search_view(request):
#     form = SearchForm()
#     results = []
#
#     if 'query' in request.GET:
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             results = Book.objects.filter(title__icontains=query)
#
#     return render(request, 'search.html', {'form': form, 'results': results})
