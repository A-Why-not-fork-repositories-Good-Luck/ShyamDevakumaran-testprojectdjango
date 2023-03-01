from django.contrib import admin
from django.urls import include, path
from testapp  import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('', include('testapp.urls'))
    
]
