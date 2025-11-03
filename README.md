# A3.2-Redes-Neuronales

En este proyecto se desarrolló un sistema de **reconocimiento de dígitos escritos a mano** utilizando redes neuronales artificiales.  
El modelo fue entrenado con la base de datos **MNIST**, ampliamente utilizada en el aprendizaje automático para tareas de clasificación de imágenes de dígitos del 0 al 9.

El objetivo fue implementar un modelo capaz de:
1. Clasificar correctamente los dígitos del conjunto de datos MNIST.  
2. Evaluar su exactitud en el conjunto de prueba.  
3. Aplicar el modelo en **tiempo real**, capturando imágenes con la cámara para realizar predicciones.  
4. Generar 50 imágenes personalizadas (5 por dígito), procesarlas y evaluar el desempeño del modelo.  
5. Introducir **mejoras al sistema** que incrementen la precisión y la robustez del modelo ante variaciones reales de iluminación, ruido o escritura.

## **Predicción en tiempo real**

El sistema fue adaptado para realizar **predicciones con cámara en tiempo real**, utilizando OpenCV y TensorFlow.  
El modelo entrenado se exportó en formato `.h5` (`my_model.h5`) y se integró a un script (`real_time_prediction.py`) que:
- Captura imágenes en vivo.  
- Las convierte a escala de grises y aplica un **umbral binario**.  
- Redimensiona a 28×28 píxeles.  
- Predice el dígito correspondiente mostrando el resultado sobre la imagen.

Además, se implementó una funcionalidad interactiva:
- Presionar **‘s’** → pausa el video y muestra la imagen actual y su predicción.  
- Presionar **‘s’** de nuevo → reanuda el reconocimiento en tiempo real.  
- Presionar **‘q’** → finaliza la ejecución.

---

## **Evaluación con 50 imágenes personalizadas**

Para evaluar el modelo en condiciones reales, se crearon **50 imágenes personalizadas (5 por cada dígito del 0 al 9)**.  
Estas imágenes fueron preprocesadas de manera similar al conjunto MNIST (escala de grises, umbral binario, 28×28 píxeles).  

El notebook incluye una sección donde se:
- Suben las 50 imágenes.  
- Se muestra cada una junto con su versión umbralizada.  
- Se despliega la predicción correspondiente.  
- Se calcula la **precisión total del modelo** en dichas imágenes.

---

## ⚙️ **Archivos incluidos**

- [A3.2_Redes_Neuronales.ipynb](A3.2_Redes_Neuronales.ipynb) → Notebook con entrenamiento, evaluación y pruebas.  
- [real_time_prediction.py](real_time_prediction.py) → Script para predicción en tiempo real con cámara.  
- [my_model.h5](my_model.h5) → Modelo entrenado y guardado.  
- [test_digits/](test_digits/) → Carpeta con las 50 imágenes personalizadas (5 por dígito).  


---

## 🔬 **Bibliotecas utilizadas**

- TensorFlow / Keras  
- NumPy  
- Matplotlib  
- OpenCV  
- Google Colab (para ejecución del entorno y captura de imágenes)  


Profesor: *Dr. Antonio Martínez Torteya*  
Año: 2025  
