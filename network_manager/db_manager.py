# -*- coding: utf-8 -*-
import pymongo


class DataManager:
    def __init__(self, ip, db, chain_col, state_col, coin_col):
        self.ip = ip

        self.client = pymongo.MongoClient(ip)
        self.db = self.client[db]

        self.chain = self.db[chain_col]
        self.state = self.db[state_col]
        self.coin = self.db[coin_col]

    def get_all_data(self):
        return_data = {"eval": []}

        result = self.state.find()

        for data in result:
            del data["_id"]
            return_data["eval"].append(data)

        return return_data

    def get_one_data(self, evaluate_id):
        return_data = {"eval": []}

        result = self.state.find({"evaluate_id": evaluate_id})

        for data in result:
            del data["_id"]
            return_data["eval"].append(data)

        return return_data

    def get_coin_data(self, user_id):
        if self.coin.count_documents({"user_id": user_id}) == 0:
            return 0

        result = self.coin.find_one({"user_id": user_id})

        return result["coin"]
