from app_config import bcrypt

def create_password_hash(password: str):
    return bcrypt.generate_password_hash(password).decode('utf-8')

def verify_password_hash(hashed_password: str, password: str):
    return bcrypt.check_password_hash(hashed_password, password)