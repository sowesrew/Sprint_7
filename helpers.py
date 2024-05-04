import requests
import random
import string


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
class DataGeneration:
    @classmethod
    def register_new_courier_and_return_login_password(cls):
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length = 10):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # генерируем логин, пароль и имя курьера
        login = generate_random_string()
        password = generate_random_string()
        first_name = generate_random_string()

        # возвращаем список
        return {
            "login": login,
            "password": password,
            "firstName": first_name
        }
