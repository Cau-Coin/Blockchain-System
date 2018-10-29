# -*- coding: utf-8 -*-
import threading

import pymongo

from blockchain_manager.genesis_block import create_genesis_block
from blockchain_manager.leader_adapter import propose_block
from blockchain_manager.node_adapter import send_tx_msg


class Blockchain:
    def __init__(self, ip, db, chain_col, state_col, leader):
        self.my_ip = ip

        # mongo db connection
        self.client = pymongo.MongoClient('0.0.0.0')
        self.db = self.client[db]

        # block db
        self.chain = self.db[chain_col]

        # state db
        self.state = self.db[state_col]

        self.tx_list = []
        self.leader = leader
        self.last_block = create_genesis_block(self.my_ip)

        self.batch_to_block()

    def send_transaction(self):
        for tx in self.tx_list:
            send_tx_msg(tx, self.my_ip)

        self.tx_list.clear()

    def save_transaction(self, tx):
        self.tx_list.append(tx)
        self.check_to_save_block()

    def check_to_save_block(self):
        if self.my_ip is self.leader:
            block, tx_num_to_remove = propose_block(self.last_block, self.tx_list, self.my_ip)

            if block is None:
                return

            self.save_block(block)
            self.tx_list = self.tx_list[tx_num_to_remove]
        else:
            self.send_transaction()

    def batch_to_block(self):
        timer = threading.Timer(30, self.check_to_save_block)
        timer.start()

    def save_block(self, block):
        self.last_block = block
        self.chain.insert(block)
        self.update_state(block)

    def update_state(self, block):
        for tx in block["transactions"]:
            if tx["type"] == "evaluate":
                data = {
                    "evaluate_id": tx["evaluate_id"],
                    "user_id": tx["user_id"],
                    "dept": tx["dept"],
                    "grade": tx["grade"],
                    "semester": tx["semester"],
                    "subject": tx["subject"],
                    "takeyear": tx["takeyear"],
                    "evaluate": tx["evaluate"],
                    "review": tx["review"],
                    "timestamp": tx["timestamp"],
                    "comments": [],
                    "scores": []
                }

                self.state.insert(data)
            elif tx["type"] == "comment":
                self.state.update(
                    {"evaluate_id": tx["evaluate_id"]},
                    {
                        "$addToSet": {
                            "comments": {
                                "user_id": tx["user_id"],
                                "comment": tx["comment"],
                                "timestamp": tx["timestamp"]
                            }
                        }
                    }
                )
            elif tx["type"] == "score":
                self.state.update(
                    {"evaluate_id": tx["evaluate_id"]},
                    {
                        "$addToSet": {
                            "scores": {
                                "user_id": tx["user_id"],
                                "score": tx["score"],
                                "timestamp": tx["timestamp"]
                            }
                        }
                    }
                )
            else:
                print("[Error] Not defined transaction!")

    def update_leader(self, new_leader):
        self.leader = new_leader
