from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page route
    path('categories/<slug:category_slug>', views.home, name='category_wise_post'),  # Category detail route
    path('author/', include('author.urls')),  # Include the author app's urls
    path('post/', include('post.urls')),  # Include the post app's urls
    path('categories/', include('categories.urls')),  # Include the categories app's urls
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
