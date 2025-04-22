import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
# Título de la aplicación
st.title("Clasificador de Imágenes de Perro o Gato")

# Cargar el modelo entrenado
fcnn_model_disk = tf.keras.models.load_model("ModeloEntrenadoImagenes.h5")
st.success("Modelo Cargado Correctamente....")


DATASET_PATH='df/PetImages'
image_size = (180, 180)
batch_size = 128 # Tamaño de lote
temp_val_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,  # 20% de los datos forman parte del subconjunto de validación
    subset="validation",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)

val_size = int(0.5 * len(temp_val_ds))
val_ds = temp_val_ds.take(val_size)
test_ds = temp_val_ds.skip(val_size)


# Evaluamos el modelo con el conjunto de datos de pruebas
evaluation_result = fcnn_model_disk.evaluate(test_ds)

# Imprimir las métricas de evaluación (por ejemplo, pérdida y precisión)
st.write("Loss:", evaluation_result[0])
st.write("Accuracy:", evaluation_result[1])


# Mostrar las imágenes del conjunto de datos junto con las predicciones
st.header("Resultados del modelo en un lote de datos de prueba")

for images, labels in test_ds.take(1):  # Obtener un lote del conjunto de datos
    fig = plt.figure(figsize=(10, 10))
    for i in range(9):  # Mostrar 9 imágenes del lote
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        predictions = fcnn_model_disk.predict(tf.expand_dims(images[i], 0))
        score = float(predictions[0])
        plt.title(f"Gato: {100 * (1 - score):.2f}%, Perro: {100 * score:.2f}%")
        plt.axis("off")

    # Mostrar la figura en Streamlit
    st.pyplot(fig)


# Subir una imagen para clasificar
uploaded_image = st.file_uploader("Cargar una imagen (Perro o Gato)", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Mostrar la imagen cargada
    img = image.load_img(uploaded_image, target_size=(180, 180))  # Ajusta el tamaño según lo que espera tu modelo
    st.image(img, caption="Imagen Cargada", use_column_width=180)


    predictions = fcnn_model_disk.predict(tf.expand_dims(img, 0))
    score = float(predictions[0])
    st.write(score)
    st.write(f"Gato: {100 * (1 - score):.2f}%, Perro: {100 * score:.2f}%")

    # Mostrar el resultado
    if predictions[0] > 0.5:
        st.write("¡Es un perro!")
    else:
        st.write("¡Es un gato!")
