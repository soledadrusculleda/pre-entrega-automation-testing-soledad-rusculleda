
# Pre-entrega - Automation Testing

## Descripción del proyecto

Este proyecto consiste en automatizar pruebas funcionales de la aplicación web **SauceDemo** utilizando Python, Selenium WebDriver y Pytest.

El objetivo es validar funcionalidades principales de la aplicación, como el inicio de sesión, la visualización del catálogo de productos y la interacción con el carrito de compras.

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- pytest-html
- Google Chrome
- Visual Studio Code
- Git y GitHub

## Sitio utilizado

**SauceDemo:** https://www.saucedemo.com/

### Credenciales de prueba

- **Usuario:** `standard_user`
- **Contraseña:** `secret_sauce`

Estas credenciales son públicas y están destinadas a realizar pruebas en SauceDemo.

## Casos de prueba automatizados

### TC-01 - Login exitoso

- Ingresar a SauceDemo.
- Completar usuario y contraseña válidos.
- Verificar la redirección a `/inventory.html`.
- Validar el título **Products** y el logo **Swag Labs**.

### TC-02 - Catálogo de productos

- Verificar que se muestre el título **Products**.
- Comprobar la presencia de productos en el catálogo.
- Obtener el nombre y precio del primer producto.
- Validar la presencia del menú y del filtro de productos.

### TC-03 - Agregar producto al carrito

- Iniciar sesión con credenciales válidas.
- Seleccionar el primer producto del catálogo.
- Agregarlo al carrito.
- Verificar que el contador indique **1**.
- Ingresar al carrito.
- Comprobar que el producto agregado coincida con el seleccionado.

## Instalación

Clonar el repositorio o descargar el proyecto.

Crear un entorno virtual:

```bash
python3 -m venv .venv
```

Activar el entorno virtual en macOS:

```bash
source .venv/bin/activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución de pruebas

Ejecutar los tres casos de prueba:

```bash
python -m pytest tests/test_saucedemo.py -v
```

Generar el reporte HTML:

```bash
python -m pytest tests/test_saucedemo.py -v --html=reporte.html --self-contained-html
```

## Reporte de ejecución

El proyecto utiliza **pytest-html** para generar un reporte con los resultados de las pruebas automatizadas.

El archivo `reporte.html` permite consultar los casos ejecutados y sus resultados.

En la ejecución de validación realizada para esta preentrega se obtuvo el siguiente resultado:

**3 tests passed.**

## Estructura del proyecto

```text
pre-entrega-automation-testing/
├── tests/
│   └── test_saucedemo.py
├── utils/
│   └── helpers.py
├── .gitignore
├── README.md
├── requirements.txt
└── reporte.html
```

- **tests/**: contiene los casos de prueba automatizados.
- **utils/**: contiene funciones auxiliares reutilizables, como el inicio de sesión.
- **requirements.txt**: contiene las dependencias del proyecto.
- **reporte.html**: contiene el reporte HTML de ejecución.
- **.gitignore**: evita incluir archivos innecesarios en el repositorio.

## Resultados

Se automatizaron tres casos de prueba funcionales utilizando Selenium WebDriver y Pytest, validando el inicio de sesión, el catálogo de productos y el carrito de compras de SauceDemo.