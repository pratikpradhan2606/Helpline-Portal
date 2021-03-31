from django.contrib import admin
from django.urls import path
from Services.views import Emergency1, ClgCampus, home,MancharNos,AboutUs
urlpatterns = [
    path('' , home),
    path('Campus', Emergency1),
    path('ClgCampus', ClgCampus),
    path('MancharNos',MancharNos),
    path('about',AboutUs)
]
