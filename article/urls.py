from django.conf.urls import patterns, include, url
from views import *

urlpatterns=patterns('',

	url(r'article/(\d{4})/$',article),
	url(r'article/$',article1),
	url(r'article/(?P<article_id>\d+)/$',article1),
	url(r'tests/$',test),
	url(r'search/$',search),

	)