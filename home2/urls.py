from django.urls import path
from home2.views import Home2

app_name ='Home2'

urlpatterns = [
    path('Home2', Home2.as_view(), name='Home2'),
]