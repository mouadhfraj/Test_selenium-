import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.feature('Magento Admin Panel')
@allure.story('Login and Add Product')
def test_add_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        # Step 1: Log in
        driver.get("http://mage2rock.magento.com/admin")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("rockadmin")
        driver.find_element(By.ID, "login").send_keys("Admin@123456")
        driver.find_element(By.XPATH, "//button[contains(@class, 'action-login')]").click()

        # Assertion: Check login success
        assert "Dashboard" in driver.title, "Login failed"

        # Step 2: Navigate to 'Products' section
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Catalog']"))).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Products']"))).click()

        # Step 3: Add a new product
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Add Product']"))).click()
        driver.find_element(By.NAME, "product[name]").send_keys("Test Product")
        driver.find_element(By.NAME, "product[sku]").send_keys("TEST123")
        driver.find_element(By.NAME, "product[price]").send_keys("99.99")
        driver.find_element(By.NAME, "product[quantity_and_stock_status][qty]").send_keys("10")
        driver.find_element(By.XPATH, "//button[@title='Save']").click()

        # Assertion: Check product was added
        success_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'message-success')]")))
        assert "You saved the product." in success_message.text, "Product not saved successfully"

        allure.step("Test Passed - Product added successfully.")
    
    finally:
        driver.quit()
