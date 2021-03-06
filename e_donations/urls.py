"""E-donations URL Configuration."""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


urlpatterns = i18n_patterns(
    path(route="i18n/", view=include("django.conf.urls.i18n")),
    path(f"{settings.ADMIN_URL}/", admin.site.urls),
    path(
        ".well-known/security.txt",
        TemplateView.as_view(template_name="security.txt", content_type="text/plain",),
    ),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain",),
    ),
    path("api/contact/", include("contact.urls")),
    path("api/donations/", include("donations.urls")),
    path("api/users/", include("users.urls")),
    prefix_default_language=False
)

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += [] + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
