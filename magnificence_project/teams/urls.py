from django.urls import path
from .views import MagnificentSevenView

urlpatterns = [
    path('magnificent-seven/', MagnificentSevenView.as_view(), name='magnificent-seven'),
]
