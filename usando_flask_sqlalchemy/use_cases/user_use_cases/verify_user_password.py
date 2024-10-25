from app_config import bcrypt

def verify_user_password(hashed_password: str, password: str):
    return bcrypt.check_password_hash(hashed_password, password)