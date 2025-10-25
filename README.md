# 🚀 Automatización de Pruebas con Selenium & Pytest

Este proyecto contiene un *test* automatizado para validar la funcionalidad de inicio de sesión en la aplicación web **SauceDemo**. El objetivo es demostrar la configuración inicial de un proyecto de automatización de pruebas con Python.

***

## 🛠️ Configuración del Proyecto

### 1. Requisitos Previos

Asegúrate de tener instalado **Python 3.x**.

También necesitarás el *driver* de tu navegador (ej. `chromedriver.exe` para Chrome).

### 2. Instalación de Dependencias

Todas las librerías necesarias para ejecutar los *tests* se encuentran especificadas en el archivo `requirements.txt`. Para instalarlas, usa el siguiente comando en tu terminal:

```bash
pip install -r requirements.txt
```

### Dependencias Clave:

pytest: Framework principal para la ejecución de pruebas.

selenium: Librería para la automatización de navegadores.

***

## 🏃 Ejecución de Pruebas

Para ejecutar el conjunto de pruebas y ver la salida de los mensajes de la prueba (los print()), utiliza el siguiente comando desde la raíz del proyecto.

Comando de Ejecución
Utilizamos las banderas -v (verbose, para ver detalles por prueba) y -s (para ver la salida de los print()):

```bash
python -m pytest tests/login-test.py -v -s
```

***

## 📁 Estructura del Proyecto
```
.
├── tests/
│   └── login-test.py   # Script principal con la prueba de login
├── README.md           # Este archivo de documentación
└── requirements.txt    # Lista de dependencias de Python
```