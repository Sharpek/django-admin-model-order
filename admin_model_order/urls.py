from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('admin_model_order.views',
    url(r'^change/(?P<model_pk>\d+)/(?P<model_type_id>\d+)/', 'change_order', name='url-admin-model-order'),
)
