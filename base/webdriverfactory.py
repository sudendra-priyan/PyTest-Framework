from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverFactory:

    def __init__(self, browser):
        self.browser = browser

    # Function returns driver
    def getWebDriverInstance(self):

        base_url = "https://www.amazon.in/"

        # Installs Firefox driver
        if self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        # Installs chrome driver
        elif self.browser == "chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())

        # Installs default Browser(Chrome) if browser type is not mentioned by the user
        else:
            driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.get(base_url)
        return driver

