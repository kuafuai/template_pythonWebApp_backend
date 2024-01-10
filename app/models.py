class FormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    has_family = db.Column(db.Boolean, nullable=False)
    has_shuttle = db.Column(db.Boolean, nullable=False)
    has_activity = db.Column(db.Boolean, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return FormData.query.all()
