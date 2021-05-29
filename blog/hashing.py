from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')


def bcrypt(password: str):
    hashed_password = pwd_cxt.hash(password)
    return hashed_password
