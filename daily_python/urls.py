"""daily_python URL Configuration
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('pythonTips/', include('pythonTips.urls')),
    path('admin/', admin.site.urls),
]
