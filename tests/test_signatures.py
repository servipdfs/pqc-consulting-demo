import pytest
import sys
sys.path.append('src')
from signature_demo import generate_dilithium_keypair, sign_message, verify_signature

def test_dilithium_signature():
    pub, priv = generate_dilithium_keypair()
    msg = b"Important transaction data"
    sig = sign_message(priv, msg)
    assert verify_signature(pub, msg, sig) == True
