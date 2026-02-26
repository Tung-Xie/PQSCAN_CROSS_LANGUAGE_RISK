from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def trigger_high_risk_python():
    # --- RSA-1024 (High Risk) ---
    # 使用 cryptography 庫的標準生成方式，CBOMkit 對此特徵最敏感
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=1024, # 這裡標記 1024
    )

    # --- MD5 (High Risk) ---
    # 明確呼叫 hashes.MD5()
    digest = hashes.Hash(hashes.MD5())
    digest.update(b"bad_idea")
    result = digest.finalize()

    # --- SHA-1 (High Risk) ---
    digest_sha1 = hashes.Hash(hashes.SHA1())
    digest_sha1.finalize()

    return "Python Crypto Triggered"
