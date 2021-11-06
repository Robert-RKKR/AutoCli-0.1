# Python Import:
from jinja2 import Environment, BaseLoader

# Django Import:
from django.shortcuts import render

# Applications Import:
from .models import (
    Template,
)

# Task Import:
from management.tasks import send_commands

# Create your views here.
def template(request, id):
    # Collect object:
    template = Template.objects.get(pk=id)

    # Collect data to display:
    data = {
        'url': request.path[3:],
        'template': template,
    }

    to_render = Environment(loader=BaseLoader).from_string(template.value)
    rendered = to_render.render(vlans=[1,2,3,4], configuration='Test')
    data['test'] = rendered

    from management.connection.netcon import NetCon
    

    
    """print('---> SELECT: ', template.value)
    print('---> RENDERED: ', rendered.split('\n'))

    data['output'] = send_commands.delay(4, rendered.split('\n'))"""

    return render(request, 'automation/template.html', data)


def template_search(request):
    # Collect object:
    templates = Template.objects.all()

    # Collect data to display:
    data = {
        'url': request.path[3:],
        'templates': templates,
    }

    # GET method:
    if request.method == 'GET':
        return render(request, 'automation/template_search.html', data)

    # POST method:
    elif request.method == 'POST':
        # Collect data from form:
        name = request.POST.get('name')

        # Collect object:
        data['templates'] = Template.objects.filter(name=name)

        return render(request, 'automation/template_search.html', data)