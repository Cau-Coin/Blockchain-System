from block import *
from transaction import *
from leader_adapter import *
from node_adapter import *
import pymongo


class Blockchain:
    def __init__(self, ip, port, db, chain_col, state_col, leader):
        self.my_ip = ip

        # mongo db connection
        self.conn = pymongo.MongoClient(ip, port)
        self.db = self.conn.get_database(db)

        # block db
        self.chain = self.db.get_collection(chain_col)

        # state db
        self.state = self.db.get_collection(state_col)

        self.tx_list = []
        self.leader = leader

    def send_transaction(self):
        for tx in self.tx_list:
            tx_json = tx.to_json()
            send_tx_msg(tx_json, self.my_ip)

        self.tx_list.clear()

    def save_transaction(self, tx):
        self.tx_list.append(tx)

    def save_block(self, block):
        self.chain.insert(block)
        self.update_state(block)

    def update_state(self, block):
        state = self.state

        for tx in block.transactions:
            if type(tx) == type(EvaluateTx):
                json_data = tx.to_json
                json.dumps(json_data)
                json_data.push({
                    "comments": [],
                    "scores": []
                })
                state.insert(json_data)
            elif type(tx) == type(CommentTx):
                evaluate_id = tx.evaluate_id
                comment = tx.comment
                state.update(
                    {"evaluate_id": evaluate_id},
                    {"comments.$push": {"comment": comment}}
                )
            elif type(tx) == type(ScoreTx):
                evaluate_id = tx.evaluate_id
                score = tx.score
                state.update(
                    {"evaluate_id": evaluate_id},
                    {"scores.$push": {"score": score}}
                )
            else:
                print("[Error] Not defined transaction!")
                return
