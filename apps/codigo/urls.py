from django.urls import path,include
from apps.codigo.views import index

urlpatterns = [
    path('index/',index,name='index_codigo'),
]