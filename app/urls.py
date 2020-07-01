from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from api import views

schema_view = get_schema_view(
    openapi.Info(
        title="Notelog API",
        default_version='v1',
        description="API for topics and entry manage."
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'entries', views.EntryViewSet)
router.register(r'topics', views.TopicViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    url(r'^swagger/$',
        schema_view.with_ui(
            'swagger',
            cache_timeout=0
        ),
        name='schema-swagger-ui'
        ),
]
