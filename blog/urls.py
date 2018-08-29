from django.urls import path
from .views import BlogListView, BlogDetailView


# `pk` or `id` is an auto-incrementing primary key for Django database models
# kept under the key `id`
urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]