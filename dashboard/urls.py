from django.conf.urls import url
from dashboard.views import *

urlpatterns = [

    # /dashboard/
    url(r'^$', Dashboard.as_view(), name='dashboard'),

    # /dashboard/add_word/
    url(r'^add_word/$', Add_word.as_view(), name='add_word'),

    # /dashboard/add_word/add
    url(r'^(?P<pk>[0-9]+)/$', DictionaryList.as_view(), name='dict_list'),

    # /dashboard/dictionary/
    url(r'^dict/add$', Dictionary.as_view(), name='dictionary')
]
