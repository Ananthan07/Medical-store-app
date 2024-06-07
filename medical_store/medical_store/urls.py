from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medicines.urls')),  # Include urls from the 'medical_store_app' app
]
