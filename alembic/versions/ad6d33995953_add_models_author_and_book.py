"""Add models Author and Book

Revision ID: ad6d33995953
Revises:
Create Date: 2021-11-24 08:27:49.422133

"""
from typing import Any

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "ad6d33995953"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> Any:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "authors",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "books",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("pub_date", sa.DATE(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "book_m2m_author",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("books_id", sa.Integer(), nullable=True),
        sa.Column("authors_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["authors_id"],
            ["authors.id"],
        ),
        sa.ForeignKeyConstraint(
            ["books_id"],
            ["books.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> Any:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("book_m2m_author")
    op.drop_table("books")
    op.drop_table("authors")
    # ### end Alembic commands ###