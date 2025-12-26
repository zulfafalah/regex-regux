from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Username unik untuk user")
    email: EmailStr = Field(..., description="Email address user")

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="Password user (minimal 6 karakter)")

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True  # Untuk Pydantic v2, gunakan from_attributes
        # orm_mode = True  # Untuk Pydantic v1
