from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

# def test_ownprep_login_and_dropdown():
#     options = webdriver.ChromeOptions()
#     # Headless removed so window will open visibly
    
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
#     driver.maximize_window()
#     driver.get("http://3.6.185.230/")
#     time.sleep(1)

#     login_link = driver.find_element(By.XPATH, "//a[@href='/auth?mode=login' and text()='Log In']")
#     login_link.click()
#     time.sleep(1)

#     student_button = driver.find_element(By.XPATH, "//button[text()='Student']")
#     student_button.click()
#     time.sleep(1)

#     phone_input = driver.find_element(By.NAME, "phone")
#     phone_input.send_keys("9021814639")
#     time.sleep(1)

#     password_input = driver.find_element(By.NAME, "password")
#     password_input.send_keys("1234567")
#     time.sleep(1)

#     login_submit_btn = driver.find_element(By.XPATH, "//button[@type='submit' and text()='Log In']")
#     login_submit_btn.click()
#     time.sleep(1)

#     driver.get("http://3.6.185.230/learn")
#     time.sleep(3)

#     scroll_height = driver.execute_script("return document.body.scrollHeight")
#     current_position = 0
#     step = 300
#     while current_position < scroll_height:
#         driver.execute_script(f"window.scrollBy(0, {step});")
#         current_position += step
#         time.sleep(0.5)
#     time.sleep(3)

#     driver.execute_script("window.scrollTo(0, 0);")
#     time.sleep(2)

#     try:
#         dropdown = driver.find_element(By.XPATH, "//select[contains(@class, 'pl-10')]")
#         select = Select(dropdown)
#         options = [option.text.strip().lower() for option in select.options]
#         if "computer science" in options:
#             select.select_by_visible_text("Computer Science")
#             print("Dropdown option 'Computer Science' selected.")
#         elif "aptitude" in options:
#             select.select_by_visible_text("Aptitude")
#             print("Dropdown option 'Aptitude' selected.")
#         elif "all" in options:
#             select.select_by_visible_text("All")
#             print("Dropdown option 'All' selected.")
#         else:
#             print("No matching dropdown option found!")
#     except NoSuchElementException:
#         print("Dropdown not found!")

#     time.sleep(2)

    # try:
    #     result = driver.find_element(By.XPATH, "//div[contains(text(), 'Aptitude')]")
    #     print("Course found!")
    # except NoSuchElementException:
    #     print("No results found!")

    # driver.quit()
  

# if __name__ == "__main__":
#     test_ownprep_login_and_dropdown()

# from selenium.webdriver.common.by import By
#
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.username_input = (By.ID, "user-name")
#         self.password_input = (By.ID, "password")
#         self.login_button = (By.ID, "login-button")
#         self.error_message = (By.CLASS_NAME, "error-message-container")
#
#     def enter_username(self, username):
#         self.driver.find_element(*self.username_input).send_keys(username)
#
#     def enter_password(self, password):
#         self.driver.find_element(*self.password_input).send_keys(password)
#
#     def click_login(self):
#         self.driver.find_element(*self.login_button).click()
#
#     def get_error(self):
#         return self.driver.find_element(*self.error_message).text

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


# driver = webdriver.Chrome()
# driver.get("https://petroatl.com/")
# driver.maximize_window()

# profile_button = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, "//button[@class='p-2 rounded-full bg-gray-800 hover:bg-gray-700 transition-colors']//*[name()='svg']"))
# )
# profile_button.click()

# signIn_button = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Sign In']"))
# )
# signIn_button.click()

# driver.find_element(By.ID, "email").send_keys("automation@test.com")
# driver.find_element(By.ID, "password").send_keys("abcd1234")
# driver.find_element(By. XPATH, "//button[@type='submit']").click()

# login_message = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.XPATH, "//div[@role='status']"))
# ).text
# if login_message == "Login successful!":
#     print(f"Login Success Message: {login_message}")
# elif login_message == "Invalid email or password":
#     print(f"Error message: {login_message}")
# else:
#     print("Undefined error")


# product_button = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[@href='/products' and text()='Products']"))
# )
# product_button.click()


# add_to_cart_button = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-3 gap-6']//div[1]//div[1]//div[1]//button[1]"))
# )
# # Scroll the button into view
# driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
# time.sleep(1)  # Wait for the scroll to complete

# # Use JavaScript to click the button
# driver.execute_script("arguments[0].click();", add_to_cart_button)
# add_toCart_message = WebDriverWait(driver, 20).until(
#     EC.visibility_of_element_located((By.XPATH, "//div[@role='status']"))
# ).text
# WebDriverWait(driver, 20).until(
#     EC.invisibility_of_element_located((By.XPATH, "//div[@role='status']"))
# )
# if add_toCart_message == "Product Added to Cart successfully.":
#     print(f"Message after clicking on add to cart button: {add_toCart_message}")

