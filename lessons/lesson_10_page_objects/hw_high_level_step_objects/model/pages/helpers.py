import os

from lessons.lesson_10_page_objects.hw_high_level_step_objects import tests
# from hw_high_level_step_objects import tests


def resources_path(file_name):
    return os.path.abspath(os.path.join(os.path.dirname(tests.__file__), f'resources/{file_name}'))
