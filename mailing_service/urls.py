from django.urls import path
from . import views  # Убедитесь, что этот импорт есть
from .views import index #или так

app_name = 'mailing_service'

urlpatterns = [
    path('', views.index, name='index'),
]