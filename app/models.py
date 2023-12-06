from app import db


class Config(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, nullable=True)
    key = db.Column(db.String(255), nullable=False)
    value = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    @staticmethod
    def create(parent_id, key, value, status):
        config = Config(parent_id=parent_id, key=key, value=value, status=status)
        db.session.add(config)
        db.session.commit()
        return config.id

    @staticmethod
    def update(id, value):
        config = Config.query.get(id)
        config.value = value
        db.session.commit()
        return config.id

    @staticmethod
    def update_status(id, status):
        config = Config.query.get(id)
        config.status = status
        db.session.commit()
        return config.id

    @staticmethod
    def get_value(key):
        config = Config.query.filter_by(key=key).first()
        if config:
            return {
                'key': config.key,
                'value': config.value,
                'status': config.status
            }
        else:
            return None


class AppConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(255), nullable=False)

    @staticmethod
    def create(value):
        app_config = AppConfig(value=value)
        db.session.add(app_config)
        db.session.commit()
        return app_config.id
