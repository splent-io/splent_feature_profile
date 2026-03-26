from splent_framework.db import db


class UserProfile(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), unique=True, nullable=False
    )

    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)

    # Relationship owned by profile (the dependent feature per UVL: profile => auth)
    user = db.relationship("User", backref=db.backref("profile", uselist=False))
