"""update user table

Revision ID: 28b9ecc810a8
Revises: 37598604bd58
Create Date: 2022-03-07 12:43:43.498173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "28b9ecc810a8"
down_revision = "37598604bd58"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users", sa.Column("registered_on", sa.DateTime(), nullable=True)
    )
    op.add_column("users", sa.Column("admin", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "admin")
    op.drop_column("users", "registered_on")
    # ### end Alembic commands ###