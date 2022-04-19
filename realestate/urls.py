
from django.contrib import admin
from django.urls import path

from .views import * #addproperty, index, login, signup, sellhome, buy, agent, auction, rent, homeloan, bid, applyagent, dashboard, propertydetails, addproperty, property_detail

# admin.site.site_header = "REMS"
# admin.site.site_title = "welcome to REMS"
# admin.site.index_title = "Welcome to the portal"
urlpatterns = [
    path('', index, name='home'),
    path('login/', login),
    path('signup', signup),
    path('logout', logout, name='logout'),

    path('sellhome', sellhome),
    path('buy', buy, name = 'buy'),
    path('agent', agent, name = 'agent'),
    path('applyagent', applyagent, name = 'applyagent'),
    path('auction', auction),
    path('rent', rent),
    path('homeloan', homeloan),
    path('bid/<int:pk>/', bid, name = 'bid'),
    path('dashboard', dashboard),
    path('propertydetails', property_list, name='property_list'),
    path('search-prop/', serach_property, name ='search-prop'),

    path('update_property/<int:pk>/', update_property, name='update_property'),

    path('addproperty/', addproperty, name='addproperty'),

    path('property-detail/<int:pk>/', property_detail, name = 'property_detail'),
    path('delete/<int:id>', delete, name='delete'),

    path('bidder-list/<int:pk>/', bidders_list, name = 'bidder-list')
]
