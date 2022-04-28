from django.urls import path
from . import views
urlpatterns= [
    path('contact/',views.contact,name='hair-contact'),
    path('about/',views.about,name='hair-about'),
    path('',views.home,name='hair-home'),
    path('price/',views.price,name='hair-price'),
    path('services',views.services,name='hair-services'),
]