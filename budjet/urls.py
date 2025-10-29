from django.urls import path
from . import views

urlpatterns = [
    path("status/", views.status),
    path("add/", views.add),
    path("balance/", views.get_balance),
]
