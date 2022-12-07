#!/usr/bin/env python

"""Code to run before generating the project.

Adapted from https://github.com/audreyfeldroy/cookiecutter-pypackage/blob/master/hooks/pre_gen_project.py.
"""

import re
import sys

MODULE_REGEX = re.compile(r'^[-a-zA-Z][-a-zA-Z0-9]+$')

package_name = '{{ cookiecutter.package_name}}'

if not MODULE_REGEX.match(package_name):
    print(
        f'ERROR: {package_name} is not a valid Python package name. Please do not use _ and use - instead'
    )

    # Exit to cancel project
    sys.exit(1)
