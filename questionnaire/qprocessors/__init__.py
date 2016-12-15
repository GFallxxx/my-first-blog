from django.conf import settings
from questionnaire import *
from django.utils.translation import ugettext as _

from . import simple           # store value as returned
from . import choice           # multiple choice, do checks
from . import range_or_number  # range of numbers
from . import timeperiod       # time periods
from . import custom           # backwards compatibility support

add_type('custom', 'Custom field')