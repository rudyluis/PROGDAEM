import streamlit as st
import tensorflow as tf
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Configuración de Streamlit
st.title("Clasificador de Imágenes de Perro o Gato")
st.write("Entrenamiento con TensorFlow y Streamlit")

# Verificar GPU
if tf.config.list_physical_devices('GPU'):
    st.write("✅ GPU detectada. Optimizando para entrenamiento acelerado.")
else:
    st.write("⚠️ No se detectó GPU. El entrenamiento será más lento.")

# Configuración de dataset
DATASET_PATH = "df/PetImages"
image_size = (180, 180)
batch_size = 128

# Carga de datos
train_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH, validation_split=0.2, subset="training",
    seed=1337, image_size=image_size, batch_size=batch_size
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH, validation_split=0.2, subset="validation",
    seed=1337, image_size=image_size, batch_size=batch_size
)

# Preprocesamiento
data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.1),
])

if st.checkbox("Mostrar Ejemplos de Data Augmentation"):
    fig, axs = plt.subplots(3, 3, figsize=(10, 10))
    for images, _ in train_ds.take(1):
        for i in range(9):
            augmented_image = data_augmentation(images)
            ax = axs[i // 3, i % 3]
            ax.imshow(augmented_image[0].numpy().astype("uint8"))
            ax.axis("off")
    st.pyplot(fig)

# Modelo preentrenado (Transfer Learning)
base_model = tf.keras.applications.MobileNetV2(
    weights="imagenet", input_shape=(180, 180, 3), include_top=False
)
base_model.trainable = False

x = layers.GlobalAveragePooling2D()(base_model.output)
x = layers.Dense(1, activation="sigmoid")(x)
model = tf.keras.Model(inputs=base_model.input, outputs=x)

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

if st.button("Iniciar Entrenamiento"):
    history = model.fit(train_ds, validation_data=val_ds, epochs=10)
    st.success("Entrenamiento completado.")

    # Mostrar resultados del entrenamiento
    history_df = pd.DataFrame(history.history)
    fig, ax = plt.subplots()
    history_df.plot(ax=ax)
    st.pyplot(fig)

    # Evaluar modelo
    loss, accuracy = model.evaluate(val_ds, verbose=0)
    st.write(f"Pérdida: {loss:.4f}")
    st.write(f"Precisión: {accuracy:.4f}")
