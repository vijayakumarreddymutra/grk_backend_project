
from cryptography.fernet import Fernet

key = Fernet.generate_key()

print(key)

data_enc = Fernet(key)

text = b"hello Virat"

enc_text = data_enc.encrypt(text)

print(enc_text)

dec = data_enc.decrypt(enc_text)

print(dec)
