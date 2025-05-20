# 🏠 Housing Price Prediction

Este proyecto entrena y expone una API que utiliza un modelo de regresión para predecir el precio de una vivienda, basándose en características como:

- Ingreso medio en la zona (`MedInc`)
- Edad promedio de las viviendas (`HouseAge`)
- Promedio de habitaciones y dormitorios (`AveRooms`, `AveBedrms`)
- Población y ocupación (`Population`, `AveOccup`)
- Ubicación geográfica (`Latitude`, `Longitude`)

## 🚀 Tecnologías usadas

- Python 3.11+
- FastAPI
- Scikit-learn
- Pandas
- Uvicorn

---

## ⚙️ Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/housing-price-prediction.git
cd housing-price-prediction
````

2. Crea y activa un entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecuta el servidor:

```bash
uvicorn app.main:app --reload
```

---

## 📡 API - Predicción de precios

### Endpoint

`POST /predict`

### Ejemplo de request:

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "MedInc": 8.3,
    "HouseAge": 41,
    "AveRooms": 6.3,
    "AveBedrms": 1.0,
    "Population": 980,
    "AveOccup": 2.7,
    "Latitude": 34.0,
    "Longitude": -118.0
  }'
```

### Ejemplo de respuesta:

```json
{
  "prediction": 256789.12
}
```

---

## 📁 Estructura del proyecto

```
ml-house-price/
├── app/
│   ├── main.py          # Archivo principal con la instancia de FastAPI
│   ├── predict.py       # Lógica del modelo de predicción
│   └── schemas.py       # Definiciones de entrada con Pydantic
├── model/
│   └── model.joblib     # Modelo entrenado guardado
├── notebooks/           # Notebooks de entrenamiento y análisis
├── requirements.txt     # Dependencias del proyecto
└── README.md
```

---

## 🧪 Entrenamiento del modelo

Puedes entrenar el modelo utilizando los notebooks en la carpeta `notebooks/`, donde se realiza la preparación de datos y el entrenamiento con `scikit-learn`.

---

## 📄 Licencia

Este proyecto está licenciado bajo la MIT License. Consulta el archivo [LICENSE](LICENSE) para más detalles.
