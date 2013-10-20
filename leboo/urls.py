from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('leboo.views',
    url(r'^$', 'index'),
    url(r'^lentform', 'lentform'),
    url(r'^contact', 'contact'),
    url(r'^lentitem', 'lentitem'),
)