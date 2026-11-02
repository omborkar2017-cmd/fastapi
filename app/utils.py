from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# Important:
# import bcrypt

# def hash(password: str) -> str:
#     # 1. Convert plaintext string to bytes
#     password_bytes = password.encode('utf-8')
#     # 2. Generate salt
#     salt = bcrypt.gensalt()
#     # 3. Hash and decode back to string for database storage
#     hashed_bytes = bcrypt.hashpw(password_bytes, salt)
#     return hashed_bytes.decode('utf-8')

# def verify(plain_password: str, hashed_password: str) -> bool:
#     # Convert both to bytes for constant-time comparison
#     return bcrypt.checkpw(
#         plain_password.encode('utf-8'),
#         hashed_password.encode('utf-8')
#     )