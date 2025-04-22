import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report

import matplotlib.pyplot as plt
import numpy as np
import zipfile
import os
import tempfile
from sklearn.model_selection import train_test_split

# Título
st.title("Proyecto 1: RNA para Clasificación de Imágenes")

# Descripción
st.write("Este proyecto utiliza redes neuronales artificiales para la clasificación de imágenes. Puedes cargar tus datos y entrenar el modelo directamente desde esta aplicación.")

# Cargar archivo ZIP único
st.header("Carga de datos")

DATASET_PATH='df/PetImages'
st.success("Los datos han sido cargados y extraídos correctamente.")
st.subheader('Verificamos si se esta usando el GPU')
st.write(tf.test.gpu_device_name())

def filter_images():
  st.write('Eliminando Imagenes que no cumplan el formato')
  deleted_imgs = 0
  for folder_name in ("Cat", "Dog"):
    folder_path = os.path.join(DATASET_PATH, folder_name)
    for image in os.listdir(folder_path):
        img_path = os.path.join(folder_path, image)
        try:
            fobj = open(img_path, "rb")
            # Comprobamos si la imagen esta en formato JPEG
            is_jfif = tf.compat.as_bytes("JFIF") in fobj.peek(10)
        finally:
            fobj.close()
        if not is_jfif:
            deleted_imgs += 1
            # Eliminamos la imagen correspondiente
            os.remove(img_path)
  st.success(f"Imágenes eliminadas: {deleted_imgs}")

filter_images()
def filter_imagesCorruptas():
    st.write('Eliminando imágenes corruptas o que no se puedan decodificar correctamente')
    deleted_imgs = 0
    for folder_name in os.listdir(DATASET_PATH):
        folder_path = os.path.join(DATASET_PATH, folder_name)
        if not os.path.isdir(folder_path):
            continue

        for image in os.listdir(folder_path):
            img_path = os.path.join(folder_path, image)
            try:
                # Verificar si la imagen se puede abrir y decodificar correctamente
                img = tf.io.read_file(img_path)
                _ = tf.io.decode_image(img, expand_animations=False)
            except Exception as e:
                deleted_imgs += 1
                os.remove(img_path)
                st.write(f"Imagen corrupta eliminada: {img_path} ({e})")

    st.success(f"Imágenes corruptas eliminadas: {deleted_imgs}")
filter_imagesCorruptas()



st.subheader("##Creación de un Dataset con Keras")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

st.write("Mostrando las primeras 9 imágenes del directorio:")

    # Crear una figura de Streamlit
fig, axes = plt.subplots(3, 3, figsize=(10, 10))
axes = axes.flatten()
folder_path = os.path.join(DATASET_PATH, "Dog")
for i, image in enumerate(os.listdir(folder_path)[:9]):
    img_path = os.path.join(folder_path, image)
    img = mpimg.imread(img_path)

    ax = axes[i]
    ax.imshow(img)
    ax.set_title(f"{img.shape[0]} x {img.shape[1]} píxeles")
    ax.axis("off")

    # Ajustar el layout
    plt.tight_layout()
st.pyplot(fig)
st.write('Keras nos permite normalizar el tamaño de las imágenes de nuestro conjunto de datos haciendo uso de funciones auxiliares que convierten los datos a un objeto Dataset de los diferentes backends que estemos utilizando.')

image_size = (180, 180)
batch_size = 128 # Tamaño de lote

train_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,  # 20% de los datos forman parte del subconjunto de validación
    subset="training",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)





st.write("Mostrando 9 imágenes de un lote del conjunto de entrenamiento:")

    # Crear una figura
fig, axes = plt.subplots(3, 3, figsize=(10, 10))
axes = axes.flatten()

for images, labels in train_ds.take(1):  # Tomar un lote del conjunto de datos
    for i in range(9):
        ax = axes[i]
        ax.imshow(images[i].numpy().astype("uint8"))
        ax.set_title(f"{images[i].shape[0]} x {images[i].shape[1]} píxeles")
        ax.axis("off")

plt.tight_layout()
st.pyplot(fig)

st.subheader("Separación de la etiqueta (label)")

batch1 = list(train_ds.take(1))
st.write(f"Número de imágenes en el batch: {len(batch1[0][0])}")
st.write(f"Etiquetas del batch: {batch1[0][1]}")
    # Crear una figura
fig, axes = plt.subplots(3, 3, figsize=(10, 10))
axes = axes.flatten()

for images, etiqueta in train_ds.take(1):  # Tomar un lote del conjunto de datos
    for i in range(9):
        ax = axes[i]
        ax.imshow(images[i].numpy().astype("uint8"))
        ax.set_title(f"Etiqueta: {etiqueta[i]}")
        ax.axis("off")

