import datetime as date


class Transaction:
    def __init__(self, maker):
        # todo : generate random tx id
        # self.txID =
        self.maker = maker
        self.timestamp = date.datetime.now()

    # todo : change tx to byte
    def serialize(self):
        pass


class GetInfoTx(Transaction):
    def __init__(self, maker, subject):
        super(GetInfoTx, self).__init__(maker)
        self.subject = subject

        # todo : get
        # self.content =
        # self.score =
        # self.comments =


class EvaluateTx(Transaction):
    def __init__(self, maker, subject, content):
        super(EvaluateTx, self).__init__(maker)

        # todo
        # self.evaluateID =
        # self.subject = subject
        # self.content = content


class ScoreTx(Transaction):
    def __init__(self, maker, evaluateID, score):
        super(ScoreTx, self).__init__(maker)
        self.evaluateID = evaluateID
        self.score = score


class CommentTx(Transaction):
    def __init__(self, maker, evaluateID, comment):
        super(CommentTx, self).__init__(maker)
        self.evaluateID = evaluateID
        self.comment = comment