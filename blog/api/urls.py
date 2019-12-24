from django.urls import path,include
from django.conf.urls import url
from .views import (
    PostDetailAPIView,
    PostListAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
    PostCreateAPIView
)
from . import views

urlpatterns = [
    # path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    # path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    # path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    # path('tinymce/', include('tinymce.urls')),
    path('', PostListAPIView.as_view(), name='list'),
    url(r'^create/$', PostCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\w-]+)/update/$', PostUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),
    # path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('post/new/', PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # path('about/', views.about, name='blog-about'),
]