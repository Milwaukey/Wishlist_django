from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_wishlist.urls')),
    path('accounts/', include('api_account.urls')),
    path('', include('wishlist_app.urls')),


    path('api-auth/', include('rest_framework.urls')),
]
