import datetime as date
import json
import uuid


class Transaction:
    def __init__(self, tx_id, tx_maker, timestamp):
        self.tx_id = tx_id
        self.tx_maker = tx_maker
        self.timestamp = timestamp


class EvaluateTx(Transaction):
    def __init__(self, tx_id, tx_maker, timestamp, evaluate_id, dept, grade, semester, subject, takeyear, score,
                 review):
        super(EvaluateTx, self).__init__(tx_id, tx_maker, timestamp)

        self.evaluate_id = evaluate_id
        self.dept = dept
        self.grade = grade
        self.semester = semester
        self.subject = subject
        self.takeyear = takeyear
        self.score = score
        self.review = review

    def to_json(self):
        json_data = {
            "tx_id": self.tx_id,
            "tx_maker": self.tx_maker,
            "timestamp": self.timestamp,
            "evaluate_id": self.evaluate_id,
            "dept": self.dept,
            "grade": self.grade,
            "semester": self.semester,
            "subject": self.subject,
            "takeyear": self.takeyear,
            "score": self.score,
            "review": self.review
        }

        return json.dumps(json_data)


def to_evaluate_tx(json_data):
    data = json.loads(json_data)

    tx_id = data["tx_id"]
    tx_maker = data["tx_maker"]
    timestamp = data["timestamp"]
    evaluate_id = data["evaluate_id"]
    dept = data["dept"]
    grade = data["grade"]
    semester = data["semester"]
    subject = data["subject"]
    takeyear = data["takeyear"]
    score = data["score"]
    review = data["review"]

    return EvaluateTx(tx_id, tx_maker, timestamp, evaluate_id, dept, grade, semester, subject, takeyear, score, review)


def new_evaluate_tx(tx_maker, timestamp, dept, grade, semester, subject, takeyear, score, review):
    tx_id = str(uuid.uuid4())
    evaluate_id = str(uuid.uuid4())

    return EvaluateTx(tx_id, tx_maker, timestamp, evaluate_id, dept, grade, semester, subject, takeyear, score, review)


class CommentTx(Transaction):
    def __init__(self, tx_id, tx_maker, timestamp, evaluate_id, comment):
        super(CommentTx, self).__init__(tx_id, tx_maker, timestamp)

        self.evaluate_id = evaluate_id
        self.comment = comment

    def to_json(self):
        json_data = {
            "tx_id": self.tx_id,
            "tx_maker": self.tx_maker,
            "timestamp": self.timestamp,
            "evaluate_id": self.evaluate_id,
            "comment": self.comment,
        }

        return json.dumps(json_data)


def to_comment_tx(json_data):
    data = json.loads(json_data)

    tx_id = data["tx_id"]
    tx_maker = data["tx_maker"]
    timestamp = data["timestamp"]
    evaluate_id = data["evaluate_id"]
    comment = data["comment"]

    return CommentTx(tx_id, tx_maker, timestamp, evaluate_id, comment)


def new_comment_tx(tx_maker, timestamp, evaluate_id, comment):
    tx_id = str(uuid.uuid4())

    return CommentTx(tx_id, tx_maker, timestamp, evaluate_id, comment)


class ScoreTx(Transaction):
    def __init__(self, tx_id, tx_maker, timestamp, evaluate_id, score):
        super(ScoreTx, self).__init__(tx_id, tx_maker, timestamp)

        self.evaluate_id = evaluate_id
        self.score = score

    def to_json(self):
        json_data = {
            "tx_id": self.tx_id,
            "tx_maker": self.tx_maker,
            "timestamp": self.timestamp,
            "evaluate_id": self.evaluate_id,
            "score": self.score
        }

        return json.dumps(json_data)


def to_score_tx(json_data):
    data = json.loads(json_data)

    tx_id = data["tx_id"]
    tx_maker = data["tx_maker"]
    timestamp = data["timestamp"]
    evaluate_id = data["evaluate_id"]
    score = data["score"]

    return ScoreTx(tx_id, tx_maker, timestamp, evaluate_id, score)


def new_score_tx(tx_maker, timestamp, evaluate_id, score):
    tx_id = str(uuid.uuid4())

    return ScoreTx(tx_id, tx_maker, timestamp, evaluate_id, score)


def new_transaction(json_data):
    tx_type = json_data["type"]

    if tx_type == "evaluate":
        tx_maker = json_data["userid"]
        dept = json_data["dept"]
        grade = json_data["grade"]
        semester = json_data["semester"]
        subject = json_data["subject"]
        takeyear = json_data["takeyear"]
        score = json_data["evaluate"]
        review = json_data["review"]
        timestamp = json_data["timestamp"]

        return new_evaluate_tx(tx_maker, timestamp, dept, grade, semester, subject, takeyear, score, review)

    elif tx_type == "comment":
        tx_maker = json_data["userid"]
        evaluate_id = json_data["evaluateid"]
        comment = json_data["comment"]
        timestamp = json_data["timestamp"]

        return new_comment_tx(tx_maker, timestamp, evaluate_id, comment)

    elif tx_type == "score":
        tx_maker = json_data["userid"]
        evaluate_id = json_data["evaluateid"]
        score = json_data["score"]
        timestamp = json_data["timestamp"]

        return new_score_tx(tx_maker, timestamp, evaluate_id, score)

    else:
        print("[Error] Not defined json type!")
        return