plt.tight_layout()
st.pyplot(fig)
st.subheader("División del conjunto de datos")
st.text("""

Cuando abordamos la resolución de un problema real aplicando Inteligencia Artificial / Machine Learning / Deep Learning, debemos dividir el conjunto de datos en 3 subconjuntos:

Subconjunto de entrenamiento (train_ds): Contiene apróximadamente el 60-80% de los datos. Este subcojunto se utiliza para entrenar el algoritmo.
Subconjunto de validación (val_ds): Contiene apróximadamente el 10-20% de los datos. Este subcojunto se utiliza para validar el comportamiento del algoritmo durante el proceso de entrenamiento.
Subconjunto de pruebas (test_ds): Contiene apróximadamente el 10-20% de los datos. Este subconjunto se utilizar para validar el comportamiento del algoritmo entrenado final. Su función es determinar si el modelo se comporta correctamente para ejemplos que no ha visto nunca.
Esta división y modo de actuar nos permite evitar problemas graves como el sobreentrenamiento u overfitting.

Keras nos permite dividir de manera muy sencilla el conjunto de datos en el subconjunto de entrenamiento y validación.
""")

# Obtenemos el suconjunto de validación
temp_val_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,  # 20% de los datos forman parte del subconjunto de validación
    subset="validation",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)

st.write(len(temp_val_ds))
# 50% de los datos formarán parte del subconjunto de validación y 50% del de pruebas
val_size = int(0.5 * len(temp_val_ds))
st.write(val_size)
val_ds = temp_val_ds.take(val_size)
test_ds = temp_val_ds.skip(val_size)
st.write(len(val_ds),len(test_ds))

## Aplicando  train_test_split de sckitlearn
from sklearn.model_selection import train_test_split
val_ds_sk = list(temp_val_ds)
# División del conjunto de validación en validación y prueba
val_ds_sk, test_ds_sk = train_test_split(
    val_ds_sk,
    test_size=0.5,  # Porcentaje para prueba
    random_state=42,  # Semilla para reproducibilidad
)


st.write("2. Definicion de la arquitectura de la Red Neuronal Artificial")


from keras import layers

input_shape = (180, 180, 3) # Dimension de las imagenes

fcnn_model = tf.keras.Sequential()

# Entrada de la red neuronal
fcnn_model.add(layers.Input(shape=input_shape))

# Escalamos las imágenes
fcnn_model.add(layers.Rescaling(1.0 / 255))

# Aplana las imágenes para la primera capa densa
fcnn_model.add(layers.Flatten())

# Layer 1
fcnn_model.add(layers.Dense(384, activation='relu'))

# Layer 2
fcnn_model.add(layers.Dense(256, activation='relu'))

# Layer 3
fcnn_model.add(layers.Dense(128, activation='relu'))

# Layer 4
fcnn_model.add(layers.Dense(1, activation='sigmoid')) # softmax
st.subheader("Visualizacion de la Red Neuronal")
fcnn_model.summary(print_fn=lambda x: st.text(x))

st.write(fcnn_model.layers)
hidden1 = fcnn_model.layers[2]
weights, biases = hidden1.get_weights()
st.write(weights,biases)
st.subheader("3. Configuracion de la Red Neuronal Artificial")

fcnn_model.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.Adam(1e-3), metrics=['accuracy'])


st.text("Resumen del modelo:")
fcnn_model.summary(print_fn=lambda x: st.text(x))

    # Entrenamiento
st.header("Entrenamiento del modelo")
epochss = st.number_input("Número de épocas", min_value=1, max_value=50, value=10, step=1)


if st.button("Entrenar modelo"):
    history = fcnn_model.fit(train_ds, epochs=epochss, validation_data=val_ds)
    st.subheader("Resultados del entrenamiento")
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    ax[0].plot(history.history['accuracy'], label='Precisión en entrenamiento')
    ax[0].plot(history.history['val_accuracy'], label='Precisión en validación')
    ax[0].set_title('Precisión')
    ax[0].set_xlabel('Épocas')
    ax[0].set_ylabel('Precisión')
    ax[0].legend()

    ax[1].plot(history.history['loss'], label='Pérdida en entrenamiento')
    ax[1].plot(history.history['val_loss'], label='Pérdida en validación')
    ax[1].set_title('Pérdida')
    ax[1].set_xlabel('Épocas')
    ax[1].set_ylabel('Pérdida')
    ax[1].legend()

    st.pyplot(fig)

        # Evaluación del modelo
    st.subheader("Evaluación del modelo")

    ##val_ds.reset()
    predictions = np.argmax(fcnn_model.predict(val_ds), axis=-1)
    ##report = classification_report(val_ds.classes, predictions, target_names=list(val_ds.class_indices.keys()))

    ##st.text(report)

    ##model_path = os.path.join(tempfile.gettempdir(), "modelo_entrenado")
    fcnn_model.save("ModeloEntrenadoImagenes.h5")
    st.success(f"El modelo ha sido guardado en: ModeloEntrenadoImagenesKeras.h5")