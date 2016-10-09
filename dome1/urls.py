from django.conf.urls import patterns, include, url
from dome_app import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dome1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register',views.register,name='register'),
    url(r'^login',views.login,name='login'),
    url(r'^index',views.index,name='index'),
    url(r'^logout',views.logout,name='logit'),
)
