import os
from hw_mid_level_step_objects import tests


def resources_path(file_name):
    # return os.getcwd() + f'/tests/resources/{file_name}'
    return os.path.abspath(os.path.join(os.path.dirname(tests.__file__), f'resources/{file_name}'))
