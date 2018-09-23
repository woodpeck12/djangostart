from django.urls import path

from .views import (
    post_list_view,
    post_detail_view
)

urlpatterns = [
    path('',post_list_view,name='post_list'),
    path('post/<int:id>',post_detail_view,name='post_detail'),

]


