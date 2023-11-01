from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('/postlist/',include('postlist.urls')),
    path('/recommand/',include('recommand.urls')),
    path('/rank/',include('rank.urls')),
    path('/login/', include('login.urls')),
    path('/singin/',include('signin.urls')),
]
