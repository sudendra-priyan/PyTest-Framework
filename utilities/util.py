import logging
import time
import traceback
import utilities.custom_logger as cl


# All most commonly used utilities should be implemented in this class
class Util(object):
    file = "utilities/data.xlsx"
    log = cl.customLogger(logging.INFO)

    # Put the program to wait for the specified amount of time
    def sleep(self, sec):

        if sec is not None:
            self.log.info("Wait :: '" + str(sec) + "' seconds")
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    # Verify actual text contains expected text string
    def verifyTextContains(self, actualText, expectedText):

        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            print("### VERIFICATION CONTAINS !!!")
            return True
        else:
            print("### VERIFICATION DOES NOT CONTAINS !!!")
            return False
