from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/recruitment/', include('recruitment.urls')),
    path('api/time_tracking/', include('time_tracking.urls')),
    path('api/evaluations/', include('evaluations.urls')),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
