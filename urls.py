import settings
from django.conf.urls.defaults import *
from django.contrib import admin
import gitcms.pages.urls
import gitcms.files.urls
import gitcms.blog.urls
admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/(?P<path>.+)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^admin/', include(admin.site.urls)),
)
urlpatterns += gitcms.files.urls.urlpatterns
urlpatterns += gitcms.blog.urls.urlpatterns
urlpatterns += gitcms.pages.urls.urlpatterns
