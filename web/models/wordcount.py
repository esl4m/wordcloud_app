from datetime import datetime
from peewee import *
from .database import BaseModel
from ..utils import generate_hash, RSA_KEY, RSA_PUBLIC_KEY


class WordCount(BaseModel):

    id = CharField(primary_key=True)
    word = BlobField(default='')
    count = IntegerField(default=0)
    created = DateTimeField(default=datetime.now)
    updated = DateTimeField(default=datetime.now)

    @classmethod
    def encrypt(self, word):
        return RSA_PUBLIC_KEY.encrypt(str(word), 32)[0]

    def decrypted_word(self):
        return RSA_KEY.decrypt(self.word)

    @classmethod
    def generate_hash(self, word):
        return generate_hash(word)

__all__ = ['WordCount']
