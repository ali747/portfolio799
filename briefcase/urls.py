from nturl2path import url2pathname
from django.urls import path, include
from briefcase import views
from . import views
from .views import about1
from django.conf import settings
from django.conf.urls.static import static

app_name = "briefcase"

urlpatterns = [
    path('', views.employeeinfo, name='index'),
    # path('index.html', views.employeeinfo, name='briefcase'),
    path('about', views.about, name='about'),
    path('about1', views.about1, name='about1'),
    path('resume', views.resume, name='resume'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),

]
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
