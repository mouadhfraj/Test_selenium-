import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Ajouter un produit dans Magento")
@allure.description("Test pour ajouter un produit dans Magento via l'interface d'administration")
def test_add_product():
    # Configuration du WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Mode headless pour CI/CD
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    try:
        with allure.step("Connexion à l'interface d'administration"):
            driver.get("http://mage2rock.magento.com/admin")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("rockadmin")
            driver.find_element(By.ID, "login").send_keys("Admin@123456")
            driver.find_element(By.XPATH, "//button[contains(@class, 'action-login') and span[text()='Sign in']]").click()

            # Assertion pour vérifier la connexion
            assert "Dashboard" in driver.title, "Connexion échouée"
            allure.attach(driver.get_screenshot_as_png(), name="Dashboard", attachment_type=allure.attachment_type.PNG)

        with allure.step("Navigation vers Produits"):
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Catalog']"))).click()
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Products']"))).click()

            # Vérification que la page Produits est affichée
            page_heading = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Products']")))
            assert page_heading.is_displayed(), "La page Produits n'est pas affichée"
            allure.attach(driver.get_screenshot_as_png(), name="Page Produits", attachment_type=allure.attachment_type.PNG)

        with allure.step("Ajout d'un nouveau produit"):
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Add Product']"))).click()

            # Remplir les informations du produit
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "product[name]"))).send_keys("Produit Test")
            driver.find_element(By.NAME, "product[sku]").send_keys("TEST123")
            driver.find_element(By.NAME, "product[price]").send_keys("99.99")
            driver.find_element(By.NAME, "product[quantity_and_stock_status][qty]").send_keys("10")

            # Sauvegarder le produit
            driver.find_element(By.XPATH, "//button[@title='Save']").click()

        with allure.step("Vérification que le produit est ajouté"):
            success_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'message-success')]"))
            )
            assert "You saved the product." in success_message.text, "Le produit n'a pas été enregistré avec succès"
            allure.attach(driver.get_screenshot_as_png(), name="Produit Ajouté", attachment_type=allure.attachment_type.PNG)

        print("Test réussi : le produit a été ajouté correctement.")

    finally:
        driver.quit()
