from django.contrib import admin
from django.urls import reverse_lazy
from django.urls import path,include
from .import settings
from django.conf.urls.static import  static
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('machines/',include('machine.urls')),
    path('',RedirectView.as_view(url=reverse_lazy('machine:machine_list')),name="index"),

]


if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)