from django.contrib import admin
from django.urls import path,include
from .views import home_page
urlpatterns = [
    path('home/', home_page),
    path('admin/', admin.site.urls),
    path("api/v1/",include('api.urls'))
]
