from scooter_api import MethodsCourier


class TestLoginCourier:
    def test_successful_courier_login(self):
        user = MethodsCourier.login_courier()
        assert user.status_code == 200 and user.json()['id'] != 0

    def test_not_password_courier(self):
        user = MethodsCourier.login_courier_not_field_password()
        assert user.status_code == 400 and user.json()['message'] == 'Недостаточно данных для входа'

    def test_no_such_username_and_password(self):
        user = MethodsCourier.login_no_such_username_and_password()
        assert user.status_code == 404 and user.json()['message'] == 'Учетная запись не найдена'
