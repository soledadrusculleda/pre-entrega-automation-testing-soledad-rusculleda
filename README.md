
# Pre-entrega - Automation Testing

## Descripcion del proyecto

Este proyecto consiste en automatizar pruebas funcionales
de la pagina SauceDemo utilizando Python, Selenium y Pytest.

El objetivo es validar el funcionamiento de algunas
funcionalidades principales de la aplicacion.

## Herramientas utilizadas

- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- Google Chrome
- Visual Studio Code

## Casos de prueba

### TC-01 - Login exitoso
- Ingresar a SauceDemo.
- Completar usuario y contraseña validos.
- Verificar el acceso al inventario.
- Validar el titulo Products y el logo Swag Labs.

### TC-02 - Catalogo de productos
- Verificar que se muestren productos.
- Obtener el nombre y precio del primer producto.
- Validar la presencia del menu y filtro de productos.

### TC-03 - Agregar producto al carrito
- Seleccionar el primer producto.
- Agregarlo al carrito.
- Verificar que el contador indique 1.
- Ingresar al carrito y comprobar que el producto aparezca.

## Instalacion

Crear un entorno virtual:

python3 -m venv .venv

Activar el entorno virtual en macOS:

source .venv/bin/activate

Instalar las dependencias:

pip install -r requirements.txt

## Ejecucion de pruebas

Ejecutar todos los tests:

python -m pytest tests/test_saucedemo.py -v

Generar reporte HTML:

python -m pytest tests/test_saucedemo.py -v --html=reporte.html --self-contained-html

## Estructura del proyecto

tests/ - Casos de prueba automatizados

utils/ - Funciones auxiliares

README.md - Documentacion del proyecto

requirements.txt - Dependencias del proyecto
