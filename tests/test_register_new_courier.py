import allure
from scooter_api import MethodsCourier
from conftest import create_and_delete_account_courier


class TestRegisterNewCourier:
    @allure.title('Проверка создания аккаунта курьера')
    @allure.description('Создаём аккаунт курьера и проверяем, что код ответа равен 201 и тело ответа соотвествует документации')
    def test_possible_create_courier(self, create_and_delete_account_courier):
        user = MethodsCourier.create_courier(create_and_delete_account_courier)
        assert user.status_code == 201 and user.text == '{"ok":true}'

    @allure.title('Проверка невозможности создания двух одинаковых аккаунтов курьеров')
    @allure.description('Посылаем два запроса с одинаковыми регистрационными данными и получаем ошибку и сообщение о ней')
    def test_duplicate_courier(self, create_and_delete_account_courier):
        user = MethodsCourier.dublicate_create_courier(create_and_delete_account_courier)
        assert user.status_code == 409 and user.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Проверка невозможности регистрации курьера без одного обязательного поля')
    @allure.description('Посылаем запрос без поля "Пароль" и пытаемся создать аккаунт, получаем ошибку и её текст')
    def test_not_once_required_field(self):
        user = MethodsCourier.not_once_required_field()
        assert user.status_code == 400 and user.json()['message'] == 'Недостаточно данных для создания учетной записи'
