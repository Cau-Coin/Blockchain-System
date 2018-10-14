from block import *
from transaction import *
from leader_adapter import *
from node_adapter import *


class Blockchain:
    def __init__(self):
        self.chain = []
        self.tx_list = []
        self.leader = ""

    def new_transaction(self):
        # tx type matching
        if ():
            pass
        elif ():
            pass
        elif ():
            pass
        elif ():
            pass
        else:
            pass

        # save tx
        # self.tx_list.append()

    def send_transaction(self):
        for tx in self.tx_list:
            send_tx_msg(tx)

        self.tx_list.clear()

    def save_transaction(self, tx):
        self.tx_list.append(tx)

    def save_block(self, block):
        # receive a block from leader

        self.chain.append(block)
