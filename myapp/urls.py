from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/new/', views.book_new, name='book_new'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('deteksi', views.detection_form, name='detection_form'),
    # path('deteksi/create', views.create_detection, name='create_detection'),
    path('riwayat', views.history, name='history'),
    path('detail-riwayat/<int:pk>/', views.detail_history, name='detail_history'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
