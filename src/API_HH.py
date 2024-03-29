from abc import ABC, abstractmethod

import requests


class GetAPI(ABC):
    """Абстрактный класс для получения API"""

    @abstractmethod
    def response(self):
        pass



class HhAPI(GetAPI):
    """Класс для работы с API сайта hh, запрашивает вакансии по нужной профессии,
    для сохранения данных в json файл и дальнейшего взаимодействия с пользователем"""

    def __init__(self,text, page=0, per_page=100):

        self.text = text
        self.page = page
        self.per_page = per_page
        # Справочник для параметров GET-запроса
        self.params = {
            'text': self.text,  # Текст фильтра.
            'area': 1,  # Поиск осуществляется по вакансиям города Москва
            'page': self.page,  # Индекс страницы поиска на HH
            'per_page': self.per_page  # Кол-во вакансий на 1 странице
        }
        self.url = "https://api.hh.ru/vacancies"  # Адрес для GET-запроса

    def response(self):
        """Получение ответа с сервера"""
        response = requests.get(self.url, self.params)
        response.raise_for_status()
        return response
