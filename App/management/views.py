# Django Import:
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy as _

# Decorators Import:
from django.contrib.auth.decorators import login_required

# Application Import:
from .tasks import single_device_check, single_device_collect
from .forms import TestForm, AddDeviceForm
from logger.logger import Logger
from logger.models import LoggerData
from .models import (
    Device, DeviceData,
)


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

        data['devices'] = Device.objects.filter(name__contains=name, **output_elements).order_by('id')
        return render(request, 'management/devices_search.html', data)


#@login_required(login_url='/management/devices_search')
def device(request, pk):
    # Collect object:
    device = get_object_or_404(Device, pk=pk)

    # Collect data to display:
    data = {
        'url': request.path[3:],
        'header': device.name,
        'device': device,
    }

    #output.append(single_device_collect.delay(device.id))
    #data['output'] = task_simple.apply_async((id,), countdown=5)
    #data['output'] = update_all.delay()
    #output.append(single_device_check(device.id))
    #output.append(single_device_collect(device.id))
    
    #output.append(single_device_check.delay(device.id))
    output = single_device_collect.delay(device.pk)
    data['response_output'] = output.id


    #data['device_data'] = DeviceData.objects.filter(device=device).latest('created')
    data['logs'] = LoggerData.objects.filter(module=device.hostname).order_by('-pk')[:10]
    
    # GET method:
    return render(request, 'management/device.html', data)


def device_add(request):

    # Collect data to display:
    data = {
        'url': request.path[3:],
        'header': _('Devices')
    }

    # GET method:
    if request.method == 'GET':
        # Form declaration:
        form = AddDeviceForm()
        data['form'] = form
        return render(request, 'management/device_add.html', data)

    # POST method:
    elif request.method == 'POST':
        # Form declaration:
        form = AddDeviceForm(request.POST)
        data['form'] = form

        if form.is_valid():
            device = form.save()
            output = single_device_collect.delay(device.id)
            data['response_output'] = output.id
        return render(request, 'management/device_add.html', data)


def logger_search(request):

    # Collect data to display:
    data = {
        'url': request.path[3:],
        'header': _('Logger')
    }

    # GET method:
    if request.method == 'GET':

        return render(request, 'management/logger_search.html', data)

    # POST method:
    elif request.method == 'POST':

         return render(request, 'management/logger_search.html', data)


"""def device_add(request):

    # Collect data to display:
    data = {
        'url': request.path[3:],
        'header': _('Devices')
    }

    # GET method:
    if request.method == 'GET':
        # Form declaration:
        form = TestForm()
        data['form'] = form
        return render(request, 'management/device_add.html', data)

    # GET method:
    elif request.method == 'POST':
        # Form declaration:
        form = TestForm(request.POST)
        data['form'] = form

        if form.is_valid():
            name = form.cleaned_data['name']
            print(name)
        return render(request, 'management/device_add.html', data)"""














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