from django.urls import path
from .views import RegisterView

urlpatterns = [
     path('a',RegisterView.as_view())
]
