from django.conf.urls import url
from dashboard.views import *

app_name = 'dashboard'

urlpatterns = [

    # /dashboard/
    url(r'^$', Dashboard.as_view(), name='dashboard'),

    # /dashboard/add_word/
    url(r'^add_word/$', Add_word.as_view(), name='add_word'),

    # /dashboard/add_word/add
    url(r'^(?P<pk>[0-9]+)/$', DictionaryDetail.as_view(), name='dict'),

    # /dashboard/add/
    url(r'dict/add/$', DictionaryCreate.as_view(), name='dict_add'),

    # /dashboard/2/update/
    url(r'dict/(?P<pk>[0-9]+)/$', DictionaryUpdate.as_view(), name='dict_update'),

    # /dashboard/2/delete/
    url(r'dict/(?P<pk>[0-9]+)/delete/$', DictionaryDelete.as_view(), name='dict_del')
]
