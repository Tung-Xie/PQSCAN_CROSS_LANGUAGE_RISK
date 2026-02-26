from Crypto.PublicKey import RSA
from Crypto.Hash import MD5

def legacy_crypto():
    # 這裡也用了 RSA-1024 (High Risk)
    key = RSA.generate(1024)
    
    # 這裡也用了 MD5
    h = MD5.new()
    h.update(b'data')
    return h.hexdigest()
