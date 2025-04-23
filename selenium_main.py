from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


def send_keys_with_delays(element, value):
    wait = WebDriverWait(driver=browser, timeout=10)
    for i in range(len(value)):
        element.send_keys(value[i])
        wait.until(lambda _: element.get_property('value')[:i] == value[:i])


browser = webdriver.Edge()
browser.get('https://service.nalog.ru/inn.do')

browser.find_element(By.ID, 'uniPageSubtitle')
time.sleep(1)
checkButton = browser.find_element(By.ID, 'unichk_0')
checkButton.click()
time.sleep(1)
continueButton = browser.find_element(By.ID, 'btnContinue')
continueButton.click()
time.sleep(1)
surname = browser.find_element(By.ID, 'fam')
send_keys_with_delays(surname, 'your_surname')  # здесь в значении value вводим Фамилию
time.sleep(1)
name = browser.find_element(By.ID, 'nam')
send_keys_with_delays(name, 'your_name')  # здесь в значении value вводим Имя
time.sleep(1)
patronymic = browser.find_element(By.ID, 'otch')
send_keys_with_delays(patronymic, 'your_patronymic')  # здесь в значении value вводим Отчество
time.sleep(1)
dateOfBirth = browser.find_element(By.ID, 'bdate')
send_keys_with_delays(dateOfBirth, 'your_date')  # здесь в значении value вводим Дату Рождения вида dd.mm.yyyy
time.sleep(2)
dropDown = browser.find_element(By.ID, "uni_select_1")
dropDown.click()
time.sleep(2)
docType = browser.find_element(By.CSS_SELECTOR, "#uni_select_4 > li:nth-child(9)")
docType.click()
time.sleep(2)
documentNumber = browser.find_element(By.ID, 'docno')
send_keys_with_delays(documentNumber, 'your_number')  # здесь в значении value вводим Номер Паспорта вида 11 11 111111
time.sleep(2)
dateOfIssue = browser.find_element(By.ID, 'docdt')
send_keys_with_delays(dateOfIssue, 'your_date2')  # здесь в значении value вводим Дату Выдачи Паспорта вида dd.mm.yyyy
time.sleep(2)
continueButton2 = browser.find_element(By.ID, 'btn_send')
continueButton2.click()
time.sleep(10)
browser.close()
