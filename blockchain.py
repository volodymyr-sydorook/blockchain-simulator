from blockchain.block import Block

class Blockchain:
    """
    Клас, що управляє ланцюгом блоків.
    """
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        return Block(0, ["Genesis Block"], "0")

    def get_latest_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, block: Block) -> bool:
        if self.is_valid_new_block(block, self.get_latest_block()):
            self.chain.append(block)
            return True
        return False

    def is_valid_new_block(self, new_block: Block, previous_block: Block) -> bool:
        return (
            previous_block.index + 1 == new_block.index and
            previous_block.hash == new_block.previous_hash and
            new_block.hash == new_block.calculate_hash()
        )

    def __repr__(self):
        return "\n".join(f"{b.index}: {b.transactions}" for b in self.chain)
