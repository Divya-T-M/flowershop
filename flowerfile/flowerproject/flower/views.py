from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from . models import District, Seller, Customer
from .forms import AddAddressForm
# Create your views here.
def home(request):
    return render(request, "index.html")





def address_create_view(request):
    form = AddAddressForm()
    if request.method == 'POST':
        form = AddAddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('address_add')
    return render(request, 'book.html', {'form': form})

def address_update_view(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = AddAddressForm(instance=customer)
    if request.method == 'POST':
        form = AddAddressForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('address_change', pk=pk)
    return render(request, 'book.html', {'form': form})

# AJAX
def load_sellers(request):
    district_id = request.GET.get('place_id')
    sellers = Seller.objects.filter(district_id=district_id).all()
    return render(request, 'add.html', {'seller': sellers})



