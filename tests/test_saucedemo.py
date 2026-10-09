
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import iniciar_sesion


# TEST 1 - LOGIN EXITOSO

def test_login_exitoso():
    # Abrir navegador Chrome
    driver = webdriver.Chrome()

    try:
        # Ingresar a SauceDemo con usuario valido
        iniciar_sesion(driver)

        # Validar que ingresamos al inventario
        assert "/inventory.html" in driver.current_url

        # Verificar logo de la pagina
        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        assert logo.text == "Swag Labs"

        # Verificar titulo de productos
        titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
        assert titulo.text == "Products"

    finally:
        # Cerrar navegador
        driver.quit()


# TEST 2 - VERIFICAR CATALOGO DE PRODUCTOS

def test_catalogo_productos():
    driver = webdriver.Chrome()

    try:
        # Iniciar sesion
        iniciar_sesion(driver)

        # Verificar titulo del inventario
        titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
        assert titulo.text == "Products"

        # Esperar hasta que aparezcan los productos
        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item")
            )
        )

        # Buscar productos disponibles
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")

        # Validar que exista al menos un producto visible
        assert len(productos) > 0
        assert productos[0].is_displayed()

        # Obtener nombre y precio del primer producto
        primer_producto = productos[0]

        nombre = primer_producto.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text

        precio = primer_producto.find_element(
            By.CLASS_NAME, "inventory_item_price"
        ).text

        # Validar nombre y precio
        assert nombre != ""
        assert precio.startswith("$")

        print("Primer producto:", nombre)
        print("Precio:", precio)

        # Verificar menu y filtro de productos
        menu = driver.find_element(By.ID, "react-burger-menu-btn")
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

        assert menu.is_displayed()
        assert filtro.is_displayed()

    finally:
        driver.quit()


# TEST 3 - AGREGAR PRODUCTO AL CARRITO

def test_agregar_producto_carrito():
    driver = webdriver.Chrome()

    try:
        # Iniciar sesion
        iniciar_sesion(driver)

        wait = WebDriverWait(driver, 10)

        # Buscar el primer producto
        primer_producto = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item")
            )
        )

        # Guardar el nombre del producto
        nombre_producto = primer_producto.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text

        # Agregar producto al carrito
        boton_agregar = primer_producto.find_element(
            By.CSS_SELECTOR, "button"
        )
        boton_agregar.click()

        # Verificar que el contador del carrito sea 1
        contador = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "shopping_cart_badge")
            )
        )

        assert contador.text == "1"

        # Ingresar al carrito
        driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        ).click()

        # Esperar a que cargue el carrito
        wait.until(EC.url_contains("/cart.html"))

        # Verificar que el producto aparezca en el carrito
        producto_carrito = driver.find_element(
            By.CLASS_NAME, "inventory_item_name"
        )

        assert producto_carrito.text == nombre_producto

        print("Producto agregado correctamente:", nombre_producto)

    finally:
        driver.quit()
