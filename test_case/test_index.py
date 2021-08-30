import time

import allure
import pytest
from common.logger import Logger
from api.api_login import ApiLogin

@allure.feature('test1')
class Test_juhe():
    @allure.story('test1-3')
    def test_01_weather(self):
        url = 'http://apis.juhe.cn/simpleWeather/query'
        body = {
            'city': '郴州',
            'key': 'e3a339c7f9e19a3fae471853d28b69f1',
        }
        res = ApiLogin().api_get_weather(url, body)
        try:
            assert res.status_code == 200
            assert res.json()['error_code'] == 0
        except Exception as e:
            Logger.error(e)
            raise e

    @allure.story('test1-4')
    def test_02_calendar(self):
        url = 'http://v.juhe.cn/calendar/day'
        body = {
            'key': 'ff93d2d2299207e4af5d8d44b4477f4b',
            'date': '2021-8-16',
        }
        res = ApiLogin().api_get_calendar(url, body)
        assert res.status_code == 200
        assert res.json()['error_code'] == 0


if __name__ == '__main__':
    pytest.main(['-s', r'F:\hello\pytest2\test_case\test_index.py'])
