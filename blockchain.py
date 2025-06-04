from block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.difficulty = 2
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [], "0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def mine_block(self, transactions):
        nonce = 0
        last_block = self.get_last_block()
        while True:
            new_block = Block(len(self.chain), transactions, last_block.hash, nonce)
            if new_block.hash.startswith("0" * self.difficulty):
                return new_block
            nonce += 1

    def add_block(self, transactions):
        new_block = self.mine_block(transactions)
        if self.is_valid_block(new_block, self.get_last_block()):
            self.chain.append(new_block)

    def is_valid_block(self, block, previous_block):
        if block.previous_hash != previous_block.hash:
            return False
        if block.hash != block.compute_hash():
            return False
        if not block.hash.startswith("0" * self.difficulty):
            return False
        return True
