from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Item, TranslatedItem


def translate(request):
    translate = TranslatedItem.objects.all()
    return render(request, 'index.html', {'translate': translate})


def home(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})

def detail_page(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'detail-page.html', {'item': item})

def my_view(request):
  return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')


def detail_page(request):
    return render(request, 'detail-page.html')

def listing_page(request):
    return render(request, 'listing-page.html')

def contact_view(request):
    context = {

    }
    return render(request, 'contact.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

class HomeView(TemplateView):
    model = Item
    template_name = 'home.html'

class ItemLogin(LoginView):
    context_object_name = 'login'
    model = Item
    template_name = 'registration/login.html'

class ItemLogout(LogoutView):
    context_object_name = 'logout'
    model = Item
    template_name = 'html/logout.html'

class ItemDetailView(DetailView):
    context_object_name = 'item'
    model = Item
    template_name = 'item_detail.html'

class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'html/item_update.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('item_detail')

class ItemDeleteView(DeleteView):
    template_name = 'item_confirm_delete.html'
    success_url = reverse_lazy('login')
