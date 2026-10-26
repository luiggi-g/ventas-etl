# Pipeline ETL de datos de comercio electrónico

Proyecto de ingeniería de datos desarrollado en Python para extraer, validar, limpiar, transformar y cargar datos de clientes y compras de comercio electrónico en PostgreSQL.

Este proyecto forma parte de mi portafolio profesional y tiene como objetivo aplicar buenas prácticas de desarrollo, procesamiento de datos, validación de calidad y organización de pipelines ETL.

## 1. Descripción del proyecto

El proyecto procesa datos sintéticos de comercio electrónico para prepararlos para su almacenamiento y posterior análisis.

El pipeline está organizado en módulos independientes que permiten separar las responsabilidades de extracción, validación, limpieza, transformación y carga.

### Objetivos

- Extraer datos desde archivos CSV.
- Validar el esquema y la calidad de los datos.
- Identificar y tratar inconsistencias en los registros.
- Limpiar cadenas de texto y gestionar registros duplicados.
- Aplicar transformaciones mediante reglas configurables.
- Cargar los datos procesados en una base de datos PostgreSQL.
- Implementar pruebas automatizadas para verificar el comportamiento de los componentes.

## 2. Arquitectura del pipeline

El proyecto sigue el patrón ETL (*Extract, Transform, Load*).

```text
Archivos CSV
     |
     v
Extracción de datos
     |
     v
Validación de esquema y datos
     |
     v
Limpieza de datos
     |
     v
Transformación de datos
     |
     v
Carga en PostgreSQL
```

Cada etapa está separada en módulos para facilitar el mantenimiento, las pruebas y la incorporación de nuevas funcionalidades.

## 3. Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | Desarrollo del pipeline ETL |
| Pandas | Manipulación y procesamiento de datos |
| PostgreSQL | Almacenamiento relacional |
| Psycopg | Conexión entre Python y PostgreSQL |
| python-dotenv | Gestión de variables de entorno |
| pytest | Pruebas automatizadas |
| uv | Gestión de dependencias y entorno de Python |
| Git | Control de versiones |

## 4. Estructura del proyecto

```text
ventas-etl/
├── config/                       # Configuraciones en JSON
├── data/
│   ├── raw/                      # Datos originales locales
│   ├── processed/                # Datos procesados locales
│   └── external/                 # Datos externos locales
├── src/
│   └── ventas_etl/
│       ├── config/               # Lectura de configuraciones
│       ├── extract/              # Extracción de datos
│       ├── transform/            # Validación y transformación
│       └── load/                 # Carga y consultas SQL
├── tests/                        # Pruebas automatizadas
├── main.py                       # Punto de entrada del pipeline
├── pyproject.toml                # Configuración y dependencias
├── uv.lock                       # Versiones bloqueadas
└── README.md                     # Documentación del proyecto
```

## 5. Fuente de los datos

El proyecto utiliza un conjunto de datos sintético de clientes y compras de comercio electrónico.

Entre sus campos se encuentran:

- Identificador del cliente.
- Fecha de compra.
- Categoría del producto.
- Precio y cantidad de los productos.
- Importe total de la compra.
- Método de pago.
- Información demográfica.
- Devoluciones y abandono de clientes (*churn*).

Los archivos utilizados durante el desarrollo son:

- `ecommerce_customer_data_custom_ratios.csv`
- `ecommerce_customer_data_large.csv`

Los archivos CSV originales no se incluyen en el repositorio para mantenerlo ligero. Deben descargarse desde la fuente y colocarse en `data/raw/`.

