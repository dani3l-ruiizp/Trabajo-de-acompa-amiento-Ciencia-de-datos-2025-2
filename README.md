## Análisis de registros sanitarios de medicamentos homeopáticos en Colombia

# Descripción del proyecto

Este proyecto realiza un análisis exploratorio, estadístico y visual de los registros sanitarios de medicamentos homeopáticos en Colombia, con el objetivo de caracterizar su distribución, estado regulatorio y principales características reportadas ante la autoridad sanitaria.

El análisis se desarrolla en el contexto de las Ciencias Farmacéuticas, con énfasis en la regulación, vigilancia sanitaria y disponibilidad de medicamentos homeopáticos en el país, aportando información relevante para la comprensión del mercado y su control normativo.

# Origen de los datos

  - Nombre del conjunto de datos: Registros sanitarios de medicamentos homeopáticos
  - Plataforma: Datos Abiertos Colombia
  - Entidad responsable: INVIMA
  - URL del conjunto de datos:
https://www.datos.gov.co/Salud-y-Protecci-n-Social/REGISTROS-SANITARIOS-DE-MEDICAMENTOS-HOMEOP-TICOS/avxp-njm3/about_data
  - Fecha de descarga: 2025
  - Formato original: CSV

# Descripción del conjunto de datos

El conjunto de datos contiene información oficial sobre los medicamentos homeopáticos que cuentan o han contado con registro sanitario en Colombia. Incluye variables como número de registro sanitario, nombre del producto, titular del registro, estado del registro, forma farmacéutica, vía de administración y fechas asociadas al proceso regulatorio.

Los datos fueron descargados en formato CSV y posteriormente procesados para su análisis mediante herramientas de ciencia de datos en Python.

# Metodología
1. Carga de datos (Cuaderno 1)
Los datos fueron cargados utilizando la librería Pandas, a partir de archivos CSV descargados directamente desde la plataforma Datos Abiertos Colombia.
En esta etapa se realizó una exploración inicial del conjunto de datos para identificar su estructura, tipos de variables y posibles inconsistencias.

2. Limpieza de datos (Cuaderno 2)
Durante la etapa de limpieza se realizaron los siguientes procesos:
  - Eliminación de registros duplicados.
  - Revisión y manejo de valores nulos en variables relevantes.
  - Normalización de nombres de columnas para facilitar el análisis.
  - Verificación de la consistencia de variables regulatorias como estado del registro, forma farmacéutica y titular.
  - Las funciones de limpieza se implementaron en el archivo src/limpieza.py y se aplicaron desde el cuaderno 02_limpieza.ipynb.

3. Análisis estadístico (Cuaderno 3)
Se llevaron a cabo análisis estadísticos descriptivos enfocados en variables categóricas, incluyendo:
  - Conteo total de registros sanitarios.
  - Tablas de frecuencia y porcentajes por:
  - Estado del registro sanitario.
  - Forma farmacéutica.
  - Titular del registro.
  - Identificación de los titulares con mayor número de registros.

Las funciones estadísticas se encuentran implementadas en el archivo src/analisis.py.

4. Visualizaciones
Se realizaron visualizaciones utilizando Matplotlib y Seaborn, incluyendo:
  - Gráficos de barras para la distribución del estado del registro sanitario.
  - Gráficos comparativos por forma farmacéutica.
  - Visualización de la concentración de registros por titular.
  - Gráficos de frecuencia para variables regulatorias relevantes.

Las funciones de visualización se encuentran en src/visualizaciones.py y se ejecutan desde el cuaderno 03_Analisis_Visualizaciones.ipynb.

# Resultados 

El análisis evidenció que una proporción significativa de los medicamentos homeopáticos registrados corresponde a estados regulatorios vigentes, lo que refleja la presencia activa de estos productos en el mercado farmacéutico colombiano. La información regulatoria permite identificar la dinámica del registro sanitario y su evolución en el tiempo.

Se observó una concentración de registros en determinadas formas farmacéuticas, lo cual sugiere preferencias en la presentación de medicamentos homeopáticos y posibles facilidades en su fabricación y comercialización. Asimismo, se identificaron titulares que concentran un mayor número de registros sanitarios, lo que puede reflejar su posicionamiento dentro de este segmento del mercado.

  # Patrones encontrados

Los resultados muestran una distribución desigual de los registros entre los distintos titulares y formas farmacéuticas. Algunos laboratorios concentran un número considerable de registros, mientras que otros presentan participaciones menores. Este patrón sugiere una estructura de mercado heterogénea dentro del sector de medicamentos homeopáticos.

  # Hallazgos inesperados

Se identificaron registros con información incompleta o con estados regulatorios poco frecuentes, lo cual resalta la importancia de procesos de limpieza y validación de datos al trabajar con información administrativa y regulatoria proveniente de fuentes abiertas.

# Conclusiones

El análisis de los registros sanitarios de medicamentos homeopáticos permitió caracterizar el estado regulatorio y la distribución de estos productos en Colombia. Se evidenció una concentración de registros en ciertos titulares y formas farmacéuticas, así como una presencia relevante de registros vigentes en el mercado.

Este tipo de análisis contribuye a la comprensión del panorama regulatorio de los medicamentos homeopáticos y puede servir como insumo para procesos de vigilancia sanitaria, gestión farmacéutica y toma de decisiones en salud pública.

# Limitaciones de los datos

El conjunto de datos no incluye información sobre consumo, ventas, eficacia clínica ni impacto terapéutico de los medicamentos. Además, algunas variables presentan valores nulos o información limitada, lo que restringe análisis más profundos.

# Recomendaciones para políticas de salud o gestión farmacéutica

Se recomienda fortalecer el monitoreo continuo de los registros sanitarios y promover la transparencia de la información regulatoria. Este tipo de análisis puede apoyar la toma de decisiones relacionadas con la vigilancia sanitaria y la evaluación del mercado de medicamentos homeopáticos en Colombia.

# Análisis futuro útil

Futuros estudios podrían integrar información temporal más detallada para evaluar la evolución de los registros sanitarios, así como relacionar estos datos con información de consumo, distribución o alertas sanitarias emitidas por la autoridad regulatoria.




