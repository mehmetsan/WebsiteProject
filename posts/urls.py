from django.contrib import admin
from django.urls import path, include

from .views import  create_post_view, single_post_view, display_all_posts, posts_by_date_view, posts_by_search_view

urlpatterns = [
    path('create', create_post_view, name='create-article'),
    path('display/<str:post_type>/all', display_all_posts, name='display-all'),
    path('search/<str:post_type>', posts_by_search_view ),
    path('display/<str:post_type>/<str:slug>', single_post_view, name='display-new'),
    path('display/date/<str:post_type>/<str:date>', posts_by_date_view ),
]
