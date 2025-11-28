from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

        # добавим обработку Alert, вдруг его добавят разработчики!
        #alert = self.browser.switch_to.alert
        #alert.accept()

        # 1-й способ реализации перехода между страницами: возвращать нужный Page Obgect
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
        # 2-й способ без return

