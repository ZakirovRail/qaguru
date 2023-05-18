import logging
import requests
import pytest

from pytest_voluptuous import S
from requests import Response

from schemas import Schemas
from hamcrest import assert_that
import json
# from tests.schemas.reqres import new_user_unsuccessful_register, new_user_successful_register, user_login_successful, \
#     user_login_unsuccessful, list_users_schema



logger = logging.getLogger(__name__)

base_url = "https://reqres.in/api/users"


class TestListUsers:

    @pytest.mark.parametrize("page_number", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_get_list_users(self, page_number):
        request_url = f"{base_url}?page={page_number}"
        response: Response = requests.get(url=request_url)
        logger.info(f"\n The path for sending request is: {request_url}")
        print(f"\n The path for sending request is: {request_url}")
        assert response.status_code == 200

    @pytest.mark.parametrize("page_number", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_check_list_users_check_schema(self, page_number):
        response: Response = requests.get(url=base_url, params={"page": page_number})
        assert S(Schemas.schema_list_users) == response.json()

    @pytest.mark.parametrize("page_number", ["=", "!", ",", "-", "?", "@", "#", "$"])
    def test_list_user_symbols_as_page_number(self, page_number):
        request_url = f"{base_url}?page={page_number}"
        response: Response = requests.get(url=request_url)
        print(f"\n The path for sending request is: {request_url}")
        #  Для меня странно, что сервис не обрабатывает спецсимволы и возвращает статус код 200. Но, что есть
        assert response.status_code == 200


class TestSingleUser:

    @pytest.mark.parametrize("user_id, status_code",
                             [(1, 200),
                              (2, 200),
                              (3, 200),
                              (4, 200),
                              (5, 200),
                              (23, 404)])
    def test_get_single_user(self, user_id, status_code):
        request_url = f"{base_url}/{user_id}"
        logger.info(f"\n The path for sending request is: {request_url}")
        print(f"\n The path for sending request is: {request_url}")
        response: Response = requests.get(url=request_url)
        assert response.status_code == status_code

    @pytest.mark.parametrize("user_id, status_code",
                             [("!", 404),
                              ("=", 404),
                              ("-", 404),
                              ("?", 200),
                              ("+", 404),
                              ("XXX", 404),
                              ("4XX", 404)])
    def test_get_single_user_symbolic_id(self, user_id, status_code):
        request_url = f"{base_url}/{user_id}"
        logger.info(f"\n The path for sending request is: {request_url}")
        print(f"\n The path for sending request is: {request_url}")
        response: Response = requests.get(url=request_url)
        assert response.status_code == status_code

    @pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_get_single_user_check_schema(self, user_id):
        request_url = f"{base_url}/{user_id}"
        response: Response = requests.get(url=request_url)
        assert S(Schemas.schema_single_user) == response.json()


class TestNewUser:

    @pytest.mark.parametrize("name, job, status_code",
                             [("Nikolas Keige", "Actor", 201),
                              ("John Wick", "Killer", 201),
                              ("John Langh", "Super Hero", 201),
                              ("Capitan America", "Solder", 201),
                              ("!", "#", 201),
                              ("202", "TestSymbols", 201),
                              ("TestSymbols", "203", 201),
                              ("", "", 201),
                              ("204", "204", 201)])
    def test_new_user(self, name, job, status_code):
        response: Response = requests.post(url=base_url, data={"name": name, "job": job})
        assert response.status_code == status_code

    @pytest.mark.parametrize("name, job, status_code",
                             [("Nikolas Keige", "Actor", 201),
                              ("John Wick", "Killer", 201),
                              ("morpheus", "leader", 201),
                              ("John Langh", "Super Hero", 201),
                              ("Capitan America", "Solder", 201),
                              ("!", "#", 201),
                              ("202", "TestSymbols", 201),
                              ("TestSymbols", "203", 201),
                              ("", "", 201),
                              ("204", "204", 201)])
    def test_new_user_check_schema(self, name, job, status_code):
        response: Response = requests.post(url=base_url, data={"name": name, "job": job})
        assert S(Schemas.schema_create_new_user) == response.json()


class TestUpdateUser:

    def test_update_user_with_put(self):
        request_url = f"{base_url}/2"
        data = {"name": "morpheus", "job": "zion resident"}
        response: Response = requests.put(url=request_url, data=data)
        assert response.status_code == 200

    def test_update_user_with_put_check_schema(self):
        request_url = f"{base_url}/2"
        data = {"name": "morpheus", "job": "zion resident"}
        response: Response = requests.put(url=request_url, data=data)
        assert S(Schemas.schema_update_user) == response.json()

    def test_update_user_with_patch(self):
        request_url = f"{base_url}/2"
        data = {"name": "morpheus", "job": "zion resident"}
        response: Response = requests.patch(url=request_url, data=data)
        assert response.status_code == 200

    def test_update_user_with_patch_check_schema(self):
        request_url = f"{base_url}/2"
        data = {"name": "morpheus", "job": "zion resident"}
        response: Response = requests.put(url=request_url, data=data)
        assert S(Schemas.schema_update_user) == response.json()

class TestRegisterUser:

    @pytest.mark.parametrize("email, password, status_code", [("eve.holt@reqres.in", "pistol", 200)])
    def test_new_user_successful_register(self, reqres_base, email, password, status_code):
        url = "/register"
        response: Response = reqres_base.post(url=url, data={"email": email, "password": password})
        assert_that(response.status_code == 200)
        assert S(Schemas.new_user_successful_register) == response.json()

    @pytest.mark.parametrize("email, password, status_code, error_message",
                             [('test_user_1@gmail.com', '', 400, '{"error":"Missing email or username"}'),
                              ('', 'passw_test', 400, '{"error":"Missing email or username"}'),
                              ('', '', 400, '{"error":"Missing email or username"}')])
    def test_new_user_unsuccessful_register(self, reqres_base, email, password, status_code, error_message):
        url = "/register"
        data = {"email": email, "password": password}
        response: Response = reqres_base.post(url=url, data=json.dumps(data))

        assert_that(response.status_code == status_code)
        assert_that(response.text == error_message)
        assert S(Schemas.new_user_unsuccessful_register == response.json())


class TestLoginUser:

    @pytest.mark.parametrize("email, password, status_code", [('eve.holt@reqres.in', 'cityslicka', 200)])
    def test_login_successful(self, reqres_base, email, password, status_code,):
        url =  "/login"
        response: Response = reqres_base.post(url=url, data={"email": email, "password": password})
        assert_that(response.status_code == status_code)
        assert S(Schemas.user_login_successful == response.json())

    @pytest.mark.parametrize("email, password, status_code, error_message",
                             [('peter@klaven', '', 400, '{"error":"Missing email or username"}')])
    def test_login_unsuccessful(self, reqres_base, email, password, status_code, error_message):
        url = "/register"
        data = {"email": email}
        response: Response = reqres_base.post(url=url, data=json.dumps(data))

        assert_that(response.status_code == status_code)
        assert_that(response.text == error_message)
        assert S(Schemas.user_login_unsuccessful == response.json())


class TestDelayedResponse:

    def test_show_users_delayed(self, reqres_base):
        url = "/users"
        response: Response = reqres_base.get(url, params={"delay": 3})
        assert_that(response.status_code == 200)
        assert S(Schemas.list_users_schema == response.json())


class TestDeleteUser:
    def test_delete_existing_user(self, reqres_base):
        url = "/users/2"
        response: Response = reqres_base.delete(url)
        assert_that(response.status_code == 204)

    # Это странно, но по идее тест должен падать. По сути, получается что подгоняют тест под текущую реализацию
    def test_delete_not_existing_user(self, reqres_base):
        url = "/users/abc"
        response: Response = reqres_base.delete(url)
        assert_that(response.status_code == 204)

    # Это странно, но по идее тест должен падать - возвращаться ошибка, что не указан ID пользователя. Но как есть
    def test_delete_user_no_id(self, reqres_base):
        url = "/users"
        response: Response = reqres_base.delete(url)
        assert_that(response.status_code == 204)