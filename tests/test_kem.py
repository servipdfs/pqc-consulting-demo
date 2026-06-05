import sys
sys.path.append('src')
from kem_hybrid_demo import hybrid_encrypt, hybrid_decrypt
import oqs

def test_hybrid():
    with oqs.KeyEncapsulation("ML-KEM-768") as kem:
        pub = kem.generate_keypair()
        priv = kem.export_secret_key()
    msg = b"test"
    ct, nonce, aes_ct = hybrid_encrypt(pub, msg)
    dec = hybrid_decrypt(priv, ct, nonce, aes_ct)
    assert msg == dec
