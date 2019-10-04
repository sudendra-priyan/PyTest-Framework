from utilities.verify_status import VerifyStatus
from pages.home_page import AmazonHome
import pytest
import unittest

# Accessing fixture from conftest.py file
@pytest.mark.usefixtures("baseSetUp")
class SaveBookDetails(unittest.TestCase):

    # Base level Set up for our test, Instantiating the required classes for test
    @pytest.fixture(autouse=True)
    def classSetup(self, baseSetUp):
        self.driver = AmazonHome(self.driver)
        self.ts = VerifyStatus(self.driver)

    # Searches for the book
    @pytest.mark.run(order=1)
    def test_search_book(self):

        self.driver.choose_book_category()

        """
        Once We search for a category in amazon, It gives you a Navigation bar for that particular category. Since we 
        choose books. I have Checked If "Book " is displayed in the Navigation Bar.
        """
        Book_Bar = self.driver.verify_books_navigation_bar_tab()
        self.ts.singleAssertion(Book_Bar, "Books option did not appear")

        """
        Just like Navigation bar appearing after search, There will be a Link indicating the searched category. In our 
        case it books. Hence I have checked for "Books" link.  
        """
        Book_Link = self.driver.verify_books_post_search_link()
        self.ts.finalAssertion("Assertions For Search Books Page ", Book_Link, "Books Link did not appear")

    # Searches for the book
    @pytest.mark.run(order=2)
    def test_goto_book_details_page_and_save_data(self):
        self.driver.select_first_search_result()
        self.driver.book_details.switch_to_next_tab()
        self.driver.book_details.check_and_closePopUp()
        self.driver.book_details.save_datas_from_book_details_page()

        """
        Every Book Details Page will contain Book's image element in it. Hence i have checked for the Book Image 
        element here. 
        """
        Book_Image = self.driver.book_details.verify_book_image()
        self.ts.singleAssertion(Book_Image, "Book Image is not displayed")

        """
        Every Book Details Page will have Product Detail Header in it. Hence i have checked for the Product Details 
        header element here
        """
        Product_Detail = self.driver.book_details.verify_product_details_heading()
        self.ts.singleAssertion(Product_Detail, "Product Detail header is not displayed")

        """
        Every Book Details Page will have Review the Product header in it. Hence i have checked for the Review Product  
        header element here
        """
        Review_Product = self.driver.book_details.verify_review_product_heading()
        self.ts.finalAssertion("Assertions For Search Books Page ", Review_Product, "Review Product header is not displayed")
