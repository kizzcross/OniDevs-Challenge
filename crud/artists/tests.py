from django.test import TestCase
from .models import *
import logging

logger = logging.getLogger(__name__)
logger.warning(getMusicsOfArtist('Artista 1'))
