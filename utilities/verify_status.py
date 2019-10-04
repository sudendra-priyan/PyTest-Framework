import utilities.custom_logger as cl
import logging
from base.seleniumDriver import SeleniumDriver


# Assertion Handled here.
class VerifyStatus(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super(VerifyStatus, self).__init__(driver)
        self.driver = driver
        self.resultList = []

    # For adding result to result list
    def setResult(self, result, resultMessage):

        if result is not None:
            if result:
                self.resultList.append("PASS")
                self.log.info("### VERIFICATION SUCCESSFUL ###")
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                self.driver.screenShot(resultMessage)

        else:
            self.resultList.append("FAIL")
            self.log.error("### VERIFICATION FAILED :: + " + resultMessage)

    # For marking a single assertion
    def singleAssertion(self, result, resultMessage):
        self.setResult(result, resultMessage)

    # For marking the last assertion in the test function
    def finalAssertion(self, testName, result, resultMessage):
        self.setResult(result, resultMessage)
        if "FAIL" in self.resultList:
            self.log.error(testName + " ### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True
