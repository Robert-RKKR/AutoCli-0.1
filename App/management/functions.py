# Django import:
from django.utils.translation import gettext_lazy as _
from django.utils.translation import (
    get_language, activate, gettext
)

# Functions:
def translate(language, data):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext(data)
    finally:
        activate(cur_language)
    return text