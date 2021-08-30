import requests


class ApiLogin():
    def api_post_login(self, url, username, password):
        headers = {'Content-Type': 'application/json'}
        data = {'username': 'admin', 'password': '123456'}
        return requests.post(url, json=data, headers=headers)

    def api_get_weather(self, url, body):
        headers = {'Content-Type': 'application/json'}
        return requests.get(url=url, params=body, headers=headers)

    def api_get_calendar(self, url, body):
        headers = {'Content-Type': 'application/json'}
        return requests.get(url=url, params=body, headers=headers)
