from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select


def test_ownprep_login_and_dropdown():
    options = webdriver.ChromeOptions()
    # Headless removed so window will open visibly
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.get("http://3.6.185.230/")
    time.sleep(1)

    login_link = driver.find_element(By.XPATH, "//a[@href='/auth?mode=login' and text()='Log In']")
    login_link.click()
    time.sleep(1)

    student_button = driver.find_element(By.XPATH, "//button[text()='Student']")
    student_button.click()
    time.sleep(1)

    phone_input = driver.find_element(By.NAME, "phone")
    phone_input.send_keys("9021814639")
    time.sleep(1)

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("1234567")
    time.sleep(1)

    login_submit_btn = driver.find_element(By.XPATH, "//button[@type='submit' and text()='Log In']")
    login_submit_btn.click()
    time.sleep(1)

    driver.get("http://3.6.185.230/learn")
    time.sleep(3)

    scroll_height = driver.execute_script("return document.body.scrollHeight")
    current_position = 0
    step = 300
    while current_position < scroll_height:
        driver.execute_script(f"window.scrollBy(0, {step});")
        current_position += step
        time.sleep(0.5)
    time.sleep(3)

    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)

    try:
        dropdown = driver.find_element(By.XPATH, "//select[contains(@class, 'pl-10')]")
        select = Select(dropdown)
        options = [option.text.strip().lower() for option in select.options]
        if "computer science" in options:
            select.select_by_visible_text("Computer Science")
            print("Dropdown option 'Computer Science' selected.")
        elif "aptitude" in options:
            select.select_by_visible_text("Aptitude")
            print("Dropdown option 'Aptitude' selected.")
        elif "all" in options:
            select.select_by_visible_text("All")
            print("Dropdown option 'All' selected.")
        else:
            print("No matching dropdown option found!")
    except NoSuchElementException:
        print("Dropdown not found!")

    time.sleep(2)

    try:
        result = driver.find_element(By.XPATH, "//div[contains(text(), 'Aptitude')]")
        print("Course found!")
    except NoSuchElementException:
        print("No results found!")
    time.sleep(1)
        
    driver.get("http://3.6.185.230/courses")
    time.sleep(1)

    driver.quit()

if __name__ == "__main__":
    test_ownprep_login_and_dropdown()
