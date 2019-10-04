from base.basePage import BasePage
from pages.book_details_page import BookDetails
from utilities import excel_util


class AmazonHome(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.book_details = BookDetails(self.driver)
        self.input_sheet = 'input'
        self.output_sheet = 'output'

    """
      ############## Locators of the page ##############
    """
    # Common xpath of the page
    Categories_DropDown_xpath = "//select[@id='searchDropdownBox']"
    Search_Bar_xpath = "//input[@id='twotabsearchtextbox']"
    First_Search_Result_xpath = "(.//*[@class='a-link-normal a-text-normal'])[2]"

    # xpath for Verification
    Books_Tab_xpath = "//a[@class='nav-a nav-b']"
    Books_Link_xpath = "(.//*[@class='a-link-normal a-text-normal'])[1]"

    """
    ############## Functions of the page ##############
    """
    # Choose the Category & Search
    def choose_book_category(self):
        dropDown = excel_util.readData(self.input_sheet, rowNum=1, columnNum=1)
        searchText = excel_util.readData(self.input_sheet, rowNum=2, columnNum=1)
        self.SelectFromDropDown(locator=self.Categories_DropDown_xpath, value=dropDown)
        self.sendKeys(data=searchText, locator=self.Search_Bar_xpath)
        self.press_enter(locator=self.Search_Bar_xpath)

    # Click on first occurrence
    def select_first_search_result(self):
        self.waitForElement(locator=self.First_Search_Result_xpath)
        self.elementClick(locator=self.First_Search_Result_xpath)

    """
    ############## Verification Function of the page ##############
    """

    # Checks for Book Tab which appears after Searching about Books
    def verify_books_navigation_bar_tab(self):
        return self.isDisplayed(self.Books_Tab_xpath)

    # Checks for Book Link which appears after Searching about Books
    def verify_books_post_search_link(self):
        return self.isDisplayed(self.Books_Link_xpath)
