from django.contrib import admin
from django.urls import path, include
from .views import home_view, team_view, contact_view, about_view, overview_view, search_panel_view, pdf_download, quality_view, services_view, privacy_view

# FOR PROFILE PHOTO
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),

    path('posts/', include("posts.urls")),
    path('team/', team_view),
    path('contact/', contact_view),
    path('about/', about_view),
    path('overview/', overview_view),

    path('search/', search_panel_view),
    path('quality-assurance/', quality_view),
    path('services/<str:servicename>/', services_view),

    path('privacy', privacy_view),
    path('pdf/<str:filename>/', pdf_download)
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
