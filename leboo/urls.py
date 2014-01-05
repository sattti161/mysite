from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('leboo.views',
    url(r'^$', 'index'),
    url(r'^contact', 'contact'),
    url(r'^lentitem', 'lentitem'),
    url(r'^borroweditem', 'borroweditem'),
    url(r'^search', 'search'),
    url(r'^datesearch', 'datesearch'),
    url(r'^alternative', 'alternative'),
)