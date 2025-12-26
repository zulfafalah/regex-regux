from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user import UserCreate
from typing import List, Optional

class UserService:
    """Service layer untuk operasi User"""
    
    @staticmethod
    def get_all_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        """Mengambil semua user dengan pagination"""
        return db.query(User).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
        """Mengambil user berdasarkan ID"""
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def get_user_by_username(db: Session, username: str) -> Optional[User]:
        """Mengambil user berdasarkan username"""
        return db.query(User).filter(User.username == username).first()
    
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Optional[User]:
        """Mengambil user berdasarkan email"""
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def create_user(db: Session, user: UserCreate) -> User:
        """Membuat user baru"""
        # Note: Dalam production, password harus di-hash!
        # from passlib.hash import bcrypt
        # hashed_password = bcrypt.hash(user.password)
        
        db_user = User(
            username=user.username,
            email=user.email,
            password=user.password  # Dalam production, gunakan hashed_password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def delete_user(db: Session, user_id: int) -> bool:
        """Menghapus user berdasarkan ID"""
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
            return True
        return False
