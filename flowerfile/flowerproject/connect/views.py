from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.shortcuts import render, get_object_or_404
from . models import Category, Product

# Create your views here.
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
def register(request):
    if request.method == 'POST':
        v1 = request.POST['username']
        v4 = request.POST['email']
        v5 = request.POST['password']
        v6 = request.POST['password1']
        if v5 == v6:
            if User.objects.filter(username=v1).exists():
                messages.info(request, "Username already Taken")
                return redirect('register')
            elif User.objects.filter(email=v4).exists():
                messages.info(request, "Email ID already Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=v1, password=v5, email=v4)
                user.save()
                print("Uer Created")
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        v1 = request.POST['username']
        v5 = request.POST['password']
        user = auth.authenticate(username=v1, password=v5)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "User name and password is incorrect")
            return redirect('login')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def allProdCat(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug!=None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.all().filter(category=c_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    paginator = Paginator(products_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'category': c_page, 'products': products})


def proDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'category.html', {'product': product})
