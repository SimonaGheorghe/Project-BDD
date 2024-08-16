# TEST_AUTOMATION_FRAMEWORK_PYTHON_BDD_MAGENTO

##### I conducted tests on various functionalities of the Magento website. I verified the integrity and functionality of the login and registration pages, tested the process of adding products to the shopping cart, and confirmed its proper functioning. Additionally, I explored the news page and tested the search button. During the tests, I ensured that products added to the shopping cart were successfully selected, including specifying the desired size and color.

### Register test:
The automated testing on Magento registration page yielded the following results:
- URL Verification: Confirmed correct URL for the registration page.
- Empty Field Handling: Checked error display for empty mandatory fields.
- Successful Registration: Validated successful registration with correct data.

Overall, tests ensured proper functionality and error handling on the registration page.

### Login test:
The login feature testing on Magento involved the following scenarios:
1. **URL Verification**: Ensured the correct URL for the login page.
2. **Login with Unregistered Email**: Validated error message display for login attempts with unregistered email addresses.

The tests covered essential functionalities and error handling for the login page.

### News test:
In the news feature testing on the Whats New Page of Magento, the following scenario was executed:
- URL Verification**: Ensured that the correct URL for the Whats New page is displayed.
- Wish List Verification**: Ensured that an item can be added to the Wish List and the success massage is displayed. 
- Add Item To Cart**: Ensured that the item added before to the Wish List can not be added to cart without selecting the color and the size


This scenario validates that the page is correctly loaded with the expected URL, ensuring users are directed to the intended content.

### Search test:
These tests verify the search functionality of the website. Here's a summary:
   - The test begins by entering the keyword "shorts" into the search field.
   - After entering the keyword, the search magnifying button is clicked to initiate the search.
   - The test verifies that the user is redirected to the search results page.
   - Finally, the test verifies that search results are displayed correctly on the page and the review for that item is added successfully.

### Women test: 
The testing for the Women Page on Magento involved the following scenarios:
URL Verification: Ensured that the user is correctly navigated to the Women page by verifying that the URL is "https://magento.softwaretestingboard.com/women.html".
Navigation to Women's Tees Section: Tested the functionality of the "Women’s Tees" button by verifying that clicking the button redirects the user to the Tees page. The expected URL for this page is "https://magento.softwaretestingboard.com/women/tops-women/tees-women.html".
These tests covered the basic navigation and URL validation for the Women Page, ensuring that users can access specific sections of the website correctly.

### Cart test: 
- Adding an Item to the Cart:
Verified that the user can successfully select a product ("Desiree Fitness Tee"), choose its size and color, add it to the cart, and view the cart details.
Ensured that any applicable discounts are correctly displayed in the cart.
- Placing the Order:
Confirmed the user can enter their shipping details, select a shipping method, and proceed through the checkout process.
Verified that the user is redirected to the correct success order page with the appropriate confirmation message displayed.
- Sign Out:
Checked that the user can access the account dropdown, sign out, and see the sign-out confirmation message.

# Summary:
The Test Automation Framework for Python Web supports best testing practices and enhances software development efficiency using the BDD approach. The project includes tests for user registration, login, product management, search functionality, and order processing, with 10 successful test scenarios providing thorough coverage of these key functionalities.