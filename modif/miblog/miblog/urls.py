
from django.contrib import admin
from django.urls import path
from core import views
from valorant import views as porta_views
from valorant.views import formu
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('agentes/',porta_views.valorant,name='agentes'),
    path('tienda/',views.tienda,name='tienda'),
    path('skins/',views.skins,name='skins'),
    path('formu/',formu,name='formu'),
    
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)

