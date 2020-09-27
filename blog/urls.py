from django.urls import path,include
from . import views

# urlpatterns = [
#     path('', views.post_list, name='post_list'),
#     path('post/<int:pk>/', views.post_detail, name='post_detail'),
#     path('post/new/', views.post_new, name='post_new'),
#     path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
# #     path('api/post/', views.PostListCreate.as_view() ),
# ]

from django.views.generic import TemplateView
from .views import ContactFormView

urlpatterns = [
    # path('home/', HomeView.as_view(), name='home_url'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('', TemplateView.as_view(template_name='blog/index.html'), name='index_url'),
    path('about/', TemplateView.as_view(template_name='blog/about.html'), name='about_url'),
    path('contact/', ContactFormView.as_view(), name='contact_url'),
    path('contact/success/', TemplateView.as_view(template_name='blog/contact_success.html'), name='contact_success_url'),
    # path('post/', TemplateView.as_view(template_name='blog/post.html'), name='post_url'),
]