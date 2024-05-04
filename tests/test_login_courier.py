from scooter_api import MethodsCourier
from data import DataCourier


class TestLoginCourier:
    def test_successful_courier_login(self):
        user = MethodsCourier.login_courier(DataCourier.data_auth)
        assert user.status_code == 200 and user.json()['id'] == 299342
