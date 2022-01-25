"""Initial Migration

Revision ID: 37598604bd58
Revises: 
Create Date: 2022-01-21 09:44:20.933235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "37598604bd58"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("email", sa.UnicodeText(), nullable=False),
        sa.Column("username", sa.UnicodeText(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
    )
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)
    op.create_table(
        "passwords",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("password", sa.UnicodeText(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_passwords_user_id_users")
        ),
        sa.PrimaryKeyConstraint("user_id", name=op.f("pk_passwords")),
    )
    op.create_table(
        "user_tokens",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("user_token", sa.UnicodeText(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_user_tokens_user_id_users")
        ),
        sa.PrimaryKeyConstraint("user_id", name=op.f("pk_user_tokens")),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user_tokens")
    op.drop_table("passwords")
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_table("users")
    # ### end Alembic commands ###
