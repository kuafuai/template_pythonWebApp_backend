from app import db

class Demo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    info1 = db.Column(db.String(80), unique=True, nullable=False)
    info2 = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, info1, info2):
        self.info1 = info1
        self.info2 = info2