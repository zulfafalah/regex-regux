from fastapi import FastAPI
from .routers import user_router
from .database import engine, Base
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Membuat database tables (hanya untuk development)
# Dalam production, gunakan Alembic untuk migration
# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=os.getenv("APP_NAME", "User Management API"),
    description="API untuk manajemen user dengan FastAPI dan SQLAlchemy",
    version=os.getenv("APP_VERSION", "1.0.0")
)

# Register routers
app.include_router(user_router)

@app.get("/")
def root():
    """
    Endpoint root untuk health check
    """
    return {
        "message": "Welcome to User Management API",
        "status": "running",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    """
    Endpoint untuk health check
    """
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    debug = os.getenv("DEBUG", "True").lower() == "true"
    
    uvicorn.run("app.main:app", host=host, port=port, reload=debug)
