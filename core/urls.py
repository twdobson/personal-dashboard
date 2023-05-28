# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path(route='admin/', view=admin.site.urls),          # Django admin route
    path(route="", view=include("apps.authentication.urls")), # Auth routes - login / register
    path('__debug__/', include('debug_toolbar.urls')),

    # ADD NEW Routes HERE
    path(route="polls/", view=include("apps.polls.urls")),

    # Leave `Home.Urls` as last the last line
    path(route="", view=include("apps.accounts.urls")),
    path(route="", view=include("apps.home.urls")),


]
