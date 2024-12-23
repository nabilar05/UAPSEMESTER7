import streamlit as st
import pandas as pd
import numpy as np
import gdown
import os
import joblib  # Untuk memuat model Random Forest
import tensorflow as tf

# Tautan model dari Google Drive
ffnn_model_url = "https://drive.google.com/uc?id=1_I5Egb47Hsm0AcitcjD5fQu0ZEg3ej1j"
random_forest_model_url = "https://drive.google.com/uc?id=1vrSjfrUr_tUDRXELzlWrskJoSOLAeNyj"

# Path untuk menyimpan model
ffnn_model_path = "ffnn_diamonds_model.h5"
random_forest_model_path = "random_forest_diamonds_model.pkl"

# Fungsi untuk mengunduh dan memuat model
@st.cache_resource
def load_trained_models():
    # Unduh model FFNN jika belum ada
    if not os.path.exists(ffnn_model_path):
        with st.spinner(f"Mengunduh model FFNN dari Google Drive..."):
            gdown.download(ffnn_model_url, ffnn_model_path, quiet=False)

    # Unduh model Random Forest jika belum ada
    if not os.path.exists(random_forest_model_path):
        with st.spinner(f"Mengunduh model Random Forest dari Google Drive..."):
            gdown.download(random_forest_model_url, random_forest_model_path, quiet=False)

    # Muat model FFNN
    try:
        model_1 = tf.keras.models.load_model(ffnn_model_path)
    except Exception as e:
        st.error(f"Gagal memuat model FFNN: {e}")
        model_1 = None

    # Muat model Random Forest
    try:
        model_2 = joblib.load(random_forest_model_path)
    except Exception as e:
        st.error(f"Gagal memuat model Random Forest: {e}")
        model_2 = None

    return model_1, model_2

# Muat model
model_1, model_2 = load_trained_models()

# Daftar fitur yang diperlukan untuk prediksi
input_features = ['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']

# Mapping nilai kategorikal ke numerikal
cut_mapping = {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Premium': 4, 'Ideal': 5}
color_mapping = {'J': 1, 'I': 2, 'H': 3, 'G': 4, 'F': 5, 'E': 6, 'D': 7}
clarity_mapping = {'I1': 1, 'SI2': 2, 'SI1': 3, 'VS2': 4, 'VS1': 5, 'VVS2': 6, 'VVS1': 7, 'IF': 8}

# Fungsi untuk memproses data input
def preprocess_input(data):
    data['cut'] = data['cut'].map(cut_mapping)
    data['color'] = data['color'].map(color_mapping)
    data['clarity'] = data['clarity'].map(clarity_mapping)
    data = data[input_features]
    return np.array(data).astype(float)

# Konfigurasi halaman Streamlit
st.title("Prediksi Harga Berlian")
st.write("Masukkan detail berlian untuk memprediksi harga menggunakan model yang telah dilatih.")

# Pilihan model
st.sidebar.header("Pilih Model")
use_model_1 = st.sidebar.checkbox("Gunakan Model FFNN", value=True)
use_model_2 = st.sidebar.checkbox("Gunakan Model Random Forest", value=True)

if not (use_model_1 or use_model_2):
    st.sidebar.warning("Pilih setidaknya satu model untuk melanjutkan.")

# Input form untuk fitur berlian
with st.form("diamond_form"):
    carat = st.number_input("Carat", min_value=0.0, max_value=5.0, step=0.01)
    cut = st.selectbox("Cut", options=list(cut_mapping.keys()))
    color = st.selectbox("Color", options=list(color_mapping.keys()))
    clarity = st.selectbox("Clarity", options=list(clarity_mapping.keys()))
    depth = st.number_input("Depth (%)", min_value=0.0, max_value=100.0, step=0.1)
    table = st.number_input("Table (%)", min_value=0.0, max_value=100.0, step=0.1)
    x = st.number_input("Length (mm)", min_value=0.0, step=0.1)
    y = st.number_input("Width (mm)", min_value=0.0, step=0.1)
    z = st.number_input("Height (mm)", min_value=0.0, step=0.1)
    submit = st.form_submit_button("Prediksi Harga")

if submit:
    # Buat DataFrame dari input pengguna
    input_data = pd.DataFrame({
        'carat': [carat],
        'cut': [cut],
        'color': [color],
        'clarity': [clarity],
        'depth': [depth],
        'table': [table],
        'x': [x],
        'y': [y],
        'z': [z]
    })

    # Preprocess data input
    processed_data = preprocess_input(input_data)

    # Prediksi harga menggunakan model yang dipilih
    if use_model_1 and model_1:
        prediction_1 = model_1.predict(processed_data)
        predicted_price_1 = prediction_1[0][0]
        st.write(f"**Prediksi Model FFNN:** ${predicted_price_1:,.2f}")

    if use_model_2 and model_2:
        prediction_2 = model_2.predict(processed_data)
        predicted_price_2 = prediction_2[0]  # Random Forest output
        st.write(f"**Prediksi Model Random Forest:** ${predicted_price_2:,.2f}")

    # Perbandingan prediksi jika kedua model dipilih
    if use_model_1 and use_model_2 and model_1 and model_2:
        st.write("### Perbandingan Prediksi")
        st.write(f"- **Model FFNN:** ${predicted_price_1:,.2f}")
        st.write(f"- **Model Random Forest:** ${predicted_price_2:,.2f}")
        difference = abs(predicted_price_1 - predicted_price_2)
        st.write(f"**Perbedaan antara kedua model:** ${difference:,.2f}")
