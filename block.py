import hashlib
import datetime as date
import json


class Block:
    def __init__(self, index, timestamp, transactions, prev_hash, constructor, this_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.constructor = constructor
        self.this_hash = this_hash

    def to_json(self):
        json_data = {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "prev_hash": self.prev_hash,
            "constructor": self.constructor,
            "this_hash:": self.this_hash
        }

        return json.dumps(json_data)


def hash_block(index, timestamp, transactions, prev_hash, constructor):
    sha = hashlib.sha256()
    hash_data = str(index) + str(timestamp) + str(transactions) + str(prev_hash) + str(
        constructor)
    sha.update(hash_data.encode('utf-8'))
    return sha.hexdigest()


def to_block(data):
    index = data["index"]
    timestamp = data["timestamp"]
    transactions = data["transactions"]
    prev_hash = data["prev_hash"]
    constructor = data["constructor"]
    this_hash = data["this_hash"]

    return Block(index, timestamp, transactions, prev_hash, constructor, this_hash)


def new_block(last_block, transactions, my_address):
    new_index = last_block.index + 1
    new_timestamp = date.datetime.now()
    new_transactions = last_block.transactions + str(transactions)
    new_prev_hash = last_block.hash
    new_constructor = my_address
    new_hash = hash_block(new_index, new_timestamp, new_transactions, new_prev_hash, new_constructor)

    return Block(new_index, new_timestamp, new_transactions, new_prev_hash, new_constructor, new_hash)
