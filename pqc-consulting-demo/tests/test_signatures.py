import sys
sys.path.append('src')
from signature_demo import generate_keypair, sign, verify

def test_sign():
    pub, priv = generate_keypair()
    msg = b"test"
    sig = sign(priv, msg)
    assert verify(pub, msg, sig) is True