#!/usr/bin/env python3
"""
Digital Signature: ML-DSA-65 (Dilithium)
"""
import oqs

def generate_keypair():
    with oqs.Signature("ML-DSA-65") as s:
        pub = s.generate_keypair()
        priv = s.export_secret_key()
    return pub, priv

def sign(priv, msg):
    # Le pasamos la clave privada como parámetro (secret_key=priv)
    with oqs.Signature("ML-DSA-65", secret_key=priv) as s:
        return s.sign(msg)

def verify(pub, msg, sig):
    with oqs.Signature("ML-DSA-65") as s:
        return s.verify(msg, sig, pub)

if __name__ == "__main__":
    pub, priv = generate_keypair()
    msg = b"Transaction: 1,000,000 EUR"
    sig = sign(priv, msg)
    assert verify(pub, msg, sig)
    print("✅ ML-DSA-65 signature successful!")
