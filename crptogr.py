# cryptographic_features.py
import hashlib

def hash_block(block):
    return hashlib.sha256(str(block).encode()).hexdigest()

class CryptographicNode(SecureNode):
    def __init__(self):
        super().__init__()
        self.chain_hashes = []

    def receive_block(self, block):
        if validate_block(block):
            self.blockchain.append(block)
            self.chain_hashes.append(hash_block(block))

    def validate_chain(self):
        for i in range(1, len(self.chain_hashes)):
            if self.chain_hashes[i] != hash_block(self.blockchain[i]):
                return False
        return True

    def validate_block_hash(self, block):
        return hash_block(block) in self.chain_hashes