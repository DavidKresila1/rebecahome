from django.urls import path
from . import views
from store.views import ProductList, contact, productdetail

urlpatterns = [
    path("", views.homePage, name="home"),
    path("login", views.login, name="login"),
    path("test", views.test, name="test"),
    path("cart", views.get_cart, name="cart"),
    path("contact", views.contact, name="contact"),

]