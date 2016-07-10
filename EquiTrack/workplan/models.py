import logging

from django.conf import settings
from django.db import models

from django.db import transaction, connection

logger = logging.getLogger('workplan.models')