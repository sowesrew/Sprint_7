import allure
import pytest
from helpers import DataGenerationOrder
from scooter_api import DataOrder


class TestCreateOrder:
    @allure.title('Проверка создания заказа')
    @allure.description('Создание заказа с различным выбором цвета самоката')
    @pytest.mark.parametrize(
        'payload',
        [
            DataGenerationOrder.create_data_for_order(["BLACK"]),
            DataGenerationOrder.create_data_for_order(["BLACK", "GREY"]),
            DataGenerationOrder.create_data_for_order([""])
        ]
    )
    def test_create_order(self, payload):
        order = DataOrder.create_order(payload)
        assert order.status_code == 201 and order.json()['track'] != 0
