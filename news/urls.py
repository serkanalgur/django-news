from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "news"
urlpatterns = [
    path('', views.BlogIndexView.as_view(), name='newsindex'),
    path('<slug:cat_slug>/<slug:slug>/', views.DetailedView.as_view(), name='newsdetail'),
    path('<slug:cat_slug>/', views.CategoryListView.as_view(), name='catindex'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)