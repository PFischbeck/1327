import os
import sys

from django.core.management.base import BaseCommand
from flake8.engine import get_style_guide

from _1327.settings import BASE_DIR


class Command(BaseCommand):
	help = 'Run flake8.'

	def handle(self, *args, **options):
		os.chdir(os.path.join(os.path.join(BASE_DIR, '..')))
		style = get_style_guide(config_file='.flake8')
		report = style.check_files(['_1327'])
		if report.total_errors > 0:
			sys.exit(1)
