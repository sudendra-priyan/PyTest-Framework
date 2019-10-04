from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import logging
import utilities.custom_logger as cl


class SeleniumDriver:
    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver

    # Identifies BY type and returns it
    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    # Identifies Element and returns it
    def getElement(self, locator, locatorType="xpath"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found")

        except:
            self.log.info("Element not found")
        return element

    # Performs Click operation
    def elementClick(self, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)

        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    # Performs Send Keys operation
    def sendKeys(self, data, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Send data on element with locator: " + locator + " locatorType: " + locatorType)

        except:
            self.log.info("Cannot Send data on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    # Mimics Keyboard Enter
    def press_enter(self, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(Keys.RETURN)
            self.log.info("Send data on element with locator: " + locator + " locatorType: " + locatorType)

        except:
            self.log.info("Cannot Send data on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    # Switch to Specific tab
    def switchToTab(self, tab):
        try:
            window = self.driver.window_handles[tab]
            self.driver.switch_to.window(window)
            self.log.info("Tab switched")

        except:
            self.log.info("Tab did not switch")

    # Returns True or False based on Element existence in web
    def isElementPresent(self, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found")

                return True
            else:
                self.log.info("Element not found")
                return False

        except:
            self.log.info("Element not found")
            return False

    # Selects a item from Drop Down
    def SelectFromDropDown(self, locator, locatorType="xpath",  value="", text="", index=""):
        try:
            byType = self.getByType(locatorType)
            element = Select(self.driver.find_element(byType, locator))

            if len(value) > 0:
                element.select_by_value(value)
                self.log.info("Element Found and Selected")
            elif len(text) > 0:
                element.select_by_visible_text(text)
                self.log.info("Element Found and Selected")
            elif len(str(index)) > 0:
                element.select_by_index(index)
                self.log.info("Element Found and Selected")
            else:
                self.log.info("Element Not Found")

        except:
            print_stack()
            self.log.info("Element not found")

    # Returns True or False based on elements visibility
    def isDisplayed(self, locator, locatorType="xpath"):
        try:
            byType = self.getByType(locatorType)
            result = self.driver.find_element(byType, locator).is_displayed()
            if result:
                self.log.info("Element Found")
                return result
            else:
                self.log.info("Element not found")
                return result

        except:
            self.log.info("Element not found")
            return False

    # Returns True or False based on given text is available in the current page
    def isTextPresentInPage(self, text):
        return self.driver.page_source.__contains__(text)

    # Returns Text of the element
    def getText(self, locator, locatorType="xpath"):
        try:
            byType = self.getByType(locatorType)
            result = self.driver.find_element(byType, locator).text
            self.log.info("Element found")
            return result

        except:
            self.log.info("Element not found")
            return False

    # Switches to specific Tab
    def switchTab(self, tab):
        self.driver.switch_to.window(self.driver.window_handles[tab])

    # Executes the Java Script passed
    def executeJavaScript(self, data):
        try:
            if self.driver.execute_script(data):
                self.log.info("JS Executed and element found")
                return True

            else:
                self.log.info("JS Executed and element not found")
                return False

        except:
            self.log.info("Element not found")
            return False

    # Waits for element
    def waitForElement(self, locator, locatorType="xpath", timeout=10, pollFrequency=0.2):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=0.1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     ElementClickInterceptedException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))

            self.log.info("Element appeared on the web page")

        except:
            self.log.info("Element not appeared on the web page")
        return element
