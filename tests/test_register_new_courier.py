from scooter_api import MethodsCourier


class TestRegisterNewCourier:
    def test_possible_create_courier(self):
        user = MethodsCourier.create_courier()
        assert user.status_code == 201 and user.text == '{"ok":true}'

    def test_duplicate_courier(self):
        user = MethodsCourier.dublicate_create_courier()
        assert user.status_code == 409 and user.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    def test_not_once_required_field(self):
        user = MethodsCourier.not_once_required_field()
        assert user.status_code == 400 and user.json()['message'] == 'Недостаточно данных для создания учетной записи'
