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

**Random Forest Architecture**
![Graphical-representation-of-the-random-forest-algorithm](https://github.com/user-attachments/assets/616b8f68-a49b-4092-924a-609dfeebc806)

**Feedforward Neural Networ Architecture**

![398048679-ace82954-b091-4cd6-a443-9d089397641b](https://github.com/user-attachments/assets/7bc8e33c-39eb-49c4-99cf-5cd55fded4f4)

## Overview Dataset
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

## Preprocessing & Modelling
## Random Forest
**Preprocessing**

Preprocessing dilakukan dengan menghapus data yang memiliki nilai kosong atau outlier yang tidak logis. Selain itu dengan mengubah data kategorikal menjadi numerik dan normalisasi data numerik. Data dibagi menjadi data train 75% dan data test 25%.

**Model**

RandomForestRegressor yang merupakan model berbasis ensemble dari banyak pohon keputusan.
Parameter:
- random_state=42: Menetapkan seed untuk memastikan hasil yang konsisten dan dapat direproduksi setiap kali model dijalankan.

  ![Cuplikan layar 2024-12-23 111233](https://github.com/user-attachments/assets/9e8795b6-56d3-4498-b8aa-44bb753a1ebd)

Gambar diatas merupakan Classification Report dari Model setelah dilakukan predict terhadap Testing Set. Dapat dilihat bahwa Akurasinya mencapai 98%.

![Cuplikan layar 2024-12-23 111248](https://github.com/user-attachments/assets/110bccc3-640a-4ee7-95a5-dfcc51d0971a)

Gambar diatas merupakan hasil dari prediksi model terhadap harga diamonds.

## Feedforward Neural Network (FFNN)
**Preprocessing**

Preprocessing dilakukan dengan menghapus data yang memiliki nilai kosong atau outlier yang tidak logis. Selain itu dengan mengubah data kategorikal menjadi numerik dan normalisasi data numerik. Data dibagi menjadi data train 80% dan data test 20%.

**Model**
Feedforward Neural Network (FFNN) menggunakan Keras, yang dirancang untuk menyelesaikan masalah regresi (karena output layer memiliki 1 neuron tanpa fungsi aktivasi). 
Arsitektur:
- Input layer sesuai dengan jumlah fitur.
- Hidden layers dengan 2 lapisan, masing-masing 128 dan 64 neuron, menggunakan aktivasi ReLU.
- Dropout layers dengan 2 lapisan dengan probabilitas yang 20%.
- Output layer dengan 1 neuron menggunakan aktivasi linear.
Optimizer: Adam.
- Loss Function: Mean Squared Error (MSE).
- Batch size: 32.
- Epochs: 50.

  ![{CF8DD3C6-AEE1-4362-BEE8-A1B500961927}](https://github.com/user-attachments/assets/4b771b3a-005f-4b98-877c-988cb3e1c160)

Gambar diatas merupakan Classification Report dari Model setelah dilakukan predict terhadap Testing Set. Dapat dilihat bahwa Akurasinya mencapai 98%.

  ![{E08F4F17-8AB2-4C20-934D-BC1E4F162D09}](https://github.com/user-attachments/assets/3d2641f6-4578-42a1-8c89-42173af9979a)

Gambar diatas merupakan hasil dari prediksi model terhadap harga diamonds.

**Link Model: https://drive.google.com/drive/folders/163GVI8dRKvrgndXsXQUMcjzg8RJzWpHp?usp=sharing**
