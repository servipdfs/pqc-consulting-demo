#!/usr/bin/env python3
"""
Hybrid Encryption: ML-KEM-768 (ML-KEM-768) + AES-256-GCM
"""
import oqs
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes

def hybrid_encrypt(public_key: bytes, plaintext: bytes):
    with oqs.KeyEncapsulation("ML-KEM-768") as kem:
        ciphertext, shared_secret = kem.encap_secret(public_key)
    hkdf = HKDF(algorithm=hashes.SHA256(), length=32, salt=None, info=b"hybrid")
    aes_key = hkdf.derive(shared_secret)
    aesgcm = AESGCM(aes_key)
    nonce = os.urandom(12)
    ciphertext_aes = aesgcm.encrypt(nonce, plaintext, None)
    return ciphertext, nonce, ciphertext_aes

def hybrid_decrypt(secret_key, ciphertext_kem, nonce, ciphertext_aes):
    with oqs.KeyEncapsulation("ML-KEM-768") as kem:
        shared_secret = kem.decap_secret(ciphertext_kem)
    hkdf = HKDF(algorithm=hashes.SHA256(), length=32, salt=None, info=b"hybrid")
    aes_key = hkdf.derive(shared_secret)
    aesgcm = AESGCM(aes_key)
    return aesgcm.decrypt(nonce, ciphertext_aes, None)

if __name__ == "__main__":
    with oqs.KeyEncapsulation("ML-KEM-768") as kem:
        pub = kem.generate_keypair()
        priv = kem.export_secret_key()
    msg = b"Transfer 1,000,000 EUR"
    ct_kem, nonce, ct_aes = hybrid_encrypt(pub, msg)
    dec = hybrid_decrypt(priv, ct_kem, nonce, ct_aes)
    assert msg == dec
    print("✅ Hybrid encryption/decryption successful!")
