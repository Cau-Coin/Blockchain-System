import hashlib
import datetime as date


class Block:
    def __init__(self, index, timestamp, data, prev_hash, constructor):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.constructor = constructor
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        hash_data = str(self.index) + str(self.timestamp) + str(self.data) + str(self.prev_hash) + str(self.constructor)
        sha.update(hash_data.encode('utf-8'))
        return sha.hexdigest()


def new_block(last_block, data):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = last_block.data + str(data)
    this_prev_hash = last_block.hash
    # todo : a value of constructor is IP?
    this_constructor = "myIP"
    return Block(this_index, this_timestamp, this_data, this_prev_hash, this_constructor)

