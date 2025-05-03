from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('signup',views.signup),
]

  # Using Reg_tbl instead of index

