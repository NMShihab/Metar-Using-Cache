from django.urls import path
from .views import ping,latestData


urlpatterns =[
    path("ping/",ping,name="ping"),
    path("info/",latestData,name='latest-data'),
    
]