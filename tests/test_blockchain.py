import unittest
import sys
import os

# Додаємо кореневу папку до шляхів імпорту
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from block import Block
from blockchain import Blockchain

class TestBlockchain(unittest.TestCase):

    def test_block_hash_is_correct(self):
        block = Block(1, [{"from": "A", "to": "B", "amount": 10}], "0")
        expected_hash = block.compute_hash()
        self.assertEqual(block.hash, expected_hash)

    def test_genesis_block_is_created(self):
        blockchain = Blockchain()
        self.assertEqual(len(blockchain.chain), 1)
        self.assertEqual(blockchain.chain[0].index, 0)

    def test_add_block(self):
        blockchain = Blockchain()
        blockchain.add_block([{"from": "Alice", "to": "Bob", "amount": 25}])
        self.assertEqual(len(blockchain.chain), 2)
        self.assertEqual(blockchain.chain[1].transactions[0]["from"], "Alice")

    def test_block_is_valid(self):
        blockchain = Blockchain()
        new_block = blockchain.mine_block([{"from": "A", "to": "B", "amount": 100}])
        last_block = blockchain.get_last_block()
        self.assertTrue(blockchain.is_valid_block(new_block, last_block))

    def test_invalid_previous_hash(self):
        blockchain = Blockchain()
        block = Block(1, [{"from": "A", "to": "B", "amount": 10}], "fakehash", nonce=0)
        self.assertFalse(blockchain.is_valid_block(block, blockchain.get_last_block()))

if __name__ == "__main__":
    unittest.main()
