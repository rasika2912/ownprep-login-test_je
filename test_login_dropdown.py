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

#     try:
#         result = driver.find_element(By.XPATH, "//div[contains(text(), 'Aptitude')]")
#         print("Course found!")
#     except NoSuchElementException:
#         print("No results found!")

#     driver.quit()

# # Close browser
# driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up driver
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# Navigate to the login page
driver.get("http://3.6.185.230/")
time.sleep(1)

# Click on the login link
driver.find_element(By.XPATH, "//a[contains(@href, '/auth?mode=login') and contains(text(),'Log In')]").click()
time.sleep(1)

# Click on the student button
driver.find_element(By.XPATH, "//button[text()='Student']").click()
time.sleep(1)

# Enter mobile number
driver.find_element(By.NAME, "phone").send_keys("9021814639")  # Replace with test number
time.sleep(1)

# Enter password
driver.find_element(By.NAME, "password").send_keys("1234567")  # Replace with test password
time.sleep(1)

# Click on the login button
driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(),'Log In')]").click()
time.sleep(1)

# Click on Top Recruiters
driver.find_element(By.XPATH, "//div[text()='Top Recruiters']").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Go to courses page
driver.get("http://3.6.185.230/courses")
time.sleep(2)

# Search course
search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search courses...']")
search_box.send_keys("Data Structures & Algorithms")
search_box.send_keys(Keys.ENTER)
time.sleep(2)

# Wait for course card
wait.until(EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Data Structures & Algorithms')]")))
time.sleep(1)

# Click Enroll Now button
enroll_button = driver.find_element(By.XPATH,
    "//h3[contains(text(), 'Data Structures & Algorithms')]/ancestor::div[contains(@class,'p-6')]//a[contains(text(),'Enroll Now')]")
enroll_button.click()
print("Clicked on Enroll Now!")
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Go to jobs page
driver.get("http://3.6.185.230/jobs")
time.sleep(2)

# Select Full-time
select_type = Select(driver.find_element(By.XPATH, "(//select[contains(@class,'appearance-none')])[1]"))
select_type.select_by_value("full-time")
print("Selected 'full-time'")

# Select Pune
select_location = Select(driver.find_element(By.XPATH, "(//select[contains(@class,'appearance-none')])[2]"))
select_location.select_by_value("Pune")
print("Selected 'Pune'")
time.sleep(2)

# Click first "View Details"
driver.find_element(By.XPATH, "(//a[contains(text(),'View Details')])[1]").click()
time.sleep(2)

# Click Wishlist
try:
    wishlist_btn = driver.find_element(By.XPATH, "//button[.//span[contains(text(), 'Wishlist') or contains(text(),'Wishlisted')]]")
    label = wishlist_btn.text.strip()
    if "Wishlisted" in label:
        print("Already wishlisted – skipping.")
    else:
        wishlist_btn.click()
        print("Clicked Wishlist")
        time.sleep(1)
except:
    print("Wishlist button not found")

# Click Apply Now
try:
    apply_btn = driver.find_element(By.XPATH, "//button[text()='Apply Now' or text()='Applied']")
    label = apply_btn.text.strip()
    if "Applied" in label:
        print("Already applied")
    else:
        apply_btn.click()
        print("Clicked Apply Now")
        time.sleep(1)
except:
    print("Apply button not found")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Go to learn page
driver.get("http://3.6.185.230/learn")
time.sleep(2)

# Click filter All
driver.find_element(By.XPATH, "//button[.//span[text()='All']]").click()
time.sleep(1)

# Select Aptitude
driver.find_element(By.XPATH, "//a[text()='Aptitude']").click()
time.sleep(2)

# Validate Aptitude Courses
assert driver.find_element(By.XPATH, "//h3[contains(text(),'Aptitude Foundation Course')]").is_displayed(), "❌ Aptitude Foundation not visible"
assert driver.find_element(By.XPATH, "//h3[contains(text(),'Aptitude Advanced Course')]").is_displayed(), "❌ Aptitude Advanced not visible"
print("✔ Aptitude Courses validated")

# Select Computer Science
driver.find_element(By.XPATH, "//button[.//span[text()='Computer Science']]").click()
time.sleep(2)

# Validate CS Course
assert driver.find_element(By.XPATH, "//h3[contains(text(),'Computer Science Fundamentals')]").is_displayed(), "❌ CS Fundamentals not visible"
print("✔ Computer Science course validated")

# Reset to All
driver.find_element(By.XPATH, "//button[.//span[text()='All']]").click()
time.sleep(2)

# Validate all 3 courses
assert driver.find_element(By.XPATH, "//h3[contains(text(),'Aptitude Foundation Course')]").is_displayed()
assert driver.find_element(By.XPATH, "//h3[contains(text(),'Aptitude Advanced Course')]").is_displayed()
assert driver.find_element(By.XPATH, "//h3[contains(text(),'Computer Science Fundamentals')]").is_displayed()
print("✔ All courses validated under All filter")

# Hover on Learn tab (optional if needed)

# Click Practice Exercise
driver.find_element(By.XPATH, "//a[text()='Practice Exercise']").click()
time.sleep(1)

# Click Practice Test
driver.find_element(By.XPATH, "//a[text()='Practice Test']").click()
time.sleep(1)

# Click Watch & Learn
driver.find_element(By.XPATH, "//a[text()='Watch & Learn']").click()
time.sleep(1)

# Close browser
driver.quit()


if __name__ == "__main__":
    test_ownprep_login_and_dropdown()
