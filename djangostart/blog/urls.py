from django.urls import path

from .views import (
    post_list_view,
    post_detail_view,
    post_new_view,
    post_edit_view
)

urlpatterns = [
    path('',post_list_view,name='post_list'),
    path('post/<int:id>',post_detail_view,name='post_detail'),
    path('post/new',post_new_view,name='post_new'),
    path('post/<int:id>/edit', post_edit_view, name='post_edit')

]


