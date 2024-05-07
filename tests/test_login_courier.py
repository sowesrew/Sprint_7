import allure
from scooter_api import MethodsCourier
from conftest import create_and_delete_account_courier


class TestLoginCourier:
    @allure.title('Проверка успешного логина курьера')
    @allure.description('Создаём аккаунт курьера и логинимся на него, получаем статус 200 и убеждаемся, что id приходит')
    def test_successful_courier_login(self, create_and_delete_account_courier):
        user = MethodsCourier.login_courier(create_and_delete_account_courier)
        assert user.status_code == 200 and user.json()['id'] != 0

    @allure.title('Проверка попытки логина курьера без поля password')
    @allure.description('Пытаемся залогиниться на аккаунт без поля Пароль и получаем ошибку 400 и соответствующий текст ответа')
    def test_not_password_courier(self):
        user = MethodsCourier.login_courier_not_field_password()
        assert user.status_code == 400 and user.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Проверка логина несуществующим курьером')
    @allure.description('Пытаемся залогиниться несуществующим аккаунтом курьера, получаем ошибку 404 и соотвествующее сообщение')
    def test_no_such_username_and_password(self):
        user = MethodsCourier.login_no_such_username_and_password()
        assert user.status_code == 404 and user.json()['message'] == 'Учетная запись не найдена'
