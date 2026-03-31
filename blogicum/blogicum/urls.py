from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import register
from django.views.generic import RedirectView

handler403 = 'pages.views.csrf_failure'
handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registration/', register, name='registration'),
    path('', include('blog.urls', namespace='blog')),
    path('', include('pages.urls', namespace='pages')),
    path('accounts/profile/', RedirectView.as_view(url='/'),
         name='profile_redirect'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
