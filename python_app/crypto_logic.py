from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def cross_lang_risk():
    # [High Risk] RSA-1024
    priv_key = rsa.generate_private_key(public_exponent=65537, key_size=1024)

    # [High Risk] MD5
    digest = hashes.Hash(hashes.MD5())
    digest.update(b"shared_secret")
    digest.finalize()

    # [Medium Risk] AES-128-CBC (跨語言常用，但 CBC 需要 IV 管理)
    key = os.urandom(16) # 128 bits
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
