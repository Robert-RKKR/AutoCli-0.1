# Django import:
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy as _

# Decorators Import:
from django.contrib.auth.decorators import login_required

# Application Import:
from logger.logger import Logger
from logger.models import LoggerData
from .models import (
    Device,
)

# Main data dictionary:
main_data = {
    
}


# All views:
def devices_search(request):
    # Collect object:
    device = Device.objects.filter(status=True)

    # Collect data to display:
    data = {
        'url': request.path[3:],
        'header': _('Devices'),
        'devices': device,
    }

    # GET method:
    if request.method == 'GET':
        return render(request, 'management/devices_search.html', data)
    
    # POST method:
    elif request.method == 'POST':
        
        # Collect data from form:
        name = request.POST.get('name')
        status = request.POST.get('active')
        ssh_status = request.POST.get('activessh')
        https_status = request.POST.get('activehttps')
        ping_status = request.POST.get('activeping')
        certificate = request.POST.get('certificate')

        # HTML / boolean value dictionary:
        output_elements = {}
        input_elements = {
            'status': status,
            'ssh_status': ssh_status,
            'https_status': https_status,
            'ping_status': ping_status,
            'certificate': certificate,
        }
        
        # Change HTML status to boolean value:
        for element in input_elements:
            if input_elements[element] == 'indeterminate':
                continue
            elif input_elements[element] == 'on':
                output_elements[element] = True
            else:
                output_elements[element] = False

        data['devices'] = Device.objects.filter(name__contains=name, **output_elements)
        return render(request, 'management/devices_search.html', data)


#@login_required(login_url='/management/devices_search')
def device(request, id):
    # Collect object:
    device = Device.objects.get(id=id)

    # Collect data to display:
    data = {
        'url': request.path[3:],
        'header': device.name,
        'device': device,
    }

    from .tasks import task_simple
    data['output'] = task_simple.delay(id)
    #data['output'] = task_simple.apply_async((id,), countdown=5)

    """from .tasks import task_simple
    data['output'] = task_simple.delay(id)"""
    data['logs'] = LoggerData.objects.filter(module=device.hostname).order_by('-id')[:10]
    
    # GET method:
    return render(request, 'management/device.html', data)

















class Testing(ListView):
    model = Device
    template_name = 'management/testing.html'
    context_object_name = 'devices'



class MainView(View):
    log = Logger('management')
    
    def __init__(self, **kwargs) -> None:
        self.template = 'management/base.html'

    def get(self, request):
        url = request.path[3:]
        return render(request, self.template, {'output':"RKKR", 'url':url})

    def post(self, request):
        url = request.path[3:]
        return render(request, self.template, {'output':"RKKR", 'url':url})


class Test(MainView):

    def __init__(self, **kwargs) -> None:
        self.template = 'management/test.html'

    def get(self, request):
        url = request.path[3:]
        return render(request, self.template, {'output':"PSP", 'url':url})


class DevicesView(MainView):

    def __init__(self, **kwargs) -> None:
        self.template = 'management/all_devices.html'

    def get(self, request):
        url = request.path[3:]
        return render(request, self.template, {'output':"PSP", 'url':url})