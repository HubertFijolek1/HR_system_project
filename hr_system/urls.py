from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/recruitment/', include('recruitment.urls')),
    path('api/time_tracking/', include('time_tracking.urls'))
]
