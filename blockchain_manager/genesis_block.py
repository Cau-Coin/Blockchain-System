import datetime as date

from blockchain_manager.block import hash_block, new_block


def create_genesis_block(ip):
    index = 0
    timestamp = date.datetime.now()
    transactions = [{}]
    prev_hash = "no_hash"
    this_hash = hash_block(index, timestamp, transactions, prev_hash, ip)

    return new_block(0, str(date.datetime.now()), [{}], "no_hash", ip, this_hash)
