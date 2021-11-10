# Django Import:
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

# Create your views here.
def login_page(request):

    # Collect data to display:
    data = {
        'url': request.path[3:],
        'header': _('Devices'),
        'output': 'administrators',
    }

    return render(request, 'administrators/login_page.html', data)