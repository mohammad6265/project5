from django.shortcuts import render


def home_shop(request):
    return render(request, 'shop/home_shop.html')
