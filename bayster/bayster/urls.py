from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('land.urls')),
    #ログイン追加
    path('accounts/', include('django.contrib.auth.urls')),
]