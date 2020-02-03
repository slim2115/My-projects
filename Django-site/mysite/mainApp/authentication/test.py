# Подключить встроенный сервер Django для использования клиента Selenium 
from django.test import LiveServerTestCase
# Подключить вебдрайвер управления браузером (тут FireFox)
from selenium import webdriver
import time

class SeleniumTest(LiveServerTestCase):
    def test_auth(self):
        # Подключить webdriver Firefox
        br = webdriver.Firefox()
        # Перейти на главную страницу, получив адрес сервера 'localhost:8081' и полный URL
        br.get('%%' % (self.live_server_url, '/'))
        # Перейти по ссылке регистрации
        br.find_element_by_xpath('//a[@href="/register/"]').click()
        # Подождать 3 секунды
        time.sleep(3)

        # Регистрация пользователя
        # Найти поле username и указать значение 'new'
        br.find_element_by_id('username').send_keys('new')
        # Найти поле email и указать значение 'new@new.ru'
        br.find_element_by_id('email').send_keys('new@new.ru')
        # Указать пароль в 2-ух полях
        br.find_element_by_id('password1').send_keys('12345678user')
        br.find_element_by_id('password2').send_keys('12345678user')
        # Перейти по ссылке регистрации
        br.find_element_by_id('btn_register').click()

        # Активизировать пользователя в тестовой БД    
        pis = Myuser.objects.get(username='new')
        # Поставить признак пользователя - Активен
        pis.is_active = True
        # Сохранить в БД
        pis.save()

        # Перейти на домашнюю страницу
        br.find_element_by_xpath('//a[@href="/"]').click()
        # Подождать 3 секунды
        time.slepp(3)

        # Войти под зарегистрированным пользователем
        br.find_element_by_id('username').send_keys('new')
        br.find_element_by_id('password').send_keys('12345678')
        br.find_element_by_name('Вход').click()
        # Проверить наличие имени авторизованного пользователя в соответствующем теге
        assert br.find_element_by_xpath('//a[@data-content="Личный кабинет"]').text == 'new'

        # Отключить вебдрайвер, закрыть браузер
        br.quit()



        
