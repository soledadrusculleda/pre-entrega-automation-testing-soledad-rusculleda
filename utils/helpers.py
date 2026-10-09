
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def iniciar_sesion(driver):
    # Abrir la pagina de SauceDemo
    driver.get("https://www.saucedemo.com/")

    # Completar usuario y contraseña
    usuario = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")

    usuario.send_keys("standard_user")
    password.send_keys("secret_sauce")

    # Hacer click en el boton de login
    driver.find_element(By.ID, "login-button").click()

    # Esperar hasta ingresar al inventario
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/inventory.html"))
