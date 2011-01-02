# ScrumDo - Agile/Scrum story management web application 
# Copyright (C) 2011 Marc Hughes, Ajay Reddy
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy (See file COPYING) of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

from django.conf.urls.defaults import *

from organizations.models import Organization
from organizations.team_models import Team

# from groups.bridge import ContentBridge
# 
# 
# bridge = ContentBridge(Project, 'projects')

urlpatterns = patterns('organizations.views',
    url(r'^debug/$', "team_debug"),
    url(r'^create/$', 'organization_create', name="organization_create"),
    url(r'^list/$', 'your_organizations', name="your_organizations"),    
    url(r'^(?P<organization_slug>[-\w]+)/$', 'organization', name="organization_detail")        ,
    url(r'^(?P<organization_slug>[-\w]+)/edit$', 'organization_edit', name="organization_edit")        
)


urlpatterns += patterns('organizations.team_views',
   url(r'^(?P<organization_slug>[-\w]+)/team/create$', 'team_create', name="team_create"),
   url(r'^(?P<organization_slug>[-\w]+)/team/(?P<team_id>[-\w]+)$', 'team', name="team_detail"),

)