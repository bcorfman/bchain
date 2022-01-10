import collections.abc
from cryptography.hazmat.primitives import hashes


class SampleClass:
    def __init__(self, data):
        if isinstance(data, collections.abc.ByteString):
            self.someString = data
        else:
            self.someString = bytes(str(data), encoding='UTF-8')


class CBlock:
    def __init__(self, data, previous_block, previous_hash=None):
        if isinstance(data, collections.abc.ByteString):
            self.data = data
        else:
            self.data = bytes(str(data), encoding='UTF-8')
        self.previousBlock = previous_block
        if previous_block is not None:
            self.previousHash = self.previousBlock.computeHash()

    def computeHash(self):
        digest = hashes.Hash(hashes.SHA256())
        digest.update(self.data)
        return digest.finalize()
