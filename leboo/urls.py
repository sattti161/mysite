from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('leboo.views',
    url(r'^$', 'index'),
    url(r'^contact', 'contact'),
    url(r'^lentitem', 'lentitem'),
    url(r'^borroweditem', 'borroweditem'),
    url(r'^search', 'search'),
    url(r'^datesearch', 'datesearch'),
    url(r'^alternative', 'alternative'),
    url(r'^intro', 'intro'),
    url(r'^login', 'login'),
    url(r'^register', 'register'),
    url(r'^alentitem', 'alentitem'),
    url(r'^aborroweditem', 'aborroweditem'),
)