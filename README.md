# Bike Sharing Dashboard 📊

## Deskripsi Proyek

Proyek ini bertujuan untuk melakukan analisis eksploratif dan visualisasi data pada dataset **Bike Sharing** guna memahami pola peminjaman sepeda berdasarkan **musim (season)** dan **jenis hari (working day vs weekend/holiday)**.
Hasil analisis kemudian disajikan dalam bentuk **dashboard interaktif menggunakan Streamlit** agar mudah dipahami oleh pengguna non-teknis.

Proyek ini dikembangkan sebagai bagian dari submission analisis data pada platform **Dicoding**.

---

## Dataset

Dataset yang digunakan adalah **Bike Sharing Dataset (day.csv)** yang berisi data peminjaman sepeda harian dengan beberapa variabel utama, antara lain:

* `dteday` : tanggal pencatatan
* `season` : musim (Spring, Summer, Fall, Winter)
* `workingday` : jenis hari (hari kerja atau akhir pekan/libur)
* `cnt` : total jumlah peminjaman sepeda per hari

Dataset ini bersumber dari **UCI Machine Learning Repository** dan digunakan secara luas untuk analisis time series serta data eksploratif.

---

## Insight Utama

Berdasarkan hasil analisis eksploratif, diperoleh beberapa insight penting:

1. **Musim Fall (Gugur)** memiliki rata-rata jumlah peminjaman sepeda tertinggi dibandingkan musim lainnya.
2. **Hari kerja (Working Day)** menunjukkan jumlah peminjaman yang lebih tinggi dibandingkan akhir pekan atau hari libur.
3. Pola peminjaman dipengaruhi secara signifikan oleh faktor musiman dan aktivitas harian masyarakat.

Insight ini dapat dimanfaatkan sebagai dasar pengambilan keputusan dalam pengelolaan layanan bike sharing.

---

## Cara Menjalankan Dashboard Secara Lokal

Ikuti langkah berikut untuk menjalankan dashboard di komputer lokal:

1. Clone repository ini:

   ```bash
   git clone https://github.com/ANDI-BACHDAR-DD/bike-sharing-dashboard.git
   cd bike-sharing-dashboard
   ```

2. Aktifkan virtual environment (opsional namun direkomendasikan):

   ```bash
   python -m venv venv
   source venv/bin/activate   # MacOS / Linux
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan aplikasi Streamlit:

   ```bash
   streamlit run dashboard/dashboard.py
   ```

5. Dashboard dapat diakses melalui browser pada:

   ```
   http://localhost:8501
   ```

---

## Link Dashboard (Streamlit Cloud)

Dashboard juga telah dideploy secara online dan dapat diakses melalui tautan berikut:

🔗 **[https://bike-sharing-dashboard-asvyulvkkxdykrnb6ynequ.streamlit.app](https://bike-sharing-dashboard-asvyulvkkxdykrnb6ynequ.streamlit.app)**

(Link ini juga dicantumkan dalam file `url.txt` sebagai kemudahan bagi reviewer.)

---

## Struktur Direktori

```
submission/
├── dashboard/
│   ├── dashboard.py
│   └── day.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

---

## Teknologi yang Digunakan

* Python
* Pandas
* Matplotlib
* Seaborn
* Streamlit

---

## Penutup

Dashboard ini diharapkan dapat memberikan gambaran yang jelas mengenai pola penggunaan layanan bike sharing serta menjadi contoh penerapan analisis data dan visualisasi interaktif yang sederhana namun informatif.
