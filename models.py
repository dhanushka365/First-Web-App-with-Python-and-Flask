from app import db

class Task(db.Model):
    id = db.column(db.Integer, primary_key=True)
    title = db.column(db.String(100),nullable=False)
    date = db.column(db.Date, nullable=False)

    def __repr__(self):
        return f'{self.title} created on{self.date}'