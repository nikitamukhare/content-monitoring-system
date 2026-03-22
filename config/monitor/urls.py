from django.urls import path
from .views import create_keyword, create_content, scan_content, update_flag, get_flags

urlpatterns = [
    path('keywords/', create_keyword),
    path('content/', create_content),
    path('scan/', scan_content),
    path('flags/', get_flags),
    path('flags/<int:id>/', update_flag),
]