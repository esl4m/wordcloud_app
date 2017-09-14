import hashlib
import os
from Crypto.PublicKey import RSA


PK_SALT = os.getenv('PK_SALT', 'b758fbf75a2d489aa248f270da956bae')

# asymmetric encrytion
RSA_KEYFILE = os.path.join(os.path.dirname(__file__), 'rsakey')
RSA_KEY = RSA.importKey(open(RSA_KEYFILE, 'r').read())
RSA_PUBLIC_KEY = RSA_KEY.publickey()


def generate_hash(word):
    return hashlib.sha1(word + PK_SALT).hexdigest()


__all__ = ['RSA_KEY', 'RSA_PUBLIC_KEY', 'generate_hash']
