from django.urls import path

from prices import views

urlpatterns = [
    path('prices/', views.upload_prices)
]