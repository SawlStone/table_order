from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/table_order/', include(('api.urls', 'api'))),

    # redirect to admin due to no main page
    path('', RedirectView.as_view(url='admin'))
]
