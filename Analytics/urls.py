from django.conf.urls import patterns, url

from Analytics import views

urlpatterns = patterns('',
#    url('^$', views.redirect_to_dashboard),
    url('^addrequest/', views.addrequest),
    url('^dashboard/$', views.initial_dashboard),
#    url('^reports?', views.reports),
#    url('^reportsG', views.reports),
    url('^giveUserID', views.giveUserID),
    url('^register/$', views.register),
    url('^login/$', views.MerchantLogin),
    url('^logout/$', views.MerchantLogout),
    url('^follow/', views.follow),
    url('^filter/', views.filters_dashboard),
    )