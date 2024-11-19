import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Mettre à jour un produit dans Magento")
@allure.description("Test pour mettre à jour les détails d'un produit via l'interface d'administration Magento.")
def test_update_product():
    # Configuration du WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Exécution en mode headless pour CI/CD
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    try:
        with allure.step("Connexion à l'interface d'administration"):
            driver.get("http://mage2rock.magento.com/admin")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("rockadmin")
            driver.find_element(By.ID, "login").send_keys("Admin@123456")
            driver.find_element(By.XPATH, "//button[contains(@class, 'action-login') and span[text()='Sign in']]").click()

            # Vérification de la connexion
            assert "Dashboard" in driver.title, "Connexion échouée"
            allure.attach(driver.get_screenshot_as_png(), name="Dashboard", attachment_type=allure.attachment_type.PNG)

        with allure.step("Navigation vers la liste des produits"):
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Catalog']"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Products']"))).click()

        with allure.step("Recherche du produit à mettre à jour"):
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "fulltext"))).clear()
            driver.find_element(By.ID, "fulltext").send_keys("Produit Test")
            driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div[1]/div[5]/button').click()

        with allure.step("Sélection du produit dans les résultats de recherche"):
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[4]/table/tbody/tr/td[15]/a'))
            ).click()

        with allure.step("Mise à jour des détails du produit"):
            # Mettre à jour le nom du produit
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "product[name]"))).clear()
            driver.find_element(By.NAME, "product[name]").send_keys("Produit Test Updated")

            # Mettre à jour le prix
            driver.find_element(By.NAME, "product[price]").clear()
            driver.find_element(By.NAME, "product[price]").send_keys("119.99")

            # Mettre à jour la quantité
            driver.find_element(By.NAME, "product[quantity_and_stock_status][qty]").clear()
            driver.find_element(By.NAME, "product[quantity_and_stock_status][qty]").send_keys("15")

        with allure.step("Sauvegarde du produit mis à jour"):
            driver.find_element(By.XPATH, "//button[@title='Save']").click()

        with allure.step("Vérification du message de succès"):
            success_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'message-success')]"))
            )
            assert "You saved the product." in success_message.text, "Le produit n'a pas été mis à jour avec succès"
            allure.attach(driver.get_screenshot_as_png(), name="Produit Mis à Jour", attachment_type=allure.attachment_type.PNG)

        print("Test réussi : Le produit a été mis à jour avec succès.")

    finally:
        driver.quit()
