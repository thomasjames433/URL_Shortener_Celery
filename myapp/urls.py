from django.urls import path
from .views import *

urlpatterns=[
    path('shorten',ShortenURL.as_view(),name="shortenurl"),
    path('redirect/:<shortUrl>',RedirectUrl.as_view(),name="redirecturl"),
    path('details/:', UrlDetails.as_view(), name='url-details'),  # Note: 'details/' now expects a query parameter
    path('top/:<int:number>',totalurl.as_view(),name="totalurls"),
]