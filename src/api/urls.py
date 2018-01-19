from django.urls import include, path

from src.api.views import SchemaView


urlpatterns = [
    path('api/', SchemaView.as_view()),
    path('', include('src.api.v1.urls')),
]
