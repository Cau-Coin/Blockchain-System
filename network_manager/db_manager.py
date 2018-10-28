# -*- coding: utf-8 -*-
import pymongo


class DataManager:
    def __init__(self, ip, db, chain_col, state_col):
        self.ip = ip

        self.client = pymongo.MongoClient(ip)
        self.db = self.client[db]

        self.chain = self.db[chain_col]
        self.state = self.db[state_col]

    def get_all_data(self):
        return_data = {"eval": []}

        result = self.state.find()

        for data in result:
            return_data["eval"].append(data)

        return return_data

    def get_one_data(self, evaluate_id):
        return_data = {"eval": []}

        result = self.state.find({"evaluate_id": evaluate_id})

        for data in result:
            return_data["eval"].append(data)

        return return_data
