from django.urls import path
from . import views   
urlpatterns = [
    path('',views.recommand, name='recommand'),
] 