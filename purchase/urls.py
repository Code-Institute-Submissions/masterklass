from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.plans, name='plans'),
    path('purchase/<id>', views.purchasePlan, name='purchase_plan'),
    path('signup/', views.signup, name='signup'),
]
