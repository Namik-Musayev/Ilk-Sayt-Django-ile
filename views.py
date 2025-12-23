from django.shortcuts import render,get_object_or_404 ,redirect
from django.http import HttpResponse
from namik import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

social_links = models.SocialLink.objects.all()

footer_links = models.FooterLink.objects.all()

buttons = models.Button.objects.all()

cart_items = models.CartItem.objects.all()

nav_items = models.Navigation.objects.all()

def inde(request):
    images = models.SliderImage.objects.all()
    return render(request, "namik/inde.html", {
        'images': images, 
        'nav_items': nav_items,
        'cart_items': cart_items,
        'buttons': buttons,
        'social_links': social_links,
        'footer_links': footer_links
        })

def about(request):
    sections = models.AboutSection.objects.all()
    return render(request, "namik/about.html",  {
        'sections': sections,
        'nav_items': nav_items,
        'cart_items': cart_items,
        'buttons': buttons,
        'social_links': social_links,
        'footer_links': footer_links
        })


def blogs(request):
    posts = models.Blog.objects.all()
    return render(request, 'namik/blogs.html',  {
        'posts': posts,
        'nav_items': nav_items,
        'cart_items': cart_items,
        'buttons': buttons,
        'social_links': social_links,
        'footer_links': footer_links
        })

def contact(request):
    if request.method == "POST":
        Adi = request.POST["Adi"]
        sifre = request.POST["sifre"]
        user = authenticate(request, username=Adi, password=sifre)
        if user is not None:
            login(request, user)
            return redirect('inde')
        else:
            return render(request, 'namik/contact.html', {'error': 'Kod sehdvdi'})
    return render(request, "namik/contact.html", {
        'nav_items': nav_items,
        'cart_items': cart_items,
        'buttons': buttons,
        'social_links': social_links,
        'footer_links': footer_links
    })

def menu(request):
    menu_items = models.MenuItem.objects.all()
    return render(request, 'namik/menu.html',  {
        'menu_items': menu_items, 
        'nav_items': nav_items,
        'cart_items': cart_items,
        'buttons': buttons,
        'social_links': social_links,
        'footer_links': footer_links
        })

def products(request):
    products = models.Product.objects.all()
    return render(request, 'namik/products.html',  {
        'products': products, 
        'nav_items': nav_items,
        'buttons': buttons,
        'cart_items': cart_items,
        'social_links': social_links,
        'footer_links': footer_links
        })

def register(request):
    if request.user.is_authenticated:
        return redirect('inde')
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, 'namik/register.html', {'error': 'Bu istifadechi adi artiq movcuddur',"username":username,"email":email,"firstname":firstname,"lastname":lastname})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, 'namik/register.html', {'error': 'Bu email artiq movcuddur',"username":username,"email":email,"firstname":firstname,"lastname":lastname})
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
                    user.save()
                    return redirect('contact')
        else:
            return render(request, 'namik/register.html', {'error': 'Parollar eyni deyil',"username":username,"email":email,"firstname":firstname,"lastname":lastname})
    return render(request, 'namik/register.html')
