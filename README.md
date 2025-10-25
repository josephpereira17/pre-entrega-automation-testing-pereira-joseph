# 🚀 Automatización de Pruebas con Selenium & Pytest

Este proyecto contiene un *test* automatizado para validar la funcionalidad de inicio de sesión en la aplicación web **SauceDemo**. El objetivo es demostrar la configuración inicial de un proyecto de automatización de pruebas con Python.

***

## 🛠️ Configuración del Proyecto

### 1. Requisitos Previos

Asegúrate de tener instalado **Python 3.x**.

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
├── pages/
│   └── base_page.py    # Clase Base: Contiene la lógica del WebDriver, esperas y métodos comunes.
├── tests/
│   └── login-test.py   # Script de Prueba: Contiene la fixture del driver y el caso de prueba.
├── .gitignore          # Archivo para ignorar compilaciones de Python y logs.
├── README.md           # Documentación del proyecto.
└── requirements.txt    # Lista de dependencias de Python.
```