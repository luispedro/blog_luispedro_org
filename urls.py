import settings
from django.conf.urls import patterns, include
from django.contrib import admin
import gitcms.pages.urls
import gitcms.files.urls
import gitcms.blog.urls
admin.autodiscover()

urlpatterns = patterns('',
    (r'^static/(?P<path>.+)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^admin/', include(admin.site.urls)),
    (r'^pages/', include(gitcms.pages.urls)),
)
urlpatterns += gitcms.files.urls.urlpatterns
urlpatterns += gitcms.blog.urls.urlpatterns
