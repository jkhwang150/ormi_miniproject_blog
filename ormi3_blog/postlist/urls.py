from django.urls import path
from . import views

urlpatterns = [
    path('', views.postlist, name='postlist'),
    path('post', views.post, name='post'),
    path('post/<int:pk>', views.postdetail, name='postdetail'),
    path('post/delete/<int:pk>', views.delete, name='delete'),
    path('post/edit/<int:pk>', views.edit, name='edit'),
    path('post/update/<int:pk>', views.update, name='update'),
    path('post/comment/<int:pk>', views.comment, name='comment')
]