#     # Locate the cart button (parent of the SVG element)
#     cart_icon = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[@class='relative']"))
#     )
#     # Click the cart button
#     cart_icon.click()
#     try:
#         empty_cart_text = WebDriverWait(driver, 7).until(
#             EC.visibility_of_element_located((
#                 By.XPATH,"//h2[@class='text-xl sm:text-2xl font-bold mb-2 sm:mb-4' and text()='Your Cart is Empty']"))).text

#         if empty_cart_text == "Your Cart is Empty":
#             print("Product Has not been added to the cart")
#     except TimeoutException as e:
#         print("Cart status: Product has been added to the cart")

#     proceed_to_checkout_button = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((
#             By.XPATH, "//a[@class='block w-full bg-teal-600 text-white text-center py-3 rounded-lg hover:bg-teal-700' and @href='/checkout' and text()= 'Proceed to Checkout']"
#         ))
#     )
#     proceed_to_checkout_button.click()

#     continue_button = WebDriverWait(driver, 15).until(
#         EC.element_to_be_clickable((
#             By.XPATH, "//button[@class='w-full bg-teal-600 text-white py-3 rounded-lg hover:bg-teal-700' and text()='Continue']"
#         ))
#     )
#     continue_button.click()

#     address_radio_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
#         By.XPATH, "//input[@type='radio' and @name='deliveryAddress']"
#     )))
#     address_radio_button.click()

#     checkout_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
#         By.XPATH, "//button[@class='w-full py-3 rounded-lg bg-teal-600 hover:bg-teal-700 text-white' and text()='Checkout']"
#     )))
#     checkout_button.click()

#     placeOrder_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
#         By.XPATH, "//button[@class=' mt-2 w-full bg-teal-600 text-white py-3 rounded-lg hover:bg-teal-700' and text()='Place Order']")))
#     placeOrder_button.click()

#     email_field_in_PayLink = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='CheckoutInput Input Input--empty' and @id='email']")))
#     email_field_in_PayLink.send_keys("automation@test.com")

#     driver.find_element(By.XPATH, "//input[@class='CheckoutInput CheckoutInput--tabularnums Input Input--empty' and contains(@placeholder, '1234 1234 1234 1234')]").send_keys("371449635398431") # card details taken from demo card
#     driver.find_element(By.XPATH, "//input[@class='CheckoutInput CheckoutInput--tabularnums Input Input--empty' and contains(@placeholder, 'MM / YY')]").send_keys("0330") # card details taken from demo card
#     driver.find_element(By.XPATH, "//input[@class='CheckoutInput CheckoutInput--tabularnums Input Input--empty' and contains(@placeholder, 'CVC')]").send_keys("7373") # card details taken from demo card
#     driver.find_element(By.XPATH, "//input[@class='CheckoutInput Input Input--empty' and contains(@placeholder, 'Full name on card')]").send_keys("Automation User") # card details taken from demo card

#     # countryDropdown = Select(driver.find_element(By.ID, "billingCountry"))
#     # countryDropdown.select_by_value("India")

#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #Scroll to the bottom of the page

#     payButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='hosted-payment-submit-button']")))
#     driver.execute_script("arguments[0].click();", payButton)
#     try:
#         orderSuccessfullScreen_Text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[@class='mt-2 text-sm sm:text-base text-gray-600' and text()='Your order has been successfully placed.']"))).text
#         if orderSuccessfullScreen_Text == "Your order has been successfully placed.":
#             print("Order has been Placed successfully")

#             # Take a screenshot
#             driver.save_screenshot("screenshots/order_successful.png")
#             print("Screenshot saved as 'order_successful.png'")
#         else:
#             print("Order has not been placed")
#     except TimeoutException:
#         print("Order has not been placed")
#         # Take a screenshot
#         driver.save_screenshot("order_error.png")
#         print("Screenshot saved as 'order_error.png'")
#     time.sleep(5)
# else:
#     print(f"Message after clicking on add to cart button: {add_toCart_message}")


# time.sleep(5)
# driver.quit()


import time
import pytest  # ✅ Add this

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

