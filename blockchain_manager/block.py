import hashlib
import datetime as date
import json


def new_block(index, timestamp, transactions, prev_hash, constructor, this_hash):
    block_dict_data = {
        "index": index,
        "timestamp": str(timestamp),
        "transactions": transactions,
        "prev_hash": prev_hash,
        "constructor": constructor,
        "this_hash": this_hash
    }

    return block_dict_data


def block_to_json(block):
    return json.dumps(block)


def json_to_block(json_block):
    return json.loads(json_block)


def hash_block(index, timestamp, transactions, prev_hash, constructor):
    sha = hashlib.sha256()
    tx_hash_data = ""
    for tx in transactions:
        tx_hash_data += str(tx)

    hash_data = str(index) + str(timestamp) + tx_hash_data + str(prev_hash) + str(constructor)
    sha.update(hash_data.encode('utf-8'))
    return sha.hexdigest()


def create_block(last_block, transactions, my_address):
    new_index = last_block["index"] + 1
    new_timestamp = str(date.datetime.now())
    new_transactions = transactions
    new_prev_hash = last_block["this_hash"]
    new_constructor = my_address
    new_hash = hash_block(new_index, new_timestamp, new_transactions, new_prev_hash, new_constructor)

    return new_block(new_index, new_timestamp, new_transactions, new_prev_hash, new_constructor, new_hash)
