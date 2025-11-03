import cv2
import numpy as np
import tensorflow as tf

# Cargar el modelo entrenado
model = tf.keras.models.load_model("my_model.h5")

cap = cv2.VideoCapture(0)

print("Presiona 'q' para salir, 's' para pausar y reanudar el tiempo real.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Preprocesamiento
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, threshed = cv2.threshold(gray, 105, 255, cv2.THRESH_BINARY_INV)
        resized = cv2.resize(threshed, (28, 28))
        input_img = resized.reshape(1, 28, 28, 1)

        # Predicción
        prediction = model.predict(input_img)
        predicted_label = np.argmax(prediction)

        # Mostrar resultado en la imagen
        frame_with_prediction = cv2.putText(
            frame.copy(),
            f"Prediccion: {predicted_label}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2,
            cv2.LINE_AA
        )

        cv2.imshow("Real-time prediction", frame_with_prediction)

        # Captura de teclas
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break

        elif key == ord('s'):
            # Pausar el flujo y mostrar la imagen actual
            print("⏸️  Pausa: mostrando imagen actual...")
            cv2.imshow("Imagen pausada", frame_with_prediction)
            cv2.imshow("Procesada (28x28)", cv2.resize(resized, (280, 280), interpolation=cv2.INTER_NEAREST))
            print("Presiona 's' de nuevo para continuar...")

            # Esperar a que se presione otra vez 's' para continuar
            while True:
                key2 = cv2.waitKey(1) & 0xFF
                if key2 == ord('s'):
                    print("▶️  Continuando en tiempo real...")
                    cv2.destroyWindow("Imagen pausada")
                    cv2.destroyWindow("Procesada (28x28)")
                    break

except KeyboardInterrupt:
    pass
finally:
    cap.release()
    cv2.destroyAllWindows()
