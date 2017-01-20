"""drop unique constraints on task and due date

Revision ID: 24ddb6bdbbed
Revises:
Create Date: 2017-01-20 11:28:58.167552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24ddb6bdbbed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint(unique, event, type_=unique, schema=None)

def downgrade():
    pass
