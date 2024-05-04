class DataUrls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'
    CREATE_COURIER = 'api/v1/courier/'
    DELETE_COURIER = 'api/v1/courier/:id/' # как вытаскивать id?
    LOGIN_COURIER = 'api/v1/courier/login/'


class DataCourier:
    data_dublicate = {
        "login": "wena",
        "password": "1234",
        "firstName": "saske"
    }

    data_no_one_field = {
        "login": "",
        "password": "1234",
        "firstName": "qeqweq"
    }

    data_auth = {
        "login": "wenja",
        "password": "1234"
    }