from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        include(
            ("mailing_service.urls", "mailing_service"), namespace="mailing_service"
        ),
    ),
    path("", include(("users.urls", "users"), namespace="users")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
