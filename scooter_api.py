import requests
import allure
from data import DataUrls, DataCourier


class MethodsCourier:
# создание курьера
    @staticmethod
    @allure.step("Создание нового курьера в системе")
    def create_courier(data):
        response = requests.post(DataUrls.BASE_URL + DataUrls.CREATE_COURIER, data=data)
        return response

# логин курьера в системе
    @staticmethod
    @allure.step("Логин курьера в системе")
    def login_courier(data):
        response = requests.post(DataUrls.BASE_URL + DataUrls.LOGIN_COURIER, data=data)
        id_courier = response.json()['id']
        return response

    #@classmethod
    #@allure.step("")