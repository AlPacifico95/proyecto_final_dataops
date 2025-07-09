# Proyecto Final - DataOps

Este proyecto realiza un proceso ETL con Python, automatizado mediante Jenkins usando contenedores Docker.

## ¿Qué hace?

- Lee un archivo `ventas.csv` con datos de ventas
- Agrupa por categoría
- Calcula:
  - la suma total de ventas
  - el promedio por categoría
  - y el número de registros por categoría

## Herramientas utilizadas

- Python 3.11
- Pandas
- Jenkins
- Docker
- Git y GitHub

## ¿Cómo se automatizó?

1. Se construyó una imagen Docker que instala Python y Pandas.
2. El contenedor Jenkins ejecuta un pipeline que:
   - Navega a `/home/scripts`
   - Ejecuta `etl.py` automáticamente
3. Se visualiza el resultado en la consola de Jenkins.

##  Cómo ejecutar el pipeline

- Abrir Jenkins desde Docker (`localhost:8080`)
- Ir al proyecto `proyecto_parcial_dataops`
- Hacer clic en **"Build Now"**

## Autor

**Alberto Pacífico**  
Certus - DataOps