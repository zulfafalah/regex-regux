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

## Database Migration dengan Alembic

### Setup Awal

Pastikan Anda sudah berada di direktori `core/`:
```bash
cd core
```

### Membuat Migration Baru

1. Setelah membuat atau mengubah model di `core/app/models/`, pastikan model sudah di-import di `core/app/models/__init__.py`

2. Buat migration dengan autogenerate:
```bash
../env/bin/alembic revision --autogenerate -m "deskripsi perubahan"
```

Contoh:
```bash
../env/bin/alembic revision --autogenerate -m "create customer_regex_rule table"
```

### Menjalankan Migration

Untuk menerapkan migration ke database:
```bash
../env/bin/alembic upgrade head
```

### Command Alembic Lainnya

- **Melihat history migration:**
```bash
../env/bin/alembic history
```

- **Melihat status migration saat ini:**
```bash
../env/bin/alembic current
```

- **Rollback migration (1 step):**
```bash
../env/bin/alembic downgrade -1
```

- **Rollback ke revision tertentu:**
```bash
../env/bin/alembic downgrade <revision_id>
```

- **Rollback semua migration:**
```bash
../env/bin/alembic downgrade base
```

## Catatan

- Script ini menggunakan regex pattern untuk ekstraksi data
- Pastikan format PDF sesuai dengan pattern yang didefinisikan
- File PDF harus berada di folder `pdf/`
- Setiap kali membuat model baru, jangan lupa import di `__init__.py` models sebelum membuat migration
