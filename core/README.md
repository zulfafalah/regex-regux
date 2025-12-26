# FastAPI Project - User Management API

API sederhana untuk manajemen user menggunakan FastAPI, SQLAlchemy, dan Alembic.

## Struktur Project

```
fastapi-project/
│
├── app/
│   ├── main.py              # Entry point aplikasi
│   ├── database.py          # Konfigurasi database
│   ├── __init__.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   └── user.py          # Router untuk endpoint user
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user.py          # Pydantic schemas untuk validasi
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py          # SQLAlchemy model User
│   │
│   └── services/
│       ├── __init__.py
│       └── user_service.py  # Business logic untuk User
│
├── alembic/
│   ├── env.py               # Konfigurasi Alembic
│   └── versions/            # Migration files
│
├── alembic.ini              # Konfigurasi Alembic
├── requirements.txt         # Dependencies
└── README.md               # Dokumentasi
```

## Features

- ✅ CRUD operations untuk User
- ✅ Model User dengan username, email, password
- ✅ Auto migration menggunakan Alembic
- ✅ Endpoint list users dengan pagination
- ✅ Validasi data menggunakan Pydantic
- ✅ Service layer pattern
- ✅ SQLite database (dapat diganti dengan PostgreSQL/MySQL)

## Installation

### 1. Clone atau buat project

```bash
cd fastapi-project
```

### 2. Buat virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate  # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Database Setup dengan Alembic

### 1. Inisialisasi Alembic (sudah dilakukan)

Jika belum ada folder alembic, jalankan:
```bash
alembic init alembic
```

### 2. Buat migration pertama

```bash
alembic revision --autogenerate -m "Initial migration - create users table"
```

### 3. Apply migration

```bash
alembic upgrade head
```

### 4. Perintah Alembic lainnya

```bash
# Lihat history migration
alembic history

# Rollback migration terakhir
alembic downgrade -1

# Rollback semua migration
alembic downgrade base

# Lihat current revision
alembic current
```

## Running the Application

### Development mode

```bash
uvicorn app.main:app --reload
```

atau

```bash
python -m app.main
```

### Production mode

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

API akan berjalan di: `http://localhost:8000`

## API Endpoints

### Health Check

- **GET** `/` - Root endpoint
- **GET** `/health` - Health check

### User Endpoints

- **GET** `/users/` - List semua user (dengan pagination)
  - Query params: `skip` (default: 0), `limit` (default: 100)
- **GET** `/users/{user_id}` - Get user by ID
- **POST** `/users/` - Create user baru
- **DELETE** `/users/{user_id}` - Delete user by ID

### API Documentation

FastAPI otomatis generate dokumentasi interaktif:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Contoh Request

### Create User

```bash
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "secret123"
  }'
```

### List Users

```bash
curl "http://localhost:8000/users/"
```

### Get User by ID

```bash
curl "http://localhost:8000/users/1"
```

## Database Configuration

File `app/database.py` menggunakan SQLite by default:

```python
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
```

### Untuk PostgreSQL:

```python
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"
```

Jangan lupa update `alembic.ini` juga:

```ini
sqlalchemy.url = postgresql://user:password@localhost/dbname
```

## Security Notes

⚠️ **PENTING untuk Production:**

1. **Password Hashing**: Password saat ini disimpan plain text. Untuk production, gunakan password hashing:

```bash
pip install passlib[bcrypt]
```

Update `app/services/user_service.py`:

```python
from passlib.hash import bcrypt

# Di method create_user:
hashed_password = bcrypt.hash(user.password)
db_user = User(
    username=user.username,
    email=user.email,
    password=hashed_password
)
```

2. **Environment Variables**: Gunakan environment variables untuk database URL dan secrets
3. **CORS**: Tambahkan CORS middleware jika diperlukan
4. **Authentication**: Implementasi JWT atau OAuth2 untuk autentikasi

## Development Tips

### Menambah Model Baru

1. Buat model di `app/models/`
2. Import di `app/models/__init__.py`
3. Import di `alembic/env.py`
4. Buat migration: `alembic revision --autogenerate -m "Add new model"`
5. Apply: `alembic upgrade head`

### Testing

Install pytest:
```bash
pip install pytest pytest-asyncio httpx
```

## License

MIT

## Author

FastAPI Project Template
