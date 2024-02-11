from django.urls import path
from django.views.generic import TemplateView

from . import views



urlpatterns = [
    path('shop/', views.home_shop, name='shop'),
    path("shop/", TemplateView.as_view(template_name="home_shop.html"), name="shop"),

]
