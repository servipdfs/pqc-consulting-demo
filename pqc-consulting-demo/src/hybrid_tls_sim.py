#!/usr/bin/env python3
"""
Hybrid TLS 1.3 handshake: X25519 + Kyber-768
"""
import oqs
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes

def simulate():
    # Server keys
    s_x25519_priv = X25519PrivateKey.generate()
    s_x25519_pub = s_x25519_priv.public_key()
    s_kem = oqs.KeyEncapsulation("Kyber-768")
    s_kem_pub = s_kem.generate_keypair()
    s_kem_priv = s_kem.export_secret_key()

    # Client keys
    c_x25519_priv = X25519PrivateKey.generate()
    c_x25519_pub = c_x25519_priv.public_key()
    c_kem = oqs.KeyEncapsulation("Kyber-768")
    kem_ct, kem_shared = c_kem.encap_secret(s_kem_pub)

    # Server decaps
    s_kem2 = oqs.KeyEncapsulation("Kyber-768")
    s_kem2.import_secret_key(s_kem_priv)
    kem_shared2 = s_kem2.decap_secret(kem_ct)
    assert kem_shared == kem_shared2

    # X25519
    x_shared_c = c_x25519_priv.exchange(s_x25519_pub)
    x_shared_s = s_x25519_priv.exchange(c_x25519_pub)
    assert x_shared_c == x_shared_s

    combined = kem_shared + x_shared_c
    final_key = HKDF(algorithm=hashes.SHA256(), length=32, salt=None, info=b"hybrid-tls13").derive(combined)
    print(f"✅ Hybrid handshake OK. Key: {final_key.hex()[:32]}...")

if __name__ == "__main__":
    simulate()