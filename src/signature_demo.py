#!/usr/bin/env python3
"""
Digital Signature: ML-DSA-65 (Dilithium)
"""
import oqs

def generate_keypair():
    with oqs.Signature("Dilithium-3") as s:
        pub = s.generate_keypair()
        priv = s.export_secret_key()
    return pub, priv

def sign(priv, msg):
    with oqs.Signature("Dilithium-3") as s:
        s.import_secret_key(priv)
        return s.sign(msg)

def verify(pub, msg, sig):
    with oqs.Signature("Dilithium-3") as s:
        return s.verify(msg, sig, pub)

if __name__ == "__main__":
    pub, priv = generate_keypair()
    msg = b"Transaction: 1,000,000 EUR"
    sig = sign(priv, msg)
    assert verify(pub, msg, sig)
    print("✅ Dilithium signature successful!")
