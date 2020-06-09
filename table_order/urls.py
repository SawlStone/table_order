from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.views.generic import RedirectView

from table_order.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(('api.urls', 'api'))),

    # redirect to admin due to no main page
    path('', RedirectView.as_view(url='admin'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
