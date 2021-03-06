from app.extensions import db
from app.utilities.models import BaseModel


class Grant(db.Model, BaseModel):
    __tablename__ = 'grants'
    client_id = db.Column(
        db.String(100), db.ForeignKey('clients.client_id'), nullable=False
    )
    client = db.relationship('Client')
    code = db.Column(db.String(255), index=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User')
    redirect_uri = db.Column(db.String(255))
    expires = db.Column(db.DateTime)

    _scopes = db.Column(db.Text)

    @property
    def scopes(self):
        if self._scopes:
            return self._scopes.split(' ')
        return []

    def delete(self):
        self.deleted = True
        return self.commit()
