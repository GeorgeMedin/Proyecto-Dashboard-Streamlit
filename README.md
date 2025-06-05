# 🎧 Dashboard Interactivo de Transmisión Global de Spotify con Streamlit

Este proyecto utiliza **Streamlit** para crear un dashboard interactivo con datos de transmisión global de Spotify, extraídos desde Kaggle. Aunque normalmente he trabajado con Power BI y Looker Studio, ¡quedé gratamente sorprendido con lo fácil y poderoso que es crear dashboards con Python y Streamlit!

## 🛠 Tecnologías utilizadas  
- ✅ **Python** → Lenguaje principal para manipulación y visualización de datos  
- ✅ **Streamlit** → Para desplegar el dashboard web interactivo  
- ✅ **Pandas** → Para manipular los datos tabulares  
- ✅ **kagglehub** → Para cargar datasets desde Kaggle automáticamente  

## 🚀 ¿Qué hace este proyecto?  
- 🔹 Muestra una tabla con datos de transmisión de Spotify (país, artista, álbum, oyentes, etc.)  
- 🔹 Permite aplicar filtros por año y país  
- 🔹 Incluye un botón para quitar todos los filtros de forma dinámica  
- 🔹 Todo en una interfaz visual simple, clara y funcional  

## 📂 Contenido del repositorio  
- 📄 `proyecto.py` → Código principal del dashboard en Streamlit
- 📄 `exportBDKaggle.py` → Base de datos extraida directamente de Kaggle
- 📄 `SpotifyBD.csv` → Dataset utilizado (descargado desde Kaggle)  
- 📷 `preview.gif` → Captura del dashboard funcionando (¡se ve genial!)  

## 🔧 Cómo ejecutarlo  
1. Clona el repositorio  
2. Asegúrate de tener Python instalado  
3. Instala las dependencias:
    ```bash
    pip install streamlit pandas kagglehub
    ```
4. Ejecuta el dashboard:
    ```bash
    streamlit run app.py
    ```

## 🌍 Dataset original  
Este dashboard está basado en el dataset disponible en Kaggle:  
🔗 [Spotify Global Streaming Data 2024](https://www.kaggle.com/datasets/atharvasoundankar/spotify-global-streaming-data-2024)

## 📩 Contacto  
¿Ideas, mejoras o solo quieres saludar? ¡Conéctate conmigo en LinkedIn!  
🔗 [https://www.linkedin.com/in/jorge-medina-rincon-5b7507237/](https://www.linkedin.com/in/jorge-medina-rincon-5b7507237/)
