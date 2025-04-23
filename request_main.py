import requests
import json
from bs4 import BeautifulSoup

headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
           "Accept-Encoding": "gzip, deflate, br, zstd",
           "Accept-Language": "ru,en;q=0.9",
           "Connection": "keep-alive",
           "Content-Length": "112",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                           "AppleWebKit/537.36 (KHTML, likeGecko) "
                           "Chrome/124.0.0.0 "
                           "YaBrowser/24.6.0.0 "
                           "Safari/537.36"
}

session = requests.Session()


url2 = 'https://service.nalog.ru/static/personal-data-proc.json'
url = 'https://service.nalog.ru/inn-new-proc.json'

# здесь необходимо ввести свои данные
payload = {"c": 'find', "captcha": '', "captchaToken": '',
           "fam": 'type your surname here', "nam": 'type your name here', "otch": 'type your patronymic here',
           "bdate": 'type your birthday date here dd.mm.yyyy', "doctype": '21',
           "docno": 'type your document number here 11 11 111111', "docdt": 'type your document date here dd.mm.yyyy'}
payload2 = {"from": '/inn.do', "svc": 'inn', "personalData": '1'}
payload3 = {"c": 'get', "requestId": ''}

request = session.post(url2, data=payload2)
request2 = session.post(url, data=payload)
answer = BeautifulSoup(request2.content, "html.parser")
token = json.loads(str(answer))["requestId"]
payload3["requestId"] = token
request3 = session.post(url, data=payload3, headers=headers)
answer = BeautifulSoup(request3.content, "html.parser")
inn = json.loads(str(answer))["inn"]
print(inn) # на этом этапе в переменной inn уже хранится ваш ИНН

