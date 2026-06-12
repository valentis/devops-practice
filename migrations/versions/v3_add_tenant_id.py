"""Add tenant_id to all user tables
Revision ID: a1b2c3d4e5f6
"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    for table in ["users", "posts", "comments", "files"]:
        op.add_column(table, sa.Column("tenant_id", sa.Integer(), nullable=True))
        op.execute(f"UPDATE {table} SET tenant_id = 1")
        op.alter_column(table, "tenant_id", nullable=False)
        op.create_index(f"ix_{table}_tenant_id", table, ["tenant_id", "id"])

def downgrade():
    for table in ["users", "posts", "comments", "files"]:
        op.drop_index(f"ix_{table}_tenant_id", table)
        op.drop_column(table, "tenant_id")
