from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^$','appWeb.views.index'),
	url(r'^admin/', include(admin.site.urls)),

    url(r'^altaproductor/', 'appWeb.views.altaproductor'),
    url(r'^bajaproductor/', 'appWeb.views.bajaproductor'),
    url(r'^modificarproductor/', 'appWeb.views.modificarproductor'),
    url(r'^altalote/', 'appWeb.views.altalote'),
    url(r'^bajalote/', 'appWeb.views.bajalote'),
    url(r'^modificarlote/', 'appWeb.views.modificarlote'),

)
