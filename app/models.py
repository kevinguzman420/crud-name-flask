from app import db

class UserName(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    phone = db.Column(db.String(13), nullable=False)

    def __repr__(self):
        return f'<Name {self.name}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_user_by_id(id):
        return UserName.query.get(id)
        
    # Get all users:
    @staticmethod
    def get_all_user():
        return UserName.query.all()

    # Verify if an email it's already in use:
    @staticmethod
    def get_by_email(email):
        return UserName.query.filter_by(email=email).first()