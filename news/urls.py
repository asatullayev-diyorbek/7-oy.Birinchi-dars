from django.urls import  path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('category/', views.CategoryView.as_view(), name='category'),
    path('latest-news/<slug:slug>/', views.LatestNewsView.as_view(), name='latest_news'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog-details/', views.BlogDetailsView.as_view(), name='blog_details'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
