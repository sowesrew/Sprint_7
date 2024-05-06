import requests
import allure
from data import DataUrls
from helpers import DataGeneration


class MethodsCourier:
# создание курьера
    @staticmethod
    @allure.step("Создание нового курьера в системе")
    def create_courier(data_payload):
        response = requests.post(DataUrls.BASE_URL + DataUrls.CREATE_COURIER, data=data_payload)
        return response

# дубликат создания курьера
    @staticmethod
    @allure.step("Повторное создание курьера")
    def dublicate_create_courier(data_payload):
        requests.post(DataUrls.BASE_URL + DataUrls.CREATE_COURIER, data=data_payload)
        response_two = requests.post(DataUrls.BASE_URL + DataUrls.CREATE_COURIER, data=data_payload)
        return response_two

# отсутствует одно из обязательных полей
    @staticmethod
    @allure.step("Попытка создания курьера без одного обязательного поля")
    def not_once_required_field():
        data_login = DataGeneration.create_new_courier_and_return_login_password()["login"]
        data = {
            "login": data_login,
            "password": ""
        }
        response = requests.post(DataUrls.BASE_URL + DataUrls.CREATE_COURIER, data=data)
        return response

# логин курьера в системе
    @staticmethod
    @allure.step("Логин курьера в системе")
    def login_courier(data_payload):
        requests.post(DataUrls.BASE_URL + DataUrls.CREATE_COURIER, data=data_payload)
        response = requests.post(DataUrls.BASE_URL + DataUrls.LOGIN_COURIER, data=data_payload)
        return response

# нет поля пароль у курьера
    @staticmethod
    @allure.step("Попытка логина курьера в системе без поля Пароль")
    def login_courier_not_field_password():
        data_payload = DataGeneration.create_new_courier_and_return_login_password()
        data = {
            "login": data_payload["login"],
            "password": ""
        }
        response = requests.post(DataUrls.BASE_URL + DataUrls.LOGIN_COURIER, data=data)
        return response

# несуществующий логин и пароль
    @staticmethod
    @allure.step("Попытка залогиниться в систему с несуществующими логином и паролем")
    def login_no_such_username_and_password():
        data_payload = DataGeneration.create_new_courier_and_return_login_password()
        response = requests.post(DataUrls.BASE_URL + DataUrls.LOGIN_COURIER, data=data_payload)
        return response


class DataOrder:
# создание заказа
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(payload):
        response = requests.post(DataUrls.BASE_URL + DataUrls.ORDER, data=payload)
        return response

# получение списка заказов
    @staticmethod
    @allure.step("Получение списка заказов")
    def get_list_order():
        response = requests.get(DataUrls.BASE_URL + DataUrls.ORDER)
        return response
