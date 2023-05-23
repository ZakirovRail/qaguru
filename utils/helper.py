import os
import tests
import logging
import curlify
import allure

from allure import step
from allure_commons.types import AttachmentType
from requests import Session


class Globals:
    REQRES_URL = os.getenv('REQRES_URL')
    REQRES_API = os.getenv('REQRES_API')
    TRICENTIS_URL = os.getenv('TRICENTIS_URL')
    WEB_SHOP_API_URL = os.getenv('WEB_SHOP_API_URL')


def resources_path(file_name):
    return os.path.abspath(os.path.join(os.path.dirname(tests.__file__), f'resources/{file_name}'))


def console_logger(function):
    def wrapper(*args, **kwargs):
        response = function(*args, **kwargs)
        logging.info(curlify.to_curl(response.request))
        logging.info(response.text)
        return response
    return wrapper


class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    @console_logger
    def request(self, method, url, **kwargs):
        with step(f'Вызов метода:{method} end-point: {url}'):
            response = super().request(method=method, url=f'{self.base_url}{url}', **kwargs)
            content_type = response.headers.get("content-type", None)

            # logging.info(f"Status code: {response.status_code}")
            # logging.info(curlify.to_curl(response.request))
            curl_log = f'STATUS CODE: {response.status_code} {curlify.to_curl(response.request)}'

            if not content_type:
                logging.warning(f"\n Was not received the content-type, check the response: '{response.text}'")
            elif "text" in content_type:
                logging.info(f"\n Response is text: {response.text}")
            elif "json" in content_type:
                logging.info(f"\n Response is json : {response.text}")

        allure.attach(curl_log, 'curl_logs', AttachmentType.TEXT, '.log')
        allure.attach(response.text, 'response_log', AttachmentType.TEXT, '.log')

        return response
