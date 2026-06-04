import pytest
import sys
sys.path.append('src')
from kem_hybrid_demo import hybrid_encrypt, hybrid_decrypt
import oqs

def test_hybrid_encryption_decryption():
    with oqs.KeyEncapsulation("Kyber-768") as kem:
        pub = kem.generate_keypair()
        priv = kem.export_secret_key()
    
    plaintext = b"Test message 12345"
    ct_kem, nonce, ct_aes = hybrid_encrypt(pub, plaintext)
    decrypted = hybrid_decrypt(priv, ct_kem, nonce, ct_aes)
    assert plaintext == decrypted
