from base.seleniumDriver import SeleniumDriver
from utilities.util import Util
import utilities.custom_logger as cl
import logging


class BasePage(SeleniumDriver):
    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    # Common function to verify Page Title
    def verifyPageTitle(self, titleToVerify):
        try:
            actualTitle = self.driver.title
            return self.util.verifyTextContains(actualTitle, titleToVerify)

        except:
            self.log.error("Failed to get page title")
            return False

    # Sleep Function
    def wait(self, sec):
        self.util.sleep(sec=sec)
