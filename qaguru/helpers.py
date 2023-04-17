import os


def resources_path(file_name):
    return os.getcwd() + f'/tests/resources/{file_name}'
