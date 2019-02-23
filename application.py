from selenium import webdriver
import time
from config import projects


class Application:

    def __init__(self, browser, project):  #
        if browser == "chrome":
            self.wd = webdriver.Chrome()
            self.wd.fullscreen_window()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
            self.wd.maximize_window()
        elif browser == "IE":
            self.wd = webdriver.Ie()
            self.wd.maximize_window()
        if project == '99papers':
            self.url = projects['99papers']   # найти путь как тянуть из списка прототип
        # self.url = 'https://99papers.com/'  # рабочий вариант для унификации проекта
        # elif project == 'bookwormlab':
        #     self.url = 'https://bookwormlab.com/'
        else:
            raise ValueError("Unrecognized browser {}".format(browser))

    def simple_test(self):
        self.wd.get(self.url)
        time.sleep(3)

    def second_simple_test(self):
        self.wd.get(self.url)
        time.sleep(1)
        print('\n im passed')

    def object_login(self):
        self.wd.find_element_by_xpath('Login').click()

    def destroy(self):
        self.wd.close()


    # екземпл запуска гибкого теста
    # pytest -sv --browser=firefox --project=bookwormlab Tests/UI/tests_some_selenium.py