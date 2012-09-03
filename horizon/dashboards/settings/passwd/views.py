# vim: tabstop=4 shiftwidth=4 softtabstop=4


# Copyright 2012 Openstack, LLC
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from django import shortcuts
from django.template import response
from horizon.api import keystone 

def index(request):
    return shortcuts.render(request, 'settings/passwd/settings.html', {})

def set_passwd(request):
    try:
        pass1=request.POST['newpasswd']
        pass2=request.POST['newpasswd2']
    except:
        return shortcuts.render(request, 'settings/passwd/settings.html', {})
    r=""
    if(len(pass1)>=6 and pass1==pass2):
        r=keystone.user_update_password(request, request.user.id,pass1, True)
        msg=True
    else:
        msg=False
    return shortcuts.render(request, 'settings/passwd/_passwdok.html', {"msg_result":msg,'keystone_r':r})