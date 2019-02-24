from selenium import webdriver
import time
from config import project_urls


class Application:

    def __init__(self, browser, project):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
            self.wd.fullscreen_window()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
            self.wd.maximize_window()
        elif browser == "IE":
            self.wd = webdriver.Ie()
            self.wd.maximize_window()

        else:
            raise ValueError(f"Unrecognized browser {browser}")
        self.url = project_urls.get(project)
        if not self.url:
            self.wd.close()
            raise ValueError(f"Ebay tu loh? {project}")

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