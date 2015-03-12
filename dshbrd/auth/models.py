from dshbrd.database import db
from flask.ext.security import UserMixin, RoleMixin

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    __table_name__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    display_name = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    @property
    def display_name_or_email(self):
        if self.display_name and len(str(self.display_name)):
            return self.display_name
        return self.email

    @property
    def verbose_roles(self):
        return ', '.join(role.name for role in self.roles)

    @classmethod
    def get_by_id(cls, id):
        if any((isinstance(id, basestring) and id.isdigit(),
                isinstance(id, (int, float))),):
            return cls.query.get(int(id))
        return None
