#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shiva.settings")

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    sys.path.append(os.path.join(BASE_DIR, 'src/'))
    sys.path.append(os.path.join(BASE_DIR, 'src/apps'))
    sys.path.append(os.path.join(BASE_DIR, 'lib'))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
