import datetime as date
from block import Block


# Normally genesis block is JSON file
def create_genesis_block():
    # todo : how first transaction?
    # todo : is a value of constructor IP?
    return Block(0, date.datetime.now(), "Genesis Block", "0", "myIP")
