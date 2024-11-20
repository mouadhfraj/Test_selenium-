import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure
from selenium.webdriver.chrome.options import Options


@allure.feature('Magento Admin Panel')
@allure.story('Login and Add Product')
def test_add_product():
    # Set up chromedriver using webdriver_manager
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        # Step 1: Log in
        driver.get("http://mage2rock.magento.com/admin")
        
        # Wait for username field and enter login credentials
        username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        username_field.send_keys("rockadmin")
        
        login_field = driver.find_element(By.ID, "login")
        login_field.send_keys("Admin@123456")
        
        login_button = driver.find_element(By.XPATH, "//button[contains(@class, 'action-login')]")
        login_button.click()

        # Assertion: Check login success by verifying page title
        WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))
        assert "Dashboard" in driver.title, f"Login failed, page title is: {driver.title}"

        # Step 2: Navigate to 'Products' section
        catalog_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Catalog']")))
        catalog_button.click()
        
        products_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Products']")))
        products_button.click()

        # Step 3: Add a new product
        add_product_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Add Product']")))
        add_product_button.click()
        
        product_name_field = driver.find_element(By.NAME, "product[name]")
        product_name_field.send_keys("Test Product")
        
        sku_field = driver.find_element(By.NAME, "product[sku]")
        sku_field.send_keys("TEST123")
        
        price_field = driver.find_element(By.NAME, "product[price]")
        price_field.send_keys("99.99")
        
        quantity_field = driver.find_element(By.NAME, "product[quantity_and_stock_status][qty]")
        quantity_field.send_keys("10")
        
        save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
        save_button.click()

        # Assertion: Check if the success message appears
        success_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'message-success')]")))
        assert "You saved the product." in success_message.text, f"Product not saved successfully. Message: {success_message.text}"

        allure.step("Test Passed - Product added successfully.")
    
    finally:
        # Close the browser
        driver.quit()
