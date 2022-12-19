import logging

from {{cookiecutter.module_name}} import Api

# Script to use to try the package in development

# Setup logger
log = logging.getLogger()
log.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(levelname)s: [%(module)s:%(funcName)s] %(message)s")
console_handler.setFormatter(formatter)
log.addHandler(console_handler)

# Add code to test the lib in development
api = Api()
print(api.get_hello_world("test"))
