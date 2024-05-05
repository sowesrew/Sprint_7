import random
import string
import json
from faker import Faker


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
class DataGeneration:
    @classmethod
    def create_new_courier_and_return_login_password(cls):
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length = 10):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # генерируем логин, пароль и имя курьера
        login = generate_random_string()
        password = generate_random_string()
        first_name = generate_random_string()

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # возвращаем список
        return payload


class DataGenerationOrder:
    @staticmethod
    def create_data_for_order(color):
        fake = Faker(locale="ru_RU")
        payload = {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "address": fake.address(),
            "metroStation": random.randrange(10),
            "phone": fake.phone_number(),
            "rentTime": random.randrange(6),
            "deliveryDate": fake.date(),
            "color": color,
            "comment": fake.text(10)
        }

        return json.dumps(payload)
