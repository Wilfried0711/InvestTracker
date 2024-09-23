from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:portfolio_id>/', views.add_investment, name='add_investment'),
]
