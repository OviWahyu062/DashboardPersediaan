# Sistem Permintaan Master Material & Approval (Python Version)

Website aplikasi persediaan dan alur approval berjenjang (L1 - L4) berbasis **Python (Flask)** dan antarmuka web modern (Tailwind CSS + Chart.js).

---

## 📁 Struktur Folder Proyek
```text
sistem-persediaan/
│── app.py                 # Backend utama berbasis Flask (REST API & penyimpanan data)
│── run_simple.py          # Server ringan bawaan Python (tanpa install library tambahan)
│── requirements.txt       # Daftar dependensi (Flask)
│── data_requests.json     # File database lokal (dibuat otomatis saat app.py dijalankan)
└── templates/
    └── index.html         # Tampilan frontend website (HTML, Tailwind CSS, Chart.js, JS)
```

---

## 🚀 Cara Menjalankan di VS Code

### Cara 1: Menggunakan Flask (Sangat Direkomendasikan)
1. Buka folder ini di **Visual Studio Code**:
   - Menu **File** -> **Open Folder...** -> pilih folder `sistem-persediaan`.
2. Buka Terminal di VS Code:
   - Tekan `Ctrl + ~` (atau menu **Terminal** -> **New Terminal**).
3. Install dependensi Flask:
   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan aplikasinya:
   ```bash
   python app.py
   ```
5. Browser Anda akan **otomatis terbuka** ke alamat:
   ```text
   http://127.0.0.1:5000
   ```
   *(Data pengajuan dan approval akan tersimpan rapi di file `data_requests.json`)*.

---

### Cara 2: Menggunakan Server Ringan Bawaan Python (Tanpa Install Apapun)
Jika Anda belum ingin menginstall Flask, Anda bisa langsung menjalankan server bawaan Python:
1. Buka Terminal di VS Code (`Ctrl + ~`).
2. Jalankan perintah:
   ```bash
   python run_simple.py
   ```
3. Browser akan otomatis membuka `http://127.0.0.1:8000/index.html`.
