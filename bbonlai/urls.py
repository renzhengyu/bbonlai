from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('ppco2/', include('ppco2.urls')),
    # path('admin/', admin.site.urls),
]
