# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

from django.urls import path, include
from core.serializers import PassengerViewSet
from rest_framework import routers




# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'passengers', PassengerViewSet)


urlpatterns = [
    path(route='admin/', view=admin.site.urls),          # Django admin route
    path(route="", view=include("apps.authentication.urls")), # Auth routes - login / register
    path('__debug__/', include('debug_toolbar.urls')),

    # ADD NEW Routes HERE
    path(route="polls/", view=include("apps.polls.urls")),
    path(route='pastebin/', view=include('apps.pastebin.urls')),
    # path('pastebin/', include(('apps.pastebin.urls', 'pastebin'), namespace='pastebin')),
    # path('api/', view=include('pastebin.urls', namespace='pastebin')),

    # If you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # TD test
    path('api/', include(router.urls)),


    # Leave `Home.Urls` as last the last line
    path(route="", view=include("apps.accounts.urls")),
    path(route="", view=include("apps.home.urls")),


]