def test_login_workflow():  
    driver = webdriver.Chrome()
    driver.get("https://petroatl.com/")
    driver.maximize_window()

    profile_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='p-2 rounded-full bg-gray-800 hover:bg-gray-700 transition-colors']//*[name()='svg']"))
    )
    profile_button.click()

    signIn_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Sign In']"))
    )
    signIn_button.click()

    driver.find_element(By.ID, "email").send_keys("automation@test")
    driver.find_element(By.ID, "password").send_keys("abcd1234")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    login_message = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='status']"))
    ).text

    assert login_message in ["Login successful!", "Invalid email or password"], "Unexpected login message"

    if login_message == "Login successful!":
        print(f"Login Success Message: {login_message}")
    elif login_message == "Invalid email or password":
        print(f"Error message: {login_message}")
    else:
        print("Undefined error")

    # ➕ rest of the code continues...
    
    product_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='/products' and text()='Products']"))
    )
    product_button.click()


    add_to_cart_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[@class='grid grid-cols-1 md:grid-cols-3 gap-6']//div[1]//div[1]//div[1]//button[1]"))
    )
    # Scroll the button into view
    driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
    time.sleep(1)  # Wait for the scroll to complete

    # Use JavaScript to click the button
    driver.execute_script("arguments[0].click();", add_to_cart_button)
    add_toCart_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@role='status']"))
    ).text
    WebDriverWait(driver, 20).until(
        EC.invisibility_of_element_located((By.XPATH, "//div[@role='status']"))
    )
    if add_toCart_message == "Product Added to Cart successfully.":
        print(f"Message after clicking on add to cart button: {add_toCart_message}")

        # Locate the cart button (parent of the SVG element)
        cart_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='relative']"))
        )
        # Click the cart button
        cart_icon.click()
        try:
            empty_cart_text = WebDriverWait(driver, 7).until(
                EC.visibility_of_element_located((
                    By.XPATH,"//h2[@class='text-xl sm:text-2xl font-bold mb-2 sm:mb-4' and text()='Your Cart is Empty']"))).text

            if empty_cart_text == "Your Cart is Empty":
                print("Product Has not been added to the cart")
        except TimeoutException as e:
            print("Cart status: Product has been added to the cart")

        proceed_to_checkout_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((
                By.XPATH, "//a[@class='block w-full bg-teal-600 text-white text-center py-3 rounded-lg hover:bg-teal-700' and @href='/checkout' and text()= 'Proceed to Checkout']"
            ))
        )
        proceed_to_checkout_button.click()

        continue_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((
                By.XPATH, "//button[@class='w-full bg-teal-600 text-white py-3 rounded-lg hover:bg-teal-700' and text()='Continue']"
            ))
        )
        continue_button.click()

        address_radio_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, "//input[@type='radio' and @name='deliveryAddress']"
        )))
        address_radio_button.click()

        checkout_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class='w-full py-3 rounded-lg bg-teal-600 hover:bg-teal-700 text-white' and text()='Checkout']"
        )))
        checkout_button.click()

        placeOrder_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, "//button[@class=' mt-2 w-full bg-teal-600 text-white py-3 rounded-lg hover:bg-teal-700' and text()='Place Order']")))
        placeOrder_button.click()

        email_field_in_PayLink = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='CheckoutInput Input Input--empty' and @id='email']")))
        email_field_in_PayLink.send_keys("automation@test.com")

        driver.find_element(By.XPATH, "//input[@class='CheckoutInput CheckoutInput--tabularnums Input Input--empty' and contains(@placeholder, '1234 1234 1234 1234')]").send_keys("371449635398431") # card details taken from demo card
        driver.find_element(By.XPATH, "//input[@class='CheckoutInput CheckoutInput--tabularnums Input Input--empty' and contains(@placeholder, 'MM / YY')]").send_keys("0330") # card details taken from demo card
        driver.find_element(By.XPATH, "//input[@class='CheckoutInput CheckoutInput--tabularnums Input Input--empty' and contains(@placeholder, 'CVC')]").send_keys("7373") # card details taken from demo card
        driver.find_element(By.XPATH, "//input[@class='CheckoutInput Input Input--empty' and contains(@placeholder, 'Full name on card')]").send_keys("Automation User") # card details taken from demo card

        # countryDropdown = Select(driver.find_element(By.ID, "billingCountry"))
        # countryDropdown.select_by_value("India")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #Scroll to the bottom of the page

        payButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='hosted-payment-submit-button']")))
        driver.execute_script("arguments[0].click();", payButton)
        try:
            orderSuccessfullScreen_Text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[@class='mt-2 text-sm sm:text-base text-gray-600' and text()='Your order has been successfully placed.']"))).text
            if orderSuccessfullScreen_Text == "Your order has been successfully placed.":
                print("Order has been Placed successfully")

                # Take a screenshot
                driver.save_screenshot("screenshots/order_successful.png")
                print("Screenshot saved as 'order_successful.png'")
            else:
                print("Order has not been placed")
        except TimeoutException:
            print("Order has not been placed")
            # Take a screenshot
            driver.save_screenshot("order_error.png")
            print("Screenshot saved as 'order_error.png'")
        time.sleep(5)
    else:
        print(f"Message after clicking on add to cart button: {add_toCart_message}")


    time.sleep(5)
    driver.quit()

