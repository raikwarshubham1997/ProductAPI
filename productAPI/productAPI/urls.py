from django.contrib import admin
from django.urls import path
from api import views
from django.conf import settings  
from django.conf.urls.static import static

app_name = "api"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productapi/', views.ProductAPI.as_view()),
    path('productapi/<int:pk>/', views.ProductAPI.as_view()),
    path('categoryapi/', views.CategoryAPI.as_view()),
    path('categoryapi/<int:pk>/', views.CategoryAPI.as_view()),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 