from.import views
from django.urls import path

app_name = 'flower'
urlpatterns = [
    path('', views.home, name='home'),

    path('add/', views.address_create_view, name='address_add'),
    path('<int:pk>/', views.address_update_view, name='address_change'),
    path('ajax/load-sellers/', views.load_sellers, name='ajax_load_sellers'),

]

