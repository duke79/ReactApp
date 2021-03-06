from sqlalchemy import ForeignKey
from sqlalchemy.sql import expression

from ... import db
from ...data.tables.project import Project
from ...data.tables.user import User


class Issue(db.Model):
    __tablename__ = 'issue'
    project = db.Column(db.Integer, ForeignKey(Project.id),
                        server_default=None, nullable=True)
    count = db.Column(db.Integer, nullable=False, server_default="1")
    title = db.Column(db.String(500), server_default=None, nullable=True)
    state = db.Column(db.String(50), server_default='open', nullable=False,
                      comment="'allow ''open'' & ''closed'")
    description = db.Column(db.Text(), server_default=None, nullable=True)
    created_by = db.Column(db.Integer, ForeignKey(User.id),
                           server_default=None, nullable=True)
    closed_at = db.Column(db.DateTime(), server_default=None, nullable=True)
    closed_by = db.Column(db.Integer, ForeignKey(User.id),
                          server_default=None, nullable=True)
    discussion_locked = db.Column(db.Boolean(), nullable=False, server_default=expression.false())

    __table_args__ = (db.UniqueConstraint('project', 'count', name='project_count'),)
