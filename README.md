# Prediksi Harga Diamonds Menggunakan Random Forest dan Feedforward Neural Network (FFNN)
## Overview Project
Proyek ini bertujuan untuk memprediksi harga diamonds menggunakan algoritma Random Forest dan Feedforward Neural Network (FFNN). Dengan pendekatan ini, diharapkan dapat memberikan prediksi harga yang akurat untuk membantu dalam pengambilan keputusan. Harga diamonds dipengaruhi oleh berbagai faktor seperti:
1. carat: Berat berlian.
2. cut: Kualitas potongan (Fair, Good, Very Good, Premium, Ideal).
3. color: Warna berlian (J hingga D, dengan D yang paling baik).
4. clarity: Kejelasan berlian (I1, SI1, SI2, VS1, VS2, VVS1, VVS2, IF).
5. depth: Rasio kedalaman berlian (persentase).
6. table: Lebar bagian atas berlian relatif terhadap bagian terluas.
7. x, y, z: Dimensi fisik berlian dalam milimeter

#Overview Dataset
Dataset yang digunakan adalah dataset "Diamond Price Prediction" yang diambil dari kaggle. Dataset ini memiliki atribut berikut:
1. carat: Berat berlian.
2. cut: Kualitas potongan (Fair, Good, Very Good, Premium, Ideal).
3. color: Warna berlian (J hingga D, dengan D yang paling baik).
4. clarity: Kejelasan berlian (I1, SI1, SI2, VS1, VS2, VVS1, VVS2, IF).
5. depth: Rasio kedalaman berlian (persentase).
6. table: Lebar bagian atas berlian relatif terhadap bagian terluas.
7. price: Harga berlian dalam dolar AS.
8. x, y, z: Dimensi fisik berlian dalam milimeter.

Link Dataset: https://www.kaggle.com/code/karnikakapoor/diamond-price-prediction

# Preprocessing & Modelling
## Random Forest
# Preprocessing
Preprocessing dilakukan dengan menghapus data yang memiliki nilai kosong atau outlier yang tidak logis. Selain itu dengan mengubah data kategorikal menjadi numerik dan normalisasi data numerik.

# Model
RandomForestRegressor yang merupakan model berbasis ensemble dari banyak pohon keputusan.
Parameter:
- random_state=42: Menetapkan seed untuk memastikan hasil yang konsisten dan dapat direproduksi setiap kali model dijalankan.

  ![Cuplikan layar 2024-12-23 111233](https://github.com/user-attachments/assets/9e8795b6-56d3-4498-b8aa-44bb753a1ebd)

Gambar diatas merupakan Classification Report dari Model setelah dilakukan predict terhadap Testing Set. Dapat dilihat bahwa Akurasinya mencapai 98%.

![Cuplikan layar 2024-12-23 111248](https://github.com/user-attachments/assets/110bccc3-640a-4ee7-95a5-dfcc51d0971a)

Gambar diatas merupakan hasil dari prediksi model terhadap harga diamonds.
