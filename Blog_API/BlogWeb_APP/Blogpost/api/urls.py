from django.contrib import admin
from django.urls import path,include
from Blogpost.api.views import BlogList,BloglistAV,BlogdetailAV,CommentCreate,CommentList,CommentDetail

urlpatterns = [
    path('list-all/',BlogList.as_view(),name="Blog-list"),
    path('list/',BloglistAV.as_view(),name="post_list"),
    path("<int:pk>/",BlogdetailAV.as_view(),name="post_detail"),
    path("<int:pk>/comment-create/",CommentCreate.as_view(),name="comment-create"),
    path("<int:pk>/comment-list/",CommentList.as_view(),name="comment-list"),
    path("comment/<int:pk>/",CommentDetail.as_view(),name="comment-detail"),
]
