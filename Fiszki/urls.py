from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Fiszki.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', RedirectView.as_view(url='dashboard/', permanent=False)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/', include('dashboard.urls'))
]
