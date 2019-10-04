from base.basePage import BasePage
from utilities import excel_util


class BookDetails(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.input_sheet = 'input'
        self.output_sheet = 'output'

    """
      ############## Locators of the page ##############
    """
    # Xpath's related to data which we want to save
    Book_Title_xpath = "//span[@id='productTitle']"
    Seller_Name_xpath = "//span[@class='author notFaded']"
    PaperBack_Type_xpath = "//a[@class='a-button-text']//span[contains(text(),'Paperback')]"
    PaperBack_Price_xpath = "//a[@class='a-button-text']//span[contains(text(),'Paperback')]/following-sibling::span//span"
    KindleEdition_Type_xpath = "//a[@class='a-button-text']//span[contains(text(),'Kindle Edition')]"
    KindleEdition_Price_xpath = "//a[@class='a-button-text']//span[contains(text(),'Kindle Edition')]/following-sibling::span//span"
    HardCover_Type_xpath = "(//a[@class='a-button-text']//span[contains(text(),'Hardcover')])[1]"
    HardCover_Price_xpath = "(//a[@class='a-button-text']//span[contains(text(),'Hardcover')]/following-sibling::span//span)[1]"
    PaperBack_Detail_xpath = "(//div[@class='content']//ul//li)[1]"
    Publisher_Detail_xpath = "(//div[@class='content']//ul//li)[2]"
    Language_Detail_xpath = "(//div[@class='content']//ul//li)[3]"
    ISBN10_Detail_xpath = "(//div[@class='content']//ul//li)[4]"
    ISBN13_Detail_xpath = "(//div[@class='content']//ul//li)[5]"
    Dimension_Detail_xpath = "(//div[@class='content']//ul//li)[6]"
    Close_Pop_UP_xpath = "//*[@id='a-popover-3']/div/header/button"

    # Formed a Dictionary for different type of books editions
    Type_Price_Dict = {PaperBack_Type_xpath: PaperBack_Price_xpath,
                       KindleEdition_Type_xpath: KindleEdition_Price_xpath,
                       HardCover_Type_xpath: HardCover_Price_xpath
                       }
    # Formed a list for all other Misc Details regarding the book
    Misc_Details_list = [PaperBack_Detail_xpath,
                         Publisher_Detail_xpath,
                         Language_Detail_xpath,
                         ISBN10_Detail_xpath,
                         ISBN13_Detail_xpath,
                         Dimension_Detail_xpath]

    # xpath for Verification
    Books_Image_xpath = "//img[@id='imgBlkFront']"
    Product_Details_Heading_xpath = "//h2[contains(text(),'Product details')]"
    Review_Product_Heading_xpath = "//h3[@class='a-spacing-micro']"

    """
    ############## Functions of the page ##############
    """
    # Switch to Next Tab
    def switch_to_next_tab(self):
        self.switchTab(1)

    # Checks for the unwanted pop and closes it
    def check_and_closePopUp(self):
        self.wait(5)
        if self.isDisplayed(self.Close_Pop_UP_xpath):
            self.elementClick(self.Close_Pop_UP_xpath)

    # Save Datas from Book Details Page
    def save_datas_from_book_details_page(self):
        i = 1
        for key in self.Type_Price_Dict:
            if self.isDisplayed(key):
                if self.isDisplayed(self.Type_Price_Dict[key]):
                    excel_util.writeData(self.output_sheet, rowNum=i, columnNum=1, data=self.getText(key))
                    excel_util.writeData(self.output_sheet, rowNum=i, columnNum=2, data=self.getText(self.Type_Price_Dict[key]))
                    i += 1
                else:
                    excel_util.writeData(self.output_sheet, rowNum=i, columnNum=1, data=self.getText(key))
                    excel_util.writeData(self.output_sheet, rowNum=i, columnNum=2, data="Price Unavailable Right Now")
                    i += 1

        for j in range(0, len(self.Misc_Details_list)):
            excel_util.writeData(self.output_sheet, rowNum=i, columnNum=1, data=self.getText(self.Misc_Details_list[j]).split(": ")[0])
            excel_util.writeData(self.output_sheet, rowNum=i, columnNum=2, data=self.getText(self.Misc_Details_list[j]).split(": ")[1])
            i += 1
    """
    ############## Verification Function of the page ##############
    """

    # Checks for Book Image in Book Details page
    def verify_book_image(self):
        return self.isDisplayed(self.Books_Image_xpath)

    # Checks for Product Details Header in Book Details page
    def verify_product_details_heading(self):
        return self.isDisplayed(self.Product_Details_Heading_xpath)

    # Checks for Review Product Header in Book Details page
    def verify_review_product_heading(self):
        return self.isDisplayed(self.Review_Product_Heading_xpath)
