from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [
    path('', include('src.api.v1.core.urls')),
    path('', include('src.api.v1.meta.urls')),
    path('', include('src.api.v1.auth.urls')),
    path('', include('src.api.v1.transactions.urls')),
]