**Fuente:** [Kaggle — conjunto de datos de comportamiento y compras de clientes de comercio electrónico](https://www.kaggle.com/).

Consulta la página original del conjunto de datos para confirmar el nombre exacto, la versión y las condiciones de uso antes de redistribuirlo.

## 6. Requisitos previos

- Python 3.14, según la versión declarada en `pyproject.toml`.
- [uv](https://docs.astral.sh/uv/).
- PostgreSQL.
- Los archivos CSV requeridos por el pipeline.

## 7. Instalación y configuración

### 7.1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd ventas-etl
```

### 7.2. Instalar las dependencias

```bash
uv sync
```

Este comando crea o sincroniza el entorno virtual e instala las dependencias declaradas en el proyecto.

### 7.3. Preparar los datos

Descarga los archivos CSV desde la fuente original y colócalos en:

```text
data/raw/
```

Verifica que los nombres y las columnas coincidan con los esperados por el pipeline.

### 7.4. Configurar la conexión a PostgreSQL

Crea un archivo `.env` en la raíz del proyecto con las variables de entorno requeridas por la aplicación.

Ejemplo ilustrativo:

```dotenv
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ventas_etl
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
```

Los nombres de las variables deben coincidir con los utilizados en el código de conexión. Sustituye los valores de ejemplo por tu configuración local.

**Importante:** no publiques el archivo `.env`, contraseñas ni otras credenciales. El archivo debe permanecer excluido mediante `.gitignore`.

## 8. Ejecución del pipeline

Desde la raíz del proyecto, ejecuta:

```bash
uv run python main.py
```

El archivo `main.py` actúa como punto de entrada y coordina las etapas del proceso.

El resultado esperado es la ejecución del flujo de procesamiento y la carga de los datos en PostgreSQL, siempre que la configuración, los archivos de entrada y la base de datos estén preparados correctamente.

## 9. Pruebas automatizadas

El proyecto utiliza `pytest` para comprobar el comportamiento de sus componentes.

Ejecutar todas las pruebas:

```bash
uv run pytest -v
```

Ejecutar las pruebas de un módulo específico:

```bash
uv run pytest tests/test_clean_data.py -v
```

Las pruebas permiten verificar comportamientos como la validación del esquema, la detección de valores nulos y la limpieza de cadenas de texto y registros duplicados.

## 10. Configuración del proceso

Las reglas del pipeline se organizan en archivos JSON para separar la configuración de la lógica de procesamiento.

| Archivo | Responsabilidad |
|---|---|
| `ecommerce_schema.json` | Reglas de validación del esquema |
| `ecommerce_cleaning.json` | Reglas de limpieza |
| `ecommerce_transform.json` | Reglas de transformación |
| `ecommerce_load.json` | Configuración de carga |

La estructura busca facilitar los cambios en las reglas sin tener que modificar innecesariamente la lógica de cada módulo.

## 11. Resultados y validación

Esta sección debe incluir resultados obtenidos mediante ejecuciones verificadas del pipeline, por ejemplo:

- Cantidad de registros extraídos.
- Cantidad de registros válidos y rechazados.
- Registros eliminados o corregidos durante la limpieza.
- Cantidad de registros cargados en PostgreSQL.
- Resultado de las pruebas automatizadas.

No se deben asumir cifras ni porcentajes sin comprobarlos con los datos procesados y las salidas reales del programa.

## 12. Mejoras futuras

Entre las posibles mejoras del proyecto se encuentran:

- Incorporar registros estructurados (*logging*) para cada etapa.
- Generar reportes de calidad de datos.
- Implementar un manejo centralizado de errores.
- Mejorar la trazabilidad de registros rechazados.
- Automatizar la ejecución del pipeline.
- Incorporar consultas SQL para analizar tendencias de compra y comportamiento de clientes.
- Añadir integración continua para ejecutar las pruebas automáticamente.

## 13. Estado del proyecto

Proyecto en desarrollo como parte de un portafolio de ingeniería de datos.

Las funcionalidades y los resultados descritos deben contrastarse con la implementación actual antes de considerar una versión como estable.

## 14. Autor

Desarrollado como proyecto práctico de aprendizaje y portafolio profesional en ingeniería de datos.