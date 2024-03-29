from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('web_app.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/messages/', include('chat.urls')),
    path('api/v1/tax/', include('tax.urls')),
    path('api/v1/words/', include('words.urls')),
]
