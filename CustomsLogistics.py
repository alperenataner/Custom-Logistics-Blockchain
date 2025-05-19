import json
import hashlib
import time
from datetime import datetime

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_data = {
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }
        block_string = json.dumps(block_data, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class CustomsLogisticsBlockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []

    def create_genesis_block(self):
        return Block(0, [], time.time(), "0")
    
    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_pending_transaction(self):
        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions,
            timestamp=time.time(),
            previous_hash=self.get_latest_block().hash
        )
        self.chain.append(new_block)
        self.pending_transactions = []

    def get_latest_block(self):
        return self.chain[-1]

    def get_shipment_status(self, tracking_number):
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.get("tracking_number") == tracking_number:
                    return transaction
        return None

    def print_chain(self):
        for block in self.chain:
            print(f"\n --- Block #{block.index} ---")
            print(f"Zaman: {datetime.fromtimestamp(block.timestamp).strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Önceki Hash: {block.previous_hash}")
            print(f"Bu Block Hash: {block.hash}")
            print("İşlemler:")
            for transaction in block.transactions:
                print(f"  - {transaction}")

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]

            if current.hash != current.calculate_hash():
                print(f"Blok {current.index} geçersiz! Veri değiştirilmiş olabilir")
                return False

            if current.previous_hash != previous.hash:
                print("Zincir kopmuş! Veri güvende değil")
                return False
        return True

    def get_all_shipments(self):
        shipments = {}
        for block in self.chain:
            for transaction in block.transactions:
                tracking_number = transaction.get("tracking_number")
                if tracking_number:
                    shipments[tracking_number] = transaction
        return shipments 