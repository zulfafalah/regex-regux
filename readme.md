# PDF Extractor - Purchase Order FOODHALL

Script Python sederhana untuk mengekstrak data dari PDF Purchase Order (FOODHALL) menjadi format JSON.

## Fitur

- Ekstrak data header (Order ID, Customer, NPWP, dll)
- Ekstrak data items (Article, Description, Qty, Price, dll)
- Output dalam format JSON
- Support multiple PDF files sekaligus

## Requirements

- Python 3.11
- pdfplumber

## Instalasi

1. Clone atau download repository ini
2. Buat virtual environment:
```bash
python3 -m venv env
```

3. Aktifkan virtual environment:
```bash
source env/bin/activate
```

4. Install dependencies:
```bash
pip install pdfplumber
```

## Cara Penggunaan

1. Letakkan file PDF yang ingin diekstrak di folder `pdf/`

2. Jalankan script:
```bash
python main.py
```

3. Hasil ekstraksi akan tersimpan di file `output.json`

## Catatan

- Script ini menggunakan regex pattern untuk ekstraksi data
- Pastikan format PDF sesuai dengan pattern yang didefinisikan
- File PDF harus berada di folder `pdf/`
