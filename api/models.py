from app import db

class Buys(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    created_at = db.Column(db.Date)
    def to_dict(self):
        return {
            "id": self.id,
            "price": self.price,
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }