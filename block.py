# blockchain/block.py
import hashlib
import json
import time

class Block:
    """
    Представляє окремий блок у блокчейні.
    """
    def __init__(self, index, transactions, previous_hash, nonce=0):
        self.index = index  # Порядковий номер блоку
        self.timestamp = time.time()  # Час створення
        self.transactions = transactions  # Транзакції у блоці
        self.previous_hash = previous_hash  # Хеш попереднього блоку
        self.nonce = nonce  # Значення для майнінгу (якщо потрібно)
        self.hash = self.calculate_hash()  # Власний хеш

    def calculate_hash(self):
        """
        Обчислює SHA-256 хеш поточного блоку.
        """
        # Створюємо рядок з усіх полів блоку
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()

        # Повертаємо SHA-256 хеш цього рядка
        return hashlib.sha256(block_string).hexdigest()